"""
Problems to solve:
1) create the page outline and declare company name and information.
2) Declare the ending message
3) The user inputs the items bought(string) and prices, calculates the total price add taxes and prints ending message.
"""

#Create a company name and informaton
company_name = "Daey's Food Mart"
company_address = '144 Kigali Street.'
company_city = 'Ajah, Lagos'

#Declare ending message
message = 'Thanks for shopping with us today!'

#Declare the variables for creating the WHILE loop
TAX_RATE = 0.09
item_no = 0
item_name = " "
subtotal = 0.0
tax = 0.0
total = 0.0

#create a top border
print('*' * 50)


#print company information first using format
#\t is to create tab spaces...\n to send to new lines
print('\n\t\t\t{}\n\t\t\t{}\n\t\t\t{}'.format(company_name, company_address
                                            ,company_city))

#print a line between sections
print('-'*50)

#print out header for section of items
print('\t\t\t\t\t\tProduct Name\tProduct Price')

#While loop
while (1):
    prompt = input("Enter Item_name:")
    print('\t\t\t\t\t\t{}'.format(prompt.title()))
    if (prompt != 'p'):
        prompt2 = float(input("Enter price:"))
        print('\t\t\t\t\t\t\t\t\t\t${}'.format(prompt2))
        subtotal += prompt2
        continue
    elif (prompt == 'p'):
        break

# print a line between sections
print('-' * 50)

#print the total
tax = subtotal * TAX_RATE
total = subtotal + tax
print("\t\t\t\t\t\tSUBTOTAL: \t\t${}".format(subtotal))
print("\t\t\t\t\t\tTAX: \t\t\t${}".format(tax))
print("\t\t\t\t\t\tTOTAL: \t\t\t${}".format(total))

# print a line between sections
print('-' * 50)

print('\t{}\n'.format(message))

# create a bottom border
print('*' * 50)