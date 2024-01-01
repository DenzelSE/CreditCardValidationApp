#---creating a Credit Card Validation App using Lunn's Algorithm---#

def user_input_card_no(): 
    '''This function prompts the user to enter card numbe,
        the card number must be of 16 characters'''
    
    card_no = input("Enter a card number: ")
    while True:
        if len(card_no) != 16:
            card_no = input("Enter a valid card number: ")
        else:
            return card_no
        
def credit_card_validation(card_no):
    '''This function takes card_no as a parameter,
        the function applies the Lhun's algorithm to check card validation
        '''
    list_card_no = list(card_no)
    list_odd_idx = []
    list_even_idx_doubles = []
    
    for idx,val in enumerate(list_card_no):
        if int(idx) % 2 != 0: #the condition for odd indexes that are used to append their values to the odd list
            list_odd_idx.append(int(val))
        if int(idx) % 2 == 0: #the conditino for even indexes that are used to append thier values to even list
            list_even_idx_doubles.append(int(val)*2) 
    sum_even_idx = sum(list_odd_idx)
    sum_of_single_odds_idx = [] # list to sum up the values of even indexes single digits

    for idx,val in enumerate(list_even_idx_doubles):
        '''this loop checks if the values of the even index are double digits, 
            then splits them and add the two together to make a single digit to append to the list of single_digits'''
        if len(str(val)) == 2:
            double_digits = list(str(val))
            sum_of_doubles_digits = int(double_digits[0]) + int(double_digits[1])
            sum_of_single_odds_idx.append(sum_of_doubles_digits)
        else:
            sum_of_single_odds_idx.append(int(val))
    sum_of_odd_idx =sum(sum_of_single_odds_idx)

    #Adding the total sums of both even and odd indexes lists
    sum_of_card_no = sum_even_idx + sum_of_odd_idx
    
    while True:
        if sum_of_card_no % 10 == 0:
            return "Credit Card is valid!, \nValidation: Successful"
        else:
            return "Credit Card is NOT valid! \nValidation: Unsuccessful"
            
def CCV():
    '''this function serves as a construstor that ensures proper control flow
        it utilizze the functions created above'''
    
    card_no = user_input_card_no()
    validation = credit_card_validation(card_no)
    print(validation)

CCV()