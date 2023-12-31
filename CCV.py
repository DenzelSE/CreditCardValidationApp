#creating a creditcard validation app  using Lunn's Algorithm

def user_input_card_no():    
    card_no = input("Enter a card number: ")
    while True:
        if len(card_no) != 16:
            card_no = input("Enter a valid card number: ")
        else:
            return card_no
        
def credit_card_validation(card_no):
    list_card_no = list(card_no)
    list_even_idx = []
    list_odd_idx_doubles = []
    print(list_card_no)
    for idx in enumerate(list_card_no):
        if int(idx) % 2 != 0:
            list_even_idx.append(int(list_card_no[int(idx)]))
        if int(idx) % 2 == 0:
            list_odd_idx_doubles.append(int(list_card_no[int(idx)])*2)
    print(list_even_idx)
    print(list_odd_idx_doubles)
    sum_even_idx = sum(list_even_idx)
    print(sum_even_idx)

    sum_of_single_odds_idx = []
    for idx,val in enumerate(list_odd_idx_doubles):
        if len(str(val)) == 2:
            double_digits = list(str(val))
            print(double_digits)
            sum_of_doubles = int(double_digits[0]) + int(double_digits[1])
            print(sum_of_doubles)
            sum_of_single_odds_idx.append(sum_of_doubles)
        else:
            sum_of_single_odds_idx.append(int(val))

    sum_of_odd_idx =sum(sum_of_single_odds_idx)
    print(sum_of_odd_idx)
    sum_of_card_no = sum_even_idx + sum_of_odd_idx
    print(sum_of_card_no)
    while True:
        if sum_of_card_no % 10 == 0:
            return "Credit Card is valid, \nValidation: successful"
        else:
            return "Credit Card is NOT valid! \nValidation: unsuccessfl"
            
def CCV():
    card_no = user_input_card_no()
    validation = credit_card_validation(card_no)
    print(validation)

CCV()