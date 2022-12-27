import random

bet_limit = 100

rows = 3
cols = 3
symbols_count = {'A': 3 ,'B': 6 , 'C': 9 , 'D': 12}
symbols_value = {'A': 4 ,'B': 3 , 'C': 2 , 'D': 1}

def spin_the_slot(rows,cols,symbols_count):
    all_symbols = []
    for symbol,symbol_count in symbols_count.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            pick = random.choice(current_symbols)
            current_symbols.remove(pick)
            column.append(pick)
        columns.append(column)  
    return columns

def slot_machine(columns):
    for i in range(len(columns[0])):  
        for idx,colum in enumerate(columns):
            if idx != cols - 1:
                print(colum[i], end = ' | ')
            else:
                print(colum[i], end = ' ')  
        print()

def bet():
    while True:
        bet_amt = int(input('Enter ur bet Amount: $'))
        if 1 <= bet_amt <= bet_limit: break
        else: print("Ur bet can't exceed the bet limit. !?") 
    return bet_amt  

def line_bet():
    while True:
        lines = int(input('Enter the number of lines u are gonna bet on: ')) 
        if 1 <= lines <= cols: break
        else: print('Enter a appropriate number of lines: ')
    return lines

def checking_for_wins(lines,columns,bet_amt,total_bet):
    winnings = 0
    for i in range(lines):
        a = columns[0][i]
        for colum in columns:
            if colum[i] != a: break
        else:
            winnings += symbols_value[a] * bet_amt
            print(f'U hv won on the line {i+1}')
        
    return winnings - total_bet        




def beting(balance):
    while True:
        bet_amt = bet()
        lines = line_bet()
        total_bet = lines * bet_amt
        if total_bet <= balance : break
        else : print('Ur total bet exceeds ur balance: ')
    return bet_amt,lines,total_bet    

    

def game(): 
    print('*'*30)
    balance = int(input('Enter ur deposits: $')) 
    print('*'*30)  
    while True:
        print()
        n = input('Press Enter to continue or q to quit: ')
        print()
        if n == 'q': 
            print(f'Ur take out is {balance}')
            break
        else:
            bet_amt,lines,total_bet = beting(balance)
            columns = spin_the_slot(rows,cols,symbols_count)
            print()
            slot_machine(columns)
            print()
            answer = checking_for_wins(lines,columns,bet_amt,total_bet)
            print()
            balance += answer
            print(f'Ur current balance is {balance}')


game()
