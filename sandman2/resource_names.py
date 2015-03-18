do_dasherize = True

custom_resource_names = {
    'log_entry': ('log-entry', 'log-entries'),
}


def _make_name(name, pluralize):
    name = name.lower()
    if name in custom_resource_names:
        s, p = custom_resource_names[name]
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


def dict_dasherize(d):
    if isinstance(d, dict):
        result = {k.replace('_', '-'): dict_dasherize(v) for k, v in d.items()}
    else:
        result = d
    return result
