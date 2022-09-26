


# Function to demonstrate printing pattern triangle
def triangle(n):

    # number of spaces
    k = n - 1

    # outer loop to handle number of rows
    for i in range(0, n-1):

        # inner loop to handle number spaces
        # values changing acc. to requirement
        for j in range(0, k):
            print(end=" ")

        # decrementing k after each loop
        k = k - 1

        # inner loop to handle number of columns
        # values changing acc. to outer loop
        print("/",end='')
        for j in range(0, 2*i):

            # printing stars
            print(" ", end="")
        print("\\")
    print('/'+(2*n-2)*'_'+'\\')
# Driver Code
n = 5
triangle(n)
