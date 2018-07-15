import random

d = {}


def shortLink(slug, destination):
    if (slug == None):
        slug = generateRandomSlug_2()
    else:
        if slug  in d:
            print( "slug already exists")
    d[slug] = destination


def generateRandomSlug():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    numChars = 7
    while 1:
        result = ""

        for i in range(numChars):
            randomIndex = random.randrange(len(alphabet) - 1)
            result += alphabet[randomIndex]

        if result not in d:
            return result


#
#
currentRandomSlugId = 0


def generateRandomSlug_2():
    slug = ""
    while 1:
        global currentRandomSlugId
        currentRandomSlugId += 1
        newId = currentRandomSlugId
        slug = encode(newId)

        if slug not in d:
            break

    return slug


BASE62 = "23456789abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ"


def encode(num, alphabet=BASE62):
    """Encode a positive number in Base X

    Arguments:
    - `num`: The number to encode
    - `alphabet`: The alphabet to use for encoding
    """
    if num == 0:
        return alphabet[0]
    arr = []
    base = len(alphabet)
    while num:
        num, rem = divmod(num, base)
        arr.append(alphabet[rem])
    arr.reverse()
    return ''.join(arr)


def decode(string, alphabet=BASE62):
    """Decode a Base X encoded string into the number

    Arguments:
    - `string`: The encoded string
    - `alphabet`: The alphabet to use for encoding
    """
    base = len(alphabet)
    strlen = len(string)
    num = 0

    idx = 0
    for char in string:
        power = (strlen - (idx + 1))
        num += alphabet.index(char) * (base ** power)
        idx += 1

    return num


shortLink(None, "https://stackoverflow.com/questions/1119722/base-62-conversion")

print(d)
