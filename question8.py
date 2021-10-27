#Program to sum up 5 numbers and
#find the average of the numbers.

def main():

    sum=0

    for i in range(5):

        number=float(input("Enter number: "))

        sum=sum+number

        average= sum/5

    print("The average is: ",average)

main()

