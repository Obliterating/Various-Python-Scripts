def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])
def marginandprofit (principal, buy, sell, name):
    itemcount = float(truncate(float(principal/buy), 0))
    realprincipal = itemcount * buy
    revenue = itemcount * sell
    baseprofit = revenue-realprincipal
    basemargin = baseprofit/realprincipal
    print ('''If you buy %s items ('%s') at a price of %s, and sell them for %s, then you will make a pre-tax profit of %s, with a margin of %s''' % (itemcount, name, buy, sell, baseprofit, basemargin))
print("def marginandprofit (principal, buy, sell, name):")

while (3 > 1):
    principal = float(input("Principal: "))
    buy = float(input("Buy: "))
    sell = float(input("Sell: "))
    name = input("Name: ")
    marginandprofit (principal, buy, sell, name)
    
