


def numberToExcelCol(number):
    '''
    so this is to convert any number to the excel alphanumberical
    column format
    0 -> A
    26 -> AA
    28 -> AC
    '''
#I dont think this works for numbers larger than 51
    colName = ''
    while number > 25:
        colName += char((number % 25) + 65)

