blockchain = [[1]];


def get_last_blockchain_value(): 
  if len(blockchain) < 1:
    return None
  return blockchain[-1]


def add_transaction_value(transaction_amount, last_transaction = [1]): 

  if last_transaction == None:
    last_transaction = [1];
  blockchain.append([blockchain[-1], transaction_amount])


def get_transaction_value(): 
  return float(input('Your transaction amount please:' ))


def get_user_choice(): 
  user_input = input('Your Choice: ')
  return user_input


def print_blockchain_elements():
  for block in blockchain: 
    print('outputting block')
    print(block)

while True: 

  print('Please choose ')
  print('1: Add a new transaction value')
  print('2: Output the blockchain blocks')
  print('q: Quit')

  user_choice = get_user_choice()

  if user_choice == '1': 
    tx_amount = get_transaction_value()
    add_transaction_value(tx_amount, get_last_blockchain_value())
  elif user_choice == '2':
    print_blockchain_elements()
  elif user_choice == 'q':
    break;
  else:
    print('Invalid input, pick a value from the list')

print('Done!')
  
# print(blockchain)
# print(get_last_blockchain_value())