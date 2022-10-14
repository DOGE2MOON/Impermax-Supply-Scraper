import time
import datetime
import json
import os
from web3 import Web3
import sys
import pandas as pd

start_time = time.time()

recipient = 'YOUR_ADDRESS_HERE'
chains = {
	'Ethereum': ['https://rpc.ankr.com/eth', '0x8C3736e2FE63cc2cD89Ee228D9dBcAb6CE5B767B'],
	'Polygon': ['https://rpc.ankr.com/polygon', '0xBB92270716C8c424849F17cCc12F4F24AD4064D6', '0x7F7AD5b16c97Aa9C2B0447C2676ce7D5CEFEbCd3'], #RPC, v1 Factory, v2 Factory
	'Arbitrum': ['https://arb1.arbitrum.io/rpc', '0x8C3736e2FE63cc2cD89Ee228D9dBcAb6CE5B767B'],
	'Avalanche': ['https://api.avax.network/ext/bc/C/rpc', '0x8C3736e2FE63cc2cD89Ee228D9dBcAb6CE5B767B'],
	'Fantom': ['https://rpc.ftm.tools/', '0x60aE5F446AE1575534A5F234D6EC743215624556'],
	'Moonriver': ['https://rpc.moonriver.moonbeam.network', '0x8C3736e2FE63cc2cD89Ee228D9dBcAb6CE5B767B']
	}


Impermax_Factory_ABI = json.loads('[{"inputs":[{"internalType":"address","name":"_admin","type":"address"},{"internalType":"address","name":"_reservesAdmin","type":"address"},{"internalType":"contract IBDeployer","name":"_bDeployer","type":"address"},{"internalType":"contract ICDeployer","name":"_cDeployer","type":"address"},{"internalType":"contract ISimpleUniswapOracle","name":"_simpleUniswapOracle","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"uniswapV2Pair","type":"address"},{"indexed":true,"internalType":"address","name":"token0","type":"address"},{"indexed":true,"internalType":"address","name":"token1","type":"address"},{"indexed":false,"internalType":"address","name":"collateral","type":"address"},{"indexed":false,"internalType":"address","name":"borrowable0","type":"address"},{"indexed":false,"internalType":"address","name":"borrowable1","type":"address"},{"indexed":false,"internalType":"uint256","name":"lendingPoolId","type":"uint256"}],"name":"LendingPoolInitialized","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"oldAdmin","type":"address"},{"indexed":false,"internalType":"address","name":"newAdmin","type":"address"}],"name":"NewAdmin","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"oldPendingAdmin","type":"address"},{"indexed":false,"internalType":"address","name":"newPendingAdmin","type":"address"}],"name":"NewPendingAdmin","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"oldReservesAdmin","type":"address"},{"indexed":false,"internalType":"address","name":"newReservesAdmin","type":"address"}],"name":"NewReservesAdmin","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"oldReservesManager","type":"address"},{"indexed":false,"internalType":"address","name":"newReservesManager","type":"address"}],"name":"NewReservesManager","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"oldReservesPendingAdmin","type":"address"},{"indexed":false,"internalType":"address","name":"newReservesPendingAdmin","type":"address"}],"name":"NewReservesPendingAdmin","type":"event"},{"constant":false,"inputs":[],"name":"_acceptAdmin","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"_acceptReservesAdmin","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"newPendingAdmin","type":"address"}],"name":"_setPendingAdmin","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"newReservesManager","type":"address"}],"name":"_setReservesManager","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"newReservesPendingAdmin","type":"address"}],"name":"_setReservesPendingAdmin","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"admin","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"allLendingPools","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"allLendingPoolsLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"bDeployer","outputs":[{"internalType":"contract IBDeployer","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"cDeployer","outputs":[{"internalType":"contract ICDeployer","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"uniswapV2Pair","type":"address"}],"name":"createBorrowable0","outputs":[{"internalType":"address","name":"borrowable0","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"uniswapV2Pair","type":"address"}],"name":"createBorrowable1","outputs":[{"internalType":"address","name":"borrowable1","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"uniswapV2Pair","type":"address"}],"name":"createCollateral","outputs":[{"internalType":"address","name":"collateral","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"getLendingPool","outputs":[{"internalType":"bool","name":"initialized","type":"bool"},{"internalType":"uint24","name":"lendingPoolId","type":"uint24"},{"internalType":"address","name":"collateral","type":"address"},{"internalType":"address","name":"borrowable0","type":"address"},{"internalType":"address","name":"borrowable1","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"uniswapV2Pair","type":"address"}],"name":"initializeLendingPool","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"pendingAdmin","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"reservesAdmin","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"reservesManager","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"reservesPendingAdmin","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"simpleUniswapOracle","outputs":[{"internalType":"contract ISimpleUniswapOracle","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"}]')
LP_Token_ABI = json.loads('[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":true,"internalType":"address","name":"minter","type":"address"},{"indexed":false,"internalType":"uint256","name":"mintAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"mintTokens","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":true,"internalType":"address","name":"redeemer","type":"address"},{"indexed":false,"internalType":"uint256","name":"redeemAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"redeemTokens","type":"uint256"}],"name":"Redeem","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"caller","type":"address"},{"indexed":false,"internalType":"uint256","name":"reward","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"bounty","type":"uint256"}],"name":"Reinvest","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"totalBalance","type":"uint256"}],"name":"Sync","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":true,"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MINIMUM_LIQUIDITY","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"PERMIT_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"REINVEST_BOUNTY","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"WETH","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_stakingRewards","type":"address"},{"internalType":"address","name":"_underlying","type":"address"},{"internalType":"address","name":"_rewardsToken","type":"address"},{"internalType":"address","name":"_token0","type":"address"},{"internalType":"address","name":"_token1","type":"address"},{"internalType":"address","name":"_router","type":"address"},{"internalType":"address","name":"_WETH","type":"address"}],"name":"_initialize","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"_setFactory","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"exchangeRate","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getReserves","outputs":[{"internalType":"uint112","name":"reserve0","type":"uint112"},{"internalType":"uint112","name":"reserve1","type":"uint112"},{"internalType":"uint32","name":"blockTimestampLast","type":"uint32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"minter","type":"address"}],"name":"mint","outputs":[{"internalType":"uint256","name":"mintTokens","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"price0CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"price1CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"redeemer","type":"address"}],"name":"redeem","outputs":[{"internalType":"uint256","name":"redeemAmount","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"reinvest","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"rewardsToken","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"router","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"skim","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"stakingRewards","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"sync","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"token0","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"token1","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"underlying","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"}]')
erc_abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"usr","type":"address"}],"name":"Deny","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"usr","type":"address"}],"name":"Rely","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"PERMIT_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"burn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"usr","type":"address"}],"name":"deny","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"deploymentChainId","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"mint","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"usr","type":"address"}],"name":"rely","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"version","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"wards","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]')
imxB_abi = json.loads('[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"interestAccumulated","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"borrowIndex","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"totalBorrows","type":"uint256"}],"name":"AccrueInterest","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":true,"internalType":"address","name":"borrower","type":"address"},{"indexed":true,"internalType":"address","name":"receiver","type":"address"},{"indexed":false,"internalType":"uint256","name":"borrowAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"repayAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"accountBorrowsPrior","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"accountBorrows","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"totalBorrows","type":"uint256"}],"name":"Borrow","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"BorrowApproval","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"borrowRate","type":"uint256"}],"name":"CalculateBorrowRate","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"kinkRate","type":"uint256"}],"name":"CalculateKink","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"kinkBorrowRate","type":"uint256"}],"name":"CalculateKinkBorrowRate","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":true,"internalType":"address","name":"borrower","type":"address"},{"indexed":true,"internalType":"address","name":"liquidator","type":"address"},{"indexed":false,"internalType":"uint256","name":"seizeTokens","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"repayAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"accountBorrowsPrior","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"accountBorrows","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"totalBorrows","type":"uint256"}],"name":"Liquidate","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":true,"internalType":"address","name":"minter","type":"address"},{"indexed":false,"internalType":"uint256","name":"mintAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"mintTokens","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"newAdjustSpeed","type":"uint256"}],"name":"NewAdjustSpeed","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"newBorrowTracker","type":"address"}],"name":"NewBorrowTracker","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"newKinkUtilizationRate","type":"uint256"}],"name":"NewKinkUtilizationRate","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"newReserveFactor","type":"uint256"}],"name":"NewReserveFactor","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":true,"internalType":"address","name":"redeemer","type":"address"},{"indexed":false,"internalType":"uint256","name":"redeemAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"redeemTokens","type":"uint256"}],"name":"Redeem","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"totalBalance","type":"uint256"}],"name":"Sync","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":true,"inputs":[],"name":"ADJUST_SPEED_MAX","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"ADJUST_SPEED_MIN","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"BORROW_FEE","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"BORROW_PERMIT_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"KINK_BORROW_RATE_MAX","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"KINK_BORROW_RATE_MIN","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"KINK_MULTIPLIER","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"KINK_UR_MAX","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"KINK_UR_MIN","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MINIMUM_LIQUIDITY","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"PERMIT_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"RESERVE_FACTOR_MAX","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"string","name":"_name","type":"string"},{"internalType":"string","name":"_symbol","type":"string"},{"internalType":"address","name":"_underlying","type":"address"},{"internalType":"address","name":"_collateral","type":"address"}],"name":"_initialize","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"newAdjustSpeed","type":"uint256"}],"name":"_setAdjustSpeed","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"newBorrowTracker","type":"address"}],"name":"_setBorrowTracker","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"_setFactory","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"newKinkUtilizationRate","type":"uint256"}],"name":"_setKinkUtilizationRate","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"newReserveFactor","type":"uint256"}],"name":"_setReserveFactor","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"accrualTimestamp","outputs":[{"internalType":"uint32","name":"","type":"uint32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"accrueInterest","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"adjustSpeed","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"borrower","type":"address"},{"internalType":"address","name":"receiver","type":"address"},{"internalType":"uint256","name":"borrowAmount","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"borrow","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"borrowAllowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"borrowApprove","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"borrower","type":"address"}],"name":"borrowBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"borrowIndex","outputs":[{"internalType":"uint112","name":"","type":"uint112"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"borrowPermit","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"borrowRate","outputs":[{"internalType":"uint48","name":"","type":"uint48"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"borrowTracker","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"collateral","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"exchangeRate","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"exchangeRateLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getBlockTimestamp","outputs":[{"internalType":"uint32","name":"","type":"uint32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"kinkBorrowRate","outputs":[{"internalType":"uint48","name":"","type":"uint48"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"kinkUtilizationRate","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"borrower","type":"address"},{"internalType":"address","name":"liquidator","type":"address"}],"name":"liquidate","outputs":[{"internalType":"uint256","name":"seizeTokens","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"minter","type":"address"}],"name":"mint","outputs":[{"internalType":"uint256","name":"mintTokens","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"rateUpdateTimestamp","outputs":[{"internalType":"uint32","name":"","type":"uint32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"redeemer","type":"address"}],"name":"redeem","outputs":[{"internalType":"uint256","name":"redeemAmount","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"reserveFactor","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"skim","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"sync","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalBorrows","outputs":[{"internalType":"uint112","name":"","type":"uint112"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"borrower","type":"address"}],"name":"trackBorrow","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"underlying","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"}]')

# added 'speedrun' method that uses a pre-compiled CSV containing static variables that do not need to be pulled from the chain every time  
def get_info(chain, recipient, speedrun): 
	output = pd.DataFrame()
	
	if speedrun == True:
		# unless modified to provide absolute path, CSV file must be in the same directory as .py file
		imxB_list = pd.read_csv(chain + "_imxB.csv")

		for e in range(1, ((len(chains[chain][1:]))+1)):
			sys.stdout.write(" Current Position: ")
			web3 = Web3(Web3.HTTPProvider(chains[chain][0]))
			Impermax_Factory_Address = chains[chain][e]
			Impermax_Factory_Contract = web3.eth.contract(address=Impermax_Factory_Address, abi=Impermax_Factory_ABI)
			Lending_Pool_Length = Impermax_Factory_Contract.functions.allLendingPoolsLength().call({"from": recipient}) - 1
		
			for i in range(0, Lending_Pool_Length):
				LP_Address = Impermax_Factory_Contract.functions.allLendingPools(i).call({"from": recipient})
				LP_Contract = web3.eth.contract(address=LP_Address, abi=LP_Token_ABI)
				getLendingPool = Impermax_Factory_Contract.functions.getLendingPool(LP_Address).call({"from": recipient})
				initialized = getLendingPool[0]

				if initialized == True:

					token0_imxB_address = imxB_list["Token0 imxB Address"][i]
					token0_imxB_contract = web3.eth.contract(address=token0_imxB_address, abi=imxB_abi)
					token0_totalSupply = token0_imxB_contract.functions.totalSupply().call()
					token0_underlying_decimals = imxB_list["Token0 Underlying Decimals"][i]
					token0_totalBalance = token0_imxB_contract.functions.totalBalance().call() / 10**token0_underlying_decimals
				
					if token0_totalSupply <= 0:
						token0_borrowAPR = 0
						token0_RF = 0
						token0_totalBorrows = 0
						token0_borrowAPR = 0
						token0_supplyAPR = 0
						token0_utilization = 0
						token0_available = token0_totalSupply
						token0_balance = 0
						token0_exchangeRate = 0
						token0_symbol = "No Supply"
						token0_imxB_rate = 0.0000000001

					else:
						token0_address = imxB_list["Token0 Underlying Address"][i]
						token0_contract = web3.eth.contract(address=token0_address, abi=erc_abi)
						token0_symbol = imxB_list["Token0 Symbol"]
						
						token0_borrowAPR = token0_imxB_contract.functions.borrowRate().call() * 365 * 24 * 60 * 60 / 10**18
						token0_exchangeRate = token0_imxB_contract.functions.exchangeRateLast().call() / 10**18
						token0_RF = token0_imxB_contract.functions.reserveFactor().call()
						token0_totalSupply = token0_imxB_contract.functions.totalSupply().call()
						token0_totalBorrows = token0_imxB_contract.functions.totalBorrows().call()
						token0_supplyAPR = token0_borrowAPR * (1 - token0_RF / 10**18) * token0_totalBorrows / (token0_totalSupply * token0_exchangeRate)
						token0_balance = token0_imxB_contract.functions.balanceOf(recipient).call() / 10**18
						
						token0_utilization = token0_totalBorrows / (token0_totalSupply * token0_exchangeRate)
						token0_available = ((token0_totalSupply * token0_exchangeRate) - token0_totalBorrows) / 10**18
						token0_imxB_rate =  token0_available / token0_totalBalance
			

					token1_imxB_address = imxB_list["Token1 imxB Address"][i]
					token1_imxB_contract = web3.eth.contract(address=token1_imxB_address, abi=imxB_abi)
					token1_totalSupply = token1_imxB_contract.functions.totalSupply().call()
					token1_underlying_decimals = imxB_list["Token0 Underlying Decimals"][i]
					token1_totalBalance = token1_imxB_contract.functions.totalBalance().call() / 10**token1_underlying_decimals
					

					if token1_totalSupply <= 0:
						token1_borrowAPR = 0
						token1_RF = 0
						token1_totalBorrows = 0
						token1_borrowAPR = 0
						token1_supplyAPR = 0
						token1_utilization = 0
						token1_available = token0_totalSupply
						token1_balance = 0
						token1_exchangeRate = 0
						token1_symbol = "No Supply"
						token1_imxB_rate = 0.0000000001

					else:
						token1_address = imxB_list["Token1 Underlying Address"][i]
						token1_contract = web3.eth.contract(address=token1_address, abi=erc_abi)
						token1_symbol = imxB_list["Token1 Symbol"][i]

						token1_borrowAPR = token1_imxB_contract.functions.borrowRate().call() * 365 * 24 * 60 * 60 / 10**18
						token1_exchangeRate = token0_imxB_contract.functions.exchangeRateLast().call() / 10**18
						token1_RF = token1_imxB_contract.functions.reserveFactor().call()
						token1_totalSupply = token1_imxB_contract.functions.totalSupply().call()
						token1_totalBorrows = token1_imxB_contract.functions.totalBorrows().call()
						token1_supplyAPR = token1_borrowAPR * (1 - token1_RF / 10**18) * token1_totalBorrows / (token1_totalSupply * token1_exchangeRate)
						token1_utilization = token1_imxB_contract.functions.totalBorrows().__call__().call() / (token1_imxB_contract.functions.totalSupply().call({"from": recipient}) * token1_exchangeRate)
						token1_available = ((token1_totalSupply * token1_exchangeRate) - token1_totalBorrows) / 10**18
						token1_imxB_rate = token1_available / token1_totalBalance
						token1_balance = token1_imxB_contract.functions.balanceOf(recipient).call() / 10**18

			
				else: # catch non-initialized pairs
					token0_address = "Not Initialized"
					token0_contract = "Not Initialized"
					token0_symbol = "Not Initialized"
					token0_imxB_address = "Not Initialized"
					token0_imxB_contract = "Not Initialized"
					token0_exchangeRate = 0
					token0_borrowAPR = 0
					token0_RF = 0
					token0_totalSupply = 0
					token0_totalBorrows = 0
					token0_supplyAPR = 0
					token0_utilization = 0
					token0_available = 0
					token0_balance = 0
					token0_imxB_rate = 0.0000000001

					token1_address = "Not Initialized"
					token1_contract = "Not Initialized"
					token1_symbol = "Not Initialized"
					token1_imxB_address = "Not Initialized"
					token1_imxB_contract = "Not Initialized"
					token1_exchangeRate = 0
					token1_borrowAPR = 0
					token1_RF = 0
					token1_totalSupply = 0
					token1_totalBorrows = 0
					token1_supplyAPR = 0
					token1_utilization = 0
					token1_available = 0
					token1_balance = 0
					token1_imxB_rate = 0.0000000001

				if e == 1:
					sys.stdout.write(" " + str(i))
					output.at[i, "Factory"] = "V" + str(int(e))
					output.at[i, "Pair"] = str(token0_symbol) + "-" + str(token1_symbol)
					output.at[i, "Token0 User Balance"] = (token0_balance / token0_imxB_rate) * token0_exchangeRate
					output.at[i, "Token0 Supply APR"] = token0_supplyAPR
					output.at[i, "Token0 Borrow APR"] = token0_borrowAPR
					output.at[i, "Token0 Total Supply"] = (token0_totalSupply / 10**18 / token0_imxB_rate) * token0_exchangeRate
					
					output.at[i, "Token1 User Balance"] = (token1_balance / token1_imxB_rate) *token1_exchangeRate
					output.at[i, "Token1 Supply APR"] = token1_supplyAPR
					output.at[i, "Token1 Borrow APR"] = token1_borrowAPR
					output.at[i, "Token1 Total Supply"] = (token1_totalSupply / 10**18 / token1_imxB_rate) * token1_exchangeRate
					
					output.at[i, "Token0 imxB Address"] = token0_imxB_address
					output.at[i, "Token1 imxB Address"] = token1_imxB_address
			
				if e > 1: 
					counter = i + len(output)
					sys.stdout.write(" " + str(counter))
					output.at[counter, "Factory"] = "V" + str(int(e))
					output.at[counter, "Pair"] = str(token0_symbol) + "-" + str(token1_symbol)
					
					output.at[counter, "Token0 User Balance"] = (token0_balance / token0_imxB_rate) * token0_exchangeRate 
					output.at[counter, "Token0 Supply APR"] = token0_supplyAPR
					output.at[counter, "Token0 Borrow APR"] = token0_borrowAPR
					output.at[counter, "Token0 Total Supply"] = (token0_totalSupply / 10**18 / token0_imxB_rate) * token0_exchangeRate 

					output.at[counter, "Token1 User Balance"] = (token1_balance / token1_imxB_rate) * token1_exchangeRate
					output.at[counter, "Token1 Supply APR"] = token1_supplyAPR
					output.at[counter, "Token1 Borrow APR"] = token1_borrowAPR
					output.at[counter, "Token1 Total Supply"] = (token1_totalSupply / 10**18 / token1_imxB_rate) * token1_exchangeRate
			
					output.at[counter, "Token0 imxB Address"] = token0_imxB_address
					output.at[counter, "Token1 imxB Address"] = token1_imxB_address


				sys.stdout.flush()


	else:
		for e in range(1, ((len(chains[chain][1:]))+1)):
			sys.stdout.write(" Current Position: ")
			web3 = Web3(Web3.HTTPProvider(chains[chain][0]))
			Impermax_Factory_Address = chains[chain][e]
			Impermax_Factory_Contract = web3.eth.contract(address=Impermax_Factory_Address, abi=Impermax_Factory_ABI)
			Lending_Pool_Length = Impermax_Factory_Contract.functions.allLendingPoolsLength().call({"from": recipient}) - 1
		
			for i in range(0, Lending_Pool_Length):
				LP_Address = Impermax_Factory_Contract.functions.allLendingPools(i).call({"from": recipient})
				LP_Contract = web3.eth.contract(address=LP_Address, abi=LP_Token_ABI)
				getLendingPool = Impermax_Factory_Contract.functions.getLendingPool(LP_Address).call({"from": recipient})
				initialized = getLendingPool[0]

				if initialized == True:

					token0_imxB_address = Web3.toChecksumAddress(getLendingPool[3])
					token0_imxB_contract = web3.eth.contract(address=token0_imxB_address, abi=imxB_abi)
					token0_totalSupply = token0_imxB_contract.functions.totalSupply().call()
					token0_underlying_decimals = web3.eth.contract(address=token0_imxB_contract.functions.underlying().call(), abi=erc_abi).functions.decimals().call()
					token0_totalBalance = token0_imxB_contract.functions.totalBalance().call() / 10**token0_underlying_decimals
				
					if token0_totalSupply <= 0:
						token0_borrowAPR = 0
						token0_RF = 0
						token0_totalBorrows = 0
						token0_borrowAPR = 0
						token0_supplyAPR = 0
						token0_utilization = 0
						token0_available = token0_totalSupply
						token0_balance = 0
						token0_exchangeRate = 0
						token0_symbol = "No Supply"

					else:
						token0_address = Web3.toChecksumAddress(LP_Contract.functions.token0.__call__().call())
						token0_contract = web3.eth.contract(address=token0_address, abi=erc_abi)
						token0_symbol = token0_contract.functions.symbol.__call__().call()
						
						token0_borrowAPR = token0_imxB_contract.functions.borrowRate().call() * 365 * 24 * 60 * 60 / 10**18
						token0_exchangeRate = token0_imxB_contract.functions.exchangeRateLast().call() / 10**18
						token0_RF = token0_imxB_contract.functions.reserveFactor().call()
						token0_totalSupply = token0_imxB_contract.functions.totalSupply().call()
						token0_totalBorrows = token0_imxB_contract.functions.totalBorrows().call()
						token0_supplyAPR = token0_borrowAPR * (1 - token0_RF / 10**18) * token0_totalBorrows / (token0_totalSupply * token0_exchangeRate)
						token0_balance = token0_imxB_contract.functions.balanceOf(recipient).call() / 10**18
					
						token0_utilization = token0_totalBorrows / (token0_totalSupply * token0_exchangeRate)
						token0_available = ((token0_totalSupply * token0_exchangeRate) - token0_totalBorrows) / 10**18
						token0_imxB_rate =  token0_available / token0_totalBalance
			

					token1_imxB_address = Web3.toChecksumAddress(getLendingPool[4])
					token1_imxB_contract = web3.eth.contract(address=token1_imxB_address, abi=imxB_abi)
					token1_totalSupply = token1_imxB_contract.functions.totalSupply().call()
					token1_underlying_decimals = web3.eth.contract(address=token1_imxB_contract.functions.underlying().call(), abi=erc_abi).functions.decimals().call()
					token1_totalBalance = token1_imxB_contract.functions.totalBalance().call() / 10**token1_underlying_decimals
					

					if token1_totalSupply <= 0:
						token1_borrowAPR = 0
						token1_RF = 0
						token1_totalBorrows = 0
						token1_borrowAPR = 0
						token1_supplyAPR = 0
						token1_utilization = 0
						token1_available = token0_totalSupply
						token1_balance = 0
						token1_exchangeRate = 0
						token1_symbol = "No Supply"

					else:
						token1_address = Web3.toChecksumAddress(LP_Contract.functions.token1.__call__().call())
						token1_contract = web3.eth.contract(address=token1_address, abi=erc_abi)
						token1_symbol = token1_contract.functions.symbol.__call__().call()

						token1_borrowAPR = token1_imxB_contract.functions.borrowRate().call() * 365 * 24 * 60 * 60 / 10**18
						token1_exchangeRate = token0_imxB_contract.functions.exchangeRateLast().call() / 10**18
						token1_RF = token1_imxB_contract.functions.reserveFactor().call()
						token1_totalSupply = token1_imxB_contract.functions.totalSupply().call()
						token1_totalBorrows = token1_imxB_contract.functions.totalBorrows().call()
						token1_supplyAPR = token1_borrowAPR * (1 - token1_RF / 10**18) * token1_totalBorrows / (token1_totalSupply * token1_exchangeRate)
						token1_utilization = token1_imxB_contract.functions.totalBorrows().__call__().call() / (token1_imxB_contract.functions.totalSupply().call({"from": recipient}) * token1_exchangeRate)
						token1_available = ((token1_totalSupply * token1_exchangeRate) - token1_totalBorrows) / 10**18
						token1_imxB_rate = token1_available / token1_totalBalance
						token1_balance = token1_imxB_contract.functions.balanceOf(recipient).call() / 10**18

			
				else: # catch non-initialized pairs
					token0_address = "Not Initialized"
					token0_contract = "Not Initialized"
					token0_symbol = "Not Initialized"
					token0_imxB_address = "Not Initialized"
					token0_imxB_contract = "Not Initialized"
					token0_exchangeRate = 0
					token0_borrowAPR = 0
					token0_RF = 0
					token0_totalSupply = 0
					token0_totalBorrows = 0
					token0_supplyAPR = 0
					token0_utilization = 0
					token0_available = 0
					token0_balance = 0
					token0_imxB_rate = 0.0000000001

					token1_address = "Not Initialized"
					token1_contract = "Not Initialized"
					token1_symbol = "Not Initialized"
					token1_imxB_address = "Not Initialized"
					token1_imxB_contract = "Not Initialized"
					token1_exchangeRate = 0
					token1_borrowAPR = 0
					token1_RF = 0
					token1_totalSupply = 0
					token1_totalBorrows = 0
					token1_supplyAPR = 0
					token1_utilization = 0
					token1_available = 0
					token1_balance = 0
					token1_imxB_rate = 0.0000000001

				if e == 1:
					sys.stdout.write(" " + str(i))
					output.at[i, "Factory"] = "V" + str(int(e))
					output.at[i, "Pair"] = str(token0_symbol) + "-" + str(token1_symbol)
					output.at[i, "Token0 User Balance"] = (token0_balance / token0_imxB_rate) * token0_exchangeRate
					output.at[i, "Token0 Supply APR"] = token0_supplyAPR
					output.at[i, "Token0 Borrow APR"] = token0_borrowAPR
					output.at[i, "Token0 Total Supply"] = (token0_totalSupply / 10**18 / token0_imxB_rate) * token0_exchangeRate
				
					output.at[i, "Token1 User Balance"] = (token1_balance / token1_imxB_rate) *token1_exchangeRate
					output.at[i, "Token1 Supply APR"] = token1_supplyAPR
					output.at[i, "Token1 Borrow APR"] = token1_borrowAPR
					output.at[i, "Token1 Total Supply"] = (token1_totalSupply / 10**18 / token1_imxB_rate) * token1_exchangeRate
					
					output.at[i, "Token0 imxB Address"] = token0_imxB_address
					output.at[i, "Token1 imxB Address"] = token1_imxB_address
			
				if e > 1: 
					counter = i + len(output)
					sys.stdout.write(" " + str(counter))
					output.at[counter, "Factory"] = "V" + str(int(e))
					output.at[counter, "Pair"] = str(token0_symbol) + "-" + str(token1_symbol)
					
					output.at[counter, "Token0 User Balance"] = (token0_balance / token0_imxB_rate) * token0_exchangeRate 
					output.at[counter, "Token0 Supply APR"] = token0_supplyAPR
					output.at[counter, "Token0 Borrow APR"] = token0_borrowAPR
					output.at[counter, "Token0 Total Supply"] = (token0_totalSupply / 10**18 / token0_imxB_rate) * token0_exchangeRate 

					output.at[counter, "Token1 User Balance"] = (token1_balance / token1_imxB_rate) * token1_exchangeRate
					output.at[counter, "Token1 Supply APR"] = token1_supplyAPR
					output.at[counter, "Token1 Borrow APR"] = token1_borrowAPR
					output.at[counter, "Token1 Total Supply"] = (token1_totalSupply / 10**18 / token1_imxB_rate) * token1_exchangeRate
				
					output.at[counter, "Token0 imxB Address"] = token0_imxB_address
					output.at[counter, "Token1 imxB Address"] = token1_imxB_address


			sys.stdout.flush()

	return output

print(" Runtime: " + str(time.time() - start_time))
