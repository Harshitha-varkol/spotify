s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if s1 != s2:
    print("String 1:", s1, "Length:", len(s1))
    print("String 2:", s2, "Length:", len(s2))


s1 = input("Enter a string: ")
vowels = "aeiouAEIOU"
s3 = ""

for i in range(1, len(s1)):
    if s1[i] not in vowels:
        s3 += s1[i - 1]
print("Output:", s3)


ch = input("Enter a character: ")
if ch.isdigit() and int(ch) % 2 == 0:
    print("Even number:", ch)
else:
    print("Not an even number")


ch = input("Enter a character: ")
if not ch.isalnum():
    print("Special character:", ch, "ASCII:", ord(ch))
else:
    print("Not a special character")


ch = input("Enter a character: ")
if ch.islower():
    print("Replicated (Uppercase):", ch.upper())
else:
    print("Not a lowercase character")


ch = input("Enter a character: ")
if ch.isupper():
    print("Replicated (Lowercase):", ch.lower())
else:
    print("Not an uppercase character")


s = input("Enter a string: ")
print("Uppercase:", s.upper())


s = input("Enter a string: ")
print("Lowercase:", s.lower())

ch = input("Enter a character: ")
if ch.isalpha():
    print("Alphabet")
elif ch.isdigit():
    print("Digit")
elif not ch.isalnum():
    print("Special character")
else:
    print("Invalid input")


s = input("Enter a sentence: ")
print("Reversed:", s[::-1])