# -*- coding: uft-8 -*-

class Ticket:

    models_and_amount = []
    ticketNum = ""

    def __init__(self,customer):
        self.customer = customer

    def generateTicketNumber(self):
        # do something to get the ticket number after the last one
        self.ticketNum = "generated number"

    def changeTicketNumber(self,ticket_num):
        # leave out a way to write the number manually in case theres issue following the last ticket number
        self.ticketNum = ticket_num

    def addModels(self,models,amount):
        self.models_and_amount.append([models,amount])

    def modelPrice(self,model):
        #get the dataframe of the price spreadsheet, locate price value with row-model and column-customer
        price = ""
        return price

    def eachModelttlPrice(self,model_amount): # [model, amount]
        model = model_amount[0]
        amount = model_amount[1]
        model_ttl_price = float(self.modelPrice(model)) * amount
        return float(model_ttl_price)

    def totalPrice(self): # ttl price and each model's ttl price
        ttl_price = 0
        for each_model_and_amount in self.models_and_amount:
            model_ttl_price = self.eachModelttlPrice(each_model_and_amount)
            ttl_price += float(model_ttl_price)
        return ttl_price

    def savingdata(self):
        # [[customer,ticket,model,price,amount,model_ttl_price],...]
        # maybe delete them or certain data that we no longer want?
        pass

class ReplenishStock:

    replenished_models = []
    ticket_num = ""

    def __init__(self,date):
        self.date = date

    def ticketNum(self,ticket_number):
        self.ticket_num = ticket_number

    def replenish(self,model,amount):
        self.replenished_models.append([model,amount])

    def cost(self): # maybe each model ttl cost due to the excel format
        # we have each model original price on the spreadsheet, we can take that, to get ttl cost
        ttl_cost = ""
        return ttl_cost

    def saveData(self):
        # save the data to the replenishment stock spreadsheet (this is new)
        pass


class Stock:

    def __init__(self):
        # get the dataframe of replenshish and sold models
        self.df_replenished = ""
        self.df_sold = ""
        pass

    def ttlReplenished(self):
        # use .groupby? models to get each model's replenished amount
        pass

    def ttlSold(self):
        # use .groupby? models to get each model's sold amount
        pass

    def updateStock(self):
        # figure this out
        pass

