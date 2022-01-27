import vowels

def test_vowels_small():
    assert vowels.vowels("dog") == 1

def test_vowels_big():
    assert vowels.vowels("Onomatopoeia") == 8