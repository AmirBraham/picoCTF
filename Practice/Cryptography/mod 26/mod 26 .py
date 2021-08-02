"""
Cryptography can be easy, do you know what ROT13 is? cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_MAZyqFQj}
"""

# ROT13 simple etter substitution cipher , that replaces a letter with the 13th letter after it in the alphabet.


from typing import cast


def rot13(string):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    encryptedString = ""
    for c in string:
        isUpperCase = c.isupper()
        try:
            idx = alphabet.index(c.lower())

            encryptedString += (alphabet[(idx + 13) % 26]
                                ).upper() if isUpperCase else (alphabet[(idx + 13) % 26])
        except:
            encryptedString += c

    print(alphabet)
    return encryptedString


# applying rot13 twice gets intial string
print(rot13("arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_MAZyqFQj"))
