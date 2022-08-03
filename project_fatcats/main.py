import api, coh, overhead, profit_loss

def main():
    forex = api.api_function()
    overhead.overhead_function(forex)
    coh.coh_function(forex)
    profit_loss.profitloss_function(forex)

main()
