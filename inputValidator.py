#!/usr/bin/env python3.7


def cmdValidator(arg_list):
    """
    Validates if list arg_list from module tgBot1 contains a valid query string
    Invalid strings reset the variables valid_product_list and valid_product to zero length and return a zero-length list and string, respectively.

    Valid strings:
        Only alpha-numeric characters example: eggs bacon

    Invalid Strings:
        eg1s b@con m*lk
    """

    error_status = 'valid'
    valid_product_list = []
    valid_product = ''

    if (len(arg_list) < 1):
        #print(f'User Supplied no arguments after /getprice command')
        error_status = 'empty'
        valid_product_list = []
        valid_product = ''
        #Call sender function here prompt user for non-empty query
    else:
        for item in arg_list:
            if not item.isalpha():
                #print(f'User supplied item {item} contains non-alphanumeric characters')
                error_status = 'nonalpha'
                valid_product_list = []
                valid_product = ''
                #Call sender function here prompt user for alphanumeric query
                break

            valid_product_list.append(item)
            valid_product = ' '.join(item for item in valid_product_list)

    #print(len(valid_product_list))
    #print(len(valid_product))
    #print(error_status)
    return valid_product, error_status


if __name__ == '__main__':
    cmdValidator(text)
