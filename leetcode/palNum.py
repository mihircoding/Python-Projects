from hashlib import new


def isPalindrome(x):
    if x < 0:
        return False
    if str(x) == str(x)[::-1]:
        return True
print(isPalindrome(121))