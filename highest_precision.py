def highest_precision(a_list_of_numbers):
    # takes in list of numbers and returns the largest number of decimal spaces present in the list
    import decimal
    try:
        longest_decimal = 0
        for val in a_list_of_numbers:
            num_decimals = abs(decimal.Decimal(str(val)).as_tuple().exponent)
            if num_decimals > longest_decimal:
                longest_decimal = num_decimals
        return longest_decimal
    
    except TypeError: 
        return(abs(decimal.Decimal(str(a_list_of_numbers)).as_tuple().exponent))
    except:
        print('Invalid argument type.')
