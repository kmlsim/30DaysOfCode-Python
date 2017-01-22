import sys

class Solution:
    # Write your code here
    def __init__(self):
        self.my_stack = []
        self.my_queue = []

    def pushCharacter(self, ch):
        self.ch = ch
        self.my_stack.append(self.ch)

    def enqueueCharacter(self, ch):
        self.ch = ch
        self.my_queue.append(self.ch)

    def popCharacter(self):
        return self.my_stack.pop(-1)

    def dequeueCharacter(self):
        return self.my_queue.pop(0)

# read the string s
s=raw_input()
#Create the Solution class object
obj=Solution()

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l / 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    sys.stdout.write ("The word, "+s+", is a palindrome.")
else:
    sys.stdout.write ("The word, "+s+", is not a palindrome.")
