#WAP to check a list contain palindrome or not

list = [1, 2, 1]

copyList = list.copy()
copyList.reverse()


if(copyList == list): print("List is palindrome",list)

else: print("List is not palindrome",list)
