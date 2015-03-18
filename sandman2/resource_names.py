from sandman2.custom_names import custom_names


do_dasherize = True


def _make_name(name, pluralize):
    name = name.lower()
    if name in custom_names:
        s, p = custom_names[name]
    else:
        s, p = name, '{}s'.format(name)
    name = p if pluralize else s
    if do_dasherize:
        name = name.replace('_', '-')
    return name


def singular(name):
    return _make_name(name, False)


def plural(name):
    return _make_name(name, True)


def dict_replace(d, c1, c2):
    if isinstance(d, dict):
        result = {k.replace(c1, c2): dict_dasherize(v) for k, v in d.items()}
    else:
        result = d
    return result


def dict_dasherize(d):
    return dict_replace(d, '_', '-')


def dict_underize(d):
    return dict_replace(d, '-', '_')
