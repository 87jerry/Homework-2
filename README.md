# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> the most profitable path: tokenB->tokenA->tokenC->tokenE->tokenD->tokenC->tokenB
> 5-> 5.655321988655322-> 2.372138936383089-> 1.5301371369636168-> 3.450741448619708-> 6.684525579572586-> 22.49722180697414

## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> Price Slippage is the change in token price caused by the total movement of the market. Price Slippage is shown as the difference between the price you expect to receive after swapping vs what you actually receive after the swap is complete. In the swapExactTokensForTokens function, the user can set amountOutMin and revert the entire process if the actual price obtained is lower than expected.

## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> to defend against Inflation Attacks

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> Keep the ratio of the two tokens in the pool the same. Even if users deposit different proportions of tokens, they can only get a smaller proportion of liquidity tokens.

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> A sandwich attack is a form of front-running. The attacker places one order right before the trade and one right after it, effectively sandwiching the original pending transaction. The purpose of these two orders is to manipulate asset prices. The attacker buys the asset the user is swapping to, knowing that this will increase the price of the asset. Then, the attacker lets the victim buy at this higher value. Finally, the attacker sells the asset at this higher price. This sequence causes the price of the asset to increase, allowing the attacker to make a profit.
