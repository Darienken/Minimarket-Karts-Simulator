customers_li=[]
box1_li=[]
box2_li=[]
box3_li=[]
box1_counter=0
box2_counter=0
box3_counter=0

#Func to append costumers to boxes
def append_costumer():
    global customers_li
    global box1_counter
    global box2_counter
    global box3_counter
    global box1_li
    global box2_li
    global box3_li
    #Box 1 counter
    box1_counter=0
    for i in box1_li:
        box1_counter+=1

    #Box 2 counter
    box2_counter=0
    for i in box2_li:
        box2_counter+=1

    #Box 3 counter
    box3_counter=0
    for i in box3_li:
        box3_counter+=1

    #Go over customers
    for customer in customers_li:
        #Evaluate if box 1 has less costumers
        if box1_counter <= box2_counter and box1_counter <= box3_counter:
            box1_li.append(customer)
            box1_counter+=1
            customers_li.pop(0)
            print(f"box 1: {box1_counter}")
            break
        #Evaluate if box 2 has less costumers
        elif box2_counter <= box1_counter and box2_counter <= box3_counter:
            box2_li.append(customer)
            box2_counter+=1
            customers_li.pop(0)
            print(f"box 2: {box2_counter}")
            break
        #Evaluate if box 3 has less costumers
        elif box3_counter <= box1_counter and box3_counter <= box2_counter:
            box3_li.append(customer)
            box3_counter+=1
            customers_li.pop(0)
            print(f"box 3: {box3_counter}")
            break
        #Else costumers go to box 1
        else:
            box1_li.append(customer)
            box1_counter+=1
            customers_li.pop(0)
            print(f"box 1 else: {box1_counter}")
            break
    return f"Customers: {box1_counter}", f"Customers: {box2_counter}", f"Customers: {box3_counter}"


def delete_customers():
    global box1_counter
    global box2_counter
    global box3_counter
    global box1_li
    global box2_li
    global box3_li
    total_costumers=box1_counter+box2_counter+box3_counter
    box1_counter=0
    box2_counter=0
    box3_counter=0
    del box1_li[:]
    del box2_li[:]
    del box3_li[:]
    return total_costumers,f"Customers: {box1_counter}", f"Customers: {box2_counter}", f"Customers: {box3_counter}"


box1_no_buy=[]
box2_no_buy=[]
box3_no_buy=[]
box1_counter_no_buy=0
box2_counter_no_buy=0
box3_counter_no_buy=0
def no_buyers():
    global customers_li
    global box1_no_buy
    global box2_no_buy
    global box3_no_buy
    global box1_counter_no_buy
    global box2_counter_no_buy
    global box3_counter_no_buy
    #Box 1 counter no buy
    box1_counter_no_buy=0
    for i in box1_no_buy:
        box1_counter_no_buy+=1

    #Box 2 counter no buy
    box2_counter_no_buy=0
    for i in box2_no_buy:
        box2_counter_no_buy+=1

    #Box 3 counter no buy
    box3_counter_no_buy=0
    for i in box3_no_buy:
        box3_counter_no_buy+=1

    #Go over customers no buy
    for customer in customers_li:
        #Evaluate if box 1 no buy has less costumers
        if box1_counter_no_buy <= box2_counter_no_buy and box1_counter_no_buy <= box3_counter_no_buy:
            box1_no_buy.append(customer)
            box1_counter_no_buy+=1
            customers_li.pop(0)
            print(box1_no_buy)
            break
        #Evaluate if box 2 no buy has less costumers
        elif box2_counter_no_buy <= box1_counter_no_buy and box2_counter_no_buy <= box3_counter_no_buy:
            box2_no_buy.append(customer)
            box2_counter_no_buy+=1
            customers_li.pop(0)
            print(box2_no_buy)
            break
        #Evaluate if box 3 no buy has less costumers
        elif box3_counter_no_buy <= box1_counter_no_buy and box3_counter_no_buy <= box2_counter_no_buy:
            box3_no_buy.append(customer)
            box3_counter_no_buy+=1
            customers_li.pop(0)
            print(box3_no_buy)
            break
        #Else costumers go to box 1 no buy
        else:
            box1_no_buy.append(customer)
            box1_counter_no_buy+=1
            customers_li.pop(0)
            print(box1_no_buy)
            break
    return f"Customers No buy: {box1_counter_no_buy}", f"Customers No buy: {box2_counter_no_buy}", f"Customers No buy: {box3_counter_no_buy}"


def retire():
    global box1_counter_no_buy
    global box2_counter_no_buy
    global box3_counter_no_buy
    global box1_no_buy
    global box2_no_buy
    global box3_no_buy
    box1_counter_no_buy=0
    box2_counter_no_buy=0
    box3_counter_no_buy=0
    del box1_no_buy[:]
    del box2_no_buy[:]
    del box3_no_buy[:]
    return f"Customers No Buy: {box1_counter_no_buy}", f"Customers No Buy: {box2_counter_no_buy}", f"Customers No Buy: {box3_counter_no_buy}"


        