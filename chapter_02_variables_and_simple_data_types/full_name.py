first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"

print(full_name)


print(f"Hello, {full_name.title()}")

print("python")


# Spacing using backslash \n for new line and \t for a tab space
print("\tPython")

print("Languages:\nPython\nC\nJavaScript")

print("Languages:\n\tPython\n\tC\n\tJavaScript")

#  Stripping Whitespaces

favorite_language = ' python '
print(favorite_language)
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())
# Striping functions are used to clean data prior storing

# Removing Prefixes
nostarch_url = 'https://nostarch.com'
nostarch_url.removeprefix('https://')
print(nostarch_url)
simple_url = nostarch_url.removesuffix('.com')
print(simple_url)







