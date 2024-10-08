# You will be given an array a and a value x. All you need to do is
# check whether the provided array contains the value.

# Array can contain numbers or strings. X can be either.

# Return true if the array contains the value, false if not.

def check(seq, elem):
    return True if elem in seq else False


print(check([66, 101], 66))  # True
print(check([78, 117, 110, 99, 104, 117, 107, 115], 8))  # False
print(check([101, 45, 75, 105, 99, 107], 107))  # True
print(check([80, 117, 115, 104, 45, 85, 112, 115], 45))  # True
print(check(['t', 'e', 's', 't'], 'e'))  # True
print(check(["what", "a", "great", "kata"], "kat"))  # False
print(check([66, "codewars", 11, "alex loves pushups"], "alex loves pushups"))  # True
print(check(["come", "on", 110, "2500", 10, '!', 7, 15], "Come"))  # False
print(check(["when's", "the", "next", "Katathon?", 9, 7], "Katathon?"))  # True
print(check([8, 7, 5, "bored", "of", "writing", "tests", 115], 45))  # False
print(check(["anyone", "want", "to", "hire", "me?"], "me?"))  # True
