from datetime import datetime
# define an empty list
items = []
prices = []
cart = []

def extactDataFromFile():
    # open file and read the content in a list
    with open('list.txt', 'r') as filehandle:
        for line in filehandle:
            # remove linebreak which is the last character of the string
            currentItem = line[:-1]
            tmp = currentItem.split("-")

            # add item to the list
            items.append(tmp[0])
            prices.append(tmp[1])

    #print(items)
    #print(prices)

def printWelcomeScreen():
    print("Welcome to our supermarket\n")
    print('Enter your name:')
    x = input()
    print('Hello, ' + x)

def printItemsList():
    for i in range(len(items)):
        print(i + 1 , " - " , items[i] , " Price: ", prices[i])

def showCustomerOptions():
    flag = True

    while flag:
        print("Write the item number to purchase - 0 if you are Done")
        try:
            x = int(input())
            while x > len(items) or x < 0:
                print("Write the item number to purchase - 0 if you are Done")
                x = input()
        except ValueError:
            print("Write the item number to purchase - 0 if you are Done")
        if (x == 0):
            flag = False
            break
        else:
            cart.append(int(x) - 1)

def printCart():
    sum = 0
    for i in range(len(cart)):
        x = cart[i]
        price = prices[x]
        sum += int(price)
        print(items[x] , '- Price: ',price)
    print("Total price:",sum)

def displayOptions():
    print("Please choose:")
    print("1 - Rate the supermarket out of 5")
    print("2 - Exit")
    x = int(input())

    if x == 1:
        print("Enter rating 0-5:")
        rating = int(input())
    elif x == 2:
        print("Good bye")


    with open('review.txt', 'a+') as filehandle:
        filehandle.write('rating - %s\n' % rating)

def savePurchaseHistory():
    with open('listpurchase.txt', 'a+') as filehandle:
        today = datetime.now()
        filehandle.write('%s\n' % today)
        for listitem in cart:
            x = items[listitem]
            filehandle.write('%s\n' % x)

def clients_feedback():
    sum = 0
    count = 0
    # open file and read the content in a list
    with open('review.txt', 'r') as filehandle:
        for line in filehandle:
            # remove linebreak which is the last character of the string
            currentItem = line[:-1]
            tmp = currentItem.split("-")
            sum += int(tmp[1])
            count += 1
    print("Total rating:" , sum / count)


def main():
    printWelcomeScreen()
    extactDataFromFile()
    printItemsList()
    showCustomerOptions()
    printCart()
    savePurchaseHistory()
    displayOptions()
    clients_feedback()



if __name__ == "__main__":
    main()