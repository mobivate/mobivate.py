import random

def random_number():
    return str(random.randint(10000000, 90000000))

def random_salt():
    alpha = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    chars = []
    for i in range(16):
        chars.append(random.choice(alpha))
    return ''.join(chars)

def dict_to_xml(root):
    xml = ''
    for key in root.keys():
        if isinstance(root[key], dict):
            xml = '%s<%s>\n%s</%s>\n' % (xml, key, dict_to_xml(root[key]), key)
        elif isinstance(root[key], list):
            xml = '%s<%s>' % (xml, key)
            for item in root[key]:
                xml = '%s%s' % (xml, dict_to_xml(item))
            xml = '%s</%s>' % (xml, key)
        else:
            value = root[key]
            xml = '%s<%s>%s</%s>\n' % (xml, key, value, key)
    return xml