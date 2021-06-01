import pytest
from caesar_cipher import __version__
from caesar_cipher.caesar_cipher import encrypt,decrypt,crack

def test_version():
    assert __version__ == '0.1.0'

def test_encrypt_one():
    expected = 'n qrnq qhpx qbrfa\'g syl onpxjneq'
    actual = encrypt('A dead duck doesn\'t fly backward',13)
    assert actual == expected

def test_encrypt_two():
    expected = 'nled lcp rzzo aped, qzc espj lcp nwply lyo lcp yze yztdj'
    actual = encrypt('Cats are good pets, for they are clean and are not noisy',37)
    assert actual == expected

def test_decrypt_one():
    expected = 'writing a list of random sentences is harder than i initially thought it would be'
    actual = decrypt('snepejc w heop kb nwjzki oajpajyao eo dwnzan pdwj e ejepewhhu pdkqcdp ep skqhz xa',22)
    assert actual == expected

def test_decrypt_two():
    expected = 'he quietly entered the museum as the super bowl started'
    actual = decrypt('tq cguqfxk qzfqdqp ftq ygeqgy me ftq egbqd naix efmdfqp',116)
    assert actual == expected

@pytest.mark.parametrize(
    "input,expected",
    [
        ("uijt xbt b hppe ebz xjui zpv","this was a good day with you"),
        ("xzmv dv pfli dfevp urizf","give me your money dario"),
        ("p fjxti wdjht xh cxrt jcixa ndj pgt dgstgts id hipn xc xi udg bdciwh","a quiet house is nice until you are ordered to stay in it for months"),
        ("r uxen njcrwp cxjbcnm lqnnbn jwm cdwj bjwmfrlqnb","i love eating toasted cheese and tuna sandwiches"),
    ],
)
def test_crack(input,expected):
    actual = crack(input)
    assert actual == expected
