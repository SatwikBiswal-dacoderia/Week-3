L=eval(input("Enter a List : "))
if L[0:-1]==L[-1:0:-1]:
    print("The List provided, is a pallindrome.")
else:
    print("The List provided is not a palindrome.")
