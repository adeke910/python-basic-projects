#Create a company name and informaton
company_name = "Daey's Food Mart"
company_address = '144 Kigali Street.'
company_city = 'Ajah, Lagos'

#Declare ending message
message = 'Thanks for shopping with us today!'

# Declare variables as the name of products and their price
prod1_name, prod1_price = 'Books', 50.95
prod2_name, prod2_price = 'Computer', 598.99
prod3_name, prod3_price = 'Monitor', 156.89

#create a top border
print('*' * 50)


#print company information first using format
#\t is to create tab spaces...\n to send to new lines
print('\n\t\t\t{}\n\t\t\t{}\n\t\t\t{}'.format(company_name,company_address
                                            ,company_city))

#print a line between sections
print('-'*50)

#print out heder for section of items
print('\tProduct Name\tProduct Price')

#create a print statement for each item
print('\t\t{}\t\t${}'.format(prod1_name, prod1_price))
print('\t\t{}\t${}'.format(prod2_name, prod2_price))
print('\t\t{}\t\t${}'.format(prod3_name, prod3_price))

#print a line between sections
print('-'*50)

#calculate total price and print and print header for section of total
total= prod1_price + prod2_price +prod3_price
print('\t\tTotal\t\t${}'.format(total))

#print a line between sections
print('-'*50)

print('\t{}\n'.format(message))

#create a bottom border
print('*' * 50)