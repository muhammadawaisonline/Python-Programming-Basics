from str_function import hello


""" def test_str_fn():
    assert hello("Awais") == "Hello Awais"
    assert hello() == "Hello World" """

def test_default_str_fn():
    assert hello() == "Hello world"

""" def test_argument_str_fn():
    assert hello("Awais") == "Hello Awais" """
 

      #using Loop for testing function
for name in ["hermoine", "Harry", "Ron", "Darco"]:
    assert hello(name) == f"Hello {name}"