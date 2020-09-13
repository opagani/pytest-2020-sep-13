from hello import hello


def test_hello():
    output = hello('world')
    assert output == 'Hello, world!'
