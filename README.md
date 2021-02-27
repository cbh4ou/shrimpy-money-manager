# Shrimpy Money Manager

  This self-hosted tool will allow you to manual program your take-profit for future Dollar-Cost-Averaging (DCA) or take home profit. It does this in increments or whole amounts by your settings in precise positive deviations of your average portfolio balance.

  By connecting your KuCoin or Binance subaccount APIs you will be able to control how your money is handled between shrimpy leaders.

  You first need to setup each leader or personal portfolio on a seperate api. 
  After this, you will set the starting balance and the allocation you would like each portfolio to have in a global setting.

# Ex. You are following "Gathering" on KuCoin and his currently 19 portfolios - Using 10% DCA take profit and 5% take-home profit on every 20% increase in the index
  He requires 50% funds spread out into the BTC/ETH. 50% set into 18 other altcoin portfolios.
  In this example, with $3600, you would do $100 in each of the 18, with $1188 in BTC and $612 in ETH if using a 66:34 ratio.
  In the tool, you would join all these portfolios into a "portfolio" or "index" set the allocations for each portfolios inputting the starting balance for each one.
  
  Bringing take profit into the example now:
    Using 10% DCA take profit and 5% take-home profit on every 20% increase in the index
     If you started with $3600, and you did a 20% increase that would be $720.
     10% or $72 will go into DCA subaccount and $36 into take home. 
     
  Rebalancing or Money Management:
     Now the software knows which portfolios are below the average by tracking current balance associated with allocation. Lets assume one portfolio sold $5 (not to be confused  
     with DCA or take home profit) of its profit after a rebalance to fill a losing portfolio below the portolio average. The system will store this as -$5 the take profit and +$5 
     for the losing portfolio. So when it is time to rebalance and take profit again, the system to optimize the distribituion of funds to the best of its ability. Best case
     the $5 of the $72 DCA profit fills into the portfolio who just transferred 5 into another portfolio once he hit a 20% increase in our portfolio and the rest will go into the
     least performing portfolios. This is where the magic happens
     
     
  Rebalancing during an overall down trend (Negative deviation of all accounts compared to the previous rebalance average)
    
    
  
