import queue

liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}

iniState=({'path':'tokenB','token':'tokenB','tokenA':0,'tokenB':5,'tokenC':0,'tokenD':0,'tokenE':0,'liquidity':liquidity});
maxToken=5
q=queue.Queue()
q.put(iniState)
def swapToken(amountIn,inToken,outToken,liquidity):
    if inToken<outToken:
        if not( (inToken,outToken) in  liquidity):
            return 0,liquidity
        getPool=liquidity[(inToken,outToken)]
        reversedIn=getPool[0]
        reversedOut=getPool[1]
        amountOut=997*amountIn*reversedOut/(1000*reversedIn+997*amountIn)
        del liquidity[(inToken,outToken)]
    else:
        if not( (outToken,inToken) in  liquidity):
            return 0,liquidity
        getPool=liquidity[(outToken,inToken)]
        reversedIn=getPool[1]
        reversedOut=getPool[0]
        amountOut=997*amountIn*reversedOut/(1000*reversedIn+997*amountIn)
        del liquidity[(outToken,inToken)]
    
    return amountOut,liquidity
    
while(not q.empty()):
    current=q.get()
    for outToken in ('tokenA','tokenB','tokenC','tokenD','tokenE'):
        inToken=current['token']
        if(inToken != outToken):
            amountOut,liquidity=swapToken(current[inToken],inToken,outToken,current['liquidity'].copy())
            if(amountOut>current[outToken]):
                outState=current.copy()
                outState['path']=current['path']+'->'+outToken
                outState['token']=outToken
                outState[outToken]=amountOut;
                outState['liquidity']=liquidity
                q.put(outState)
                if(outToken=='tokenB' and amountOut>maxToken):
                    maxPath=outState['path']
                    maxToken=amountOut
    
print(f"path: {maxPath}, tokenB balance={maxToken}")
