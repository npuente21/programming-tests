objects = [
    {
        "age": 12,
        "name": "Mateo",
        "last_name": "González",
    },
    {
        "age": 25,
        "name": "Arturo",
        "last_name": "González",
    },
    {
        "age": 12,
        "name": "Julián",
        "last_name": "Fernández",
    },
]


def indexing_level(document, keys, result):
    """Aquí va la solución"""

    if len(keys) == 1:
        key = keys[0]
        if document[key] in result.keys():
            result[document[key]].append(document)

            return result
        else:
            result[document[key]] = [document]
            return result
    else:
        value = document[keys[0]]
        if value not in result:
            aux = {}
            result[value] = indexing_level(document, keys[1:], aux)
        else:
            aux = indexing_level(document, keys[1:], result[value])
    return result


def multilevel_indexing(documents, keys):
    """Aquí va la solución"""
    result = {}
    for document in documents:
        result.update(indexing_level(document, keys, result))

    return result


result = multilevel_indexing(objects, ["age", "last_name"])
print(result)
