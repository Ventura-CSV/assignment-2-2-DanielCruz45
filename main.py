def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celcius fahrenheit 
    ##################################################
    """
    #input value, askes user for some degrees cekcius. added text to clarify what to input.
    celcius = int(input('Degrees Celcius: '))

    #translates celcius to fahrenheit using the related equation
    fahrenheit= (9 / 5) * celcius + 32

    #outputs the calcualted fahrenheit in the desired format
    print(f'Farenheit: \t {fahrenheit:.2f}')
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celcius, fahrenheit


if __name__ == '__main__':
    main()
