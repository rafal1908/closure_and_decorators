def full_sentence(name):
    age = 36
    xd = "lol"

    def sentence(city):
        return f"I am {name}, age: {age} and come from {city}"

    return sentence


# s = full_sentence("Paweł")
# print(s.__closure__[0].cell_contents)
# print(s("Kraków"))
# print(s("Katowice"))



def gen_uuid():
    idx = 0 # dwie funckjce, zewnętrzna zwraca wewnętrzną
    def next_id():
        nonlocal idx
        result = idx
        idx += 1
        return result

    return next_id

uuid = gen_uuid()


for _ in range(10):
    print(uuid())