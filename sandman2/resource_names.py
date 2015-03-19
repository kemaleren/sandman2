from sandman2.custom_names import custom_names


def _make_name(name, pluralize):
    name = name.lower()
    if name in custom_names:
        s, p = custom_names[name]
    else:
        s, p = name, '{}s'.format(name)
    name = p if pluralize else s
    return name


def singular(name):
    return _make_name(name, False)


def plural(name):
    return _make_name(name, True)
