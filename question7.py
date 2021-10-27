#Program to sum up 5 numbers.

def main():

    sum=0

    for i in range(5):

        number=int(input("Enter number: "))

        sum=sum+number

    print("The sum is: ",sum)

main()
