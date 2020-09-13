from hello import hello


def test_hello():
    output = hello('world')
    assert output == 'Hello, world!'


def test_hello2():
    output = hello('someone else')
    assert output == 'Hello, someone else!'
