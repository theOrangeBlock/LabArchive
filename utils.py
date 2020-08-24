


def numberToExcelCol(number):
    '''
    so this is to convert any number to the excel alphanumberical
    column format
    0 -> A
    26 -> AA
    28 -> AC
    '''

    colName = ''
    while number > 25:
        
