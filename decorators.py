def html_tag(tag='h1'):
    def wrapper(fn):
        def inner(name):
            result = f"<p>{fn(name)}</p>"
            result = result.replace(name, f'<{tag}>{name}</{tag}>')

            return result
        return inner
    return wrapper




def capitalize(fn):
    def inner(name):
        #result = f"<p>{fn(name)}</p>"
        #result = result.replace(name, f'<h1>{name}</h1>')
        return fn(name.title())

    return inner


@capitalize
@html_tag('h2')
def hello(name):
    return f"Hello {name}"


@capitalize
@html_tag()
def goodbye(name):
    return f"Bye {name}"


print(hello("paweł"))
print(goodbye("paweł"))

# <p>Hello <h1>Paweł</h1></p>