def table_1(interest, year, money):
    '''
    return calculate future value one pack
    '''
    money = int(money)
    n = int(year)
    k = (float(interest))/100
    values = ((1+k)**n)*money
    return '%.2f'%values

def table_2(interest, year, money):
    '''
    return calculate future value muti pack
    '''
    money = int(money)
    n = int(year)
    k = (float(interest))/100
    values = ((((1+k)**n)-1)/k)*money
    return '%.2f'%values

def table_3(interest, year, money):
    '''
    return calculate present value one pack
    '''
    money = int(money)
    n = int(year)
    k = (float(interest))/100
    values = (1/((1+k)**n))*money
    return '%.2f'%values

def table_4(interest, year, money):
    '''
    return calculate present value muti pack
    '''
    money = int(money)
    n = int(year)
    k = (float(interest))/100
    values = ((1-(1/((1+k)**n)))/k)*money
    return '%.2f'%values

