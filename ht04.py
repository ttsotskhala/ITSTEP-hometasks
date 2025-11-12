#1

st = input("Enter a string: ")
st1 = st.encode()
print(f"{st1}\n")

print()

#2
st0 = input("Enter a string: ")
st01 = st0.strip().casefold()
if "python" in st01:
    st02 = st01.replace('python', 'Python', 1)
    print(st02)
else:
    print(st01 + " Python")

print()



#3
text = input("Enter a string: ")
half_text = len(text)//2
print(text[:half_text])
print()

#4
str = input("Enter a string:")
has_letter = any(c.isalpha() for c in str)
has_digit = any(c.isdigit() for c in str)
if has_letter and has_digit and str.isalnum():
 print("Valid")
else:
    print("Not valid")

print()



#5

txt = input('Enter a string: ')
txt1 = txt.encode()
print (txt1)
txt2 = txt1.decode()
print(txt2)
print()