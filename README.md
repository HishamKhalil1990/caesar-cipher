# caesar-cipher
## Lab Summary:
#### create a method to encrypt a message that can then be decrypted when supplied with the corresponding key using:
- Create an encrypt function that takes in a plain text phrase and a numeric shift.
    - the phrase will then be shifted that many letters.
        - E.g. encrypt(‘abc’,1) would return ‘bcd’ = E.g. encrypt(‘abc’, 10) would return ‘klm’
    - shifts that exceed 26 should wrap around
        - E.g. encrypt(‘abc’,27) would return ‘bcd’
    - shifts that push a letter out or range should wrap around
        - E.g. encrypt(‘zzz’,1) would return ‘aaa’
- Create a decrypt function that takes in encrypted text and numeric shift which will restore the encrypted text back to its original form when correct key is supplied
- create a crack function that will decode the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key.
#### PR https://github.com/HishamKhalil1990/caesar-cipher/pull/1