import pytest
from caesar_cipher import __version__
from caesar_cipher.caesar_cipher import encrypt,decrypt,crack

def test_version():
    assert __version__ == '0.1.0'

def test_encrypt_one():
    expected = 'N qrnq qhpx qbrfa\'g syl onpxjneq'
    actual = encrypt('A dead duck doesn\'t fly backward',13)
    assert actual == expected

def test_encrypt_two():
    expected = 'Nled lcp rzzo aped, qzc espj lcp nwply lyo lcp yze yztdj'
    actual = encrypt('Cats are good pets, for they are clean and are not noisy',37)
    assert actual == expected

def test_decrypt_one():
    expected = 'A dead duck doesn\'t fly backward'
    actual = decrypt('N qrnq qhpx qbrfa\'g syl onpxjneq',13)
    assert actual == expected

def test_decrypt_two():
    expected = 'Cats are good pets, for they are clean and are not noisy'
    actual = decrypt('Nled lcp rzzo aped, qzc espj lcp nwply lyo lcp yze yztdj',37)
    assert actual == expected

def test_crak_one():
    expected = 'It was the best of times, it was the worst of times.'
    decryptrd = decrypt('It was the best of times, it was the worst of times.',35)
    actual = crack(decryptrd)
    assert actual == expected

@pytest.mark.parametrize(
    "input,expected",
    [
        ("Uijt xbt b hppe ebz xjui zpv","This was a good day with you"),
        ("Xzmv dv pfli dfevp Urizf","Give me your money Dario"),
        ("P fjxti wdjht xh cxrt jcixa ndj pgt dgstgts id hipn xc xi udg bdciwh","A quiet house is nice until you are ordered to stay in it for months"),
        ("R uxen njcrwp cxjbcnm lqnnbn jwm cdwj bjwmfrlqnb","I love eating toasted cheese and tuna sandwiches"),
    ],
)
def test_crack_two(input,expected):
    actual = crack(input)
    assert actual == expected
