#https://stackoverflow.com/questions/54382573/how-to-find-all-the-keys-having-null-values-present-in-the-nested-json-file-usin

import json
j = json.loads('[{\
  "A": "val",\
  "B": "val",\
  "C": [\
       {\
          "D": null,\
          "E": null,\
          "F": [\
               { "G": null },\
               { "G": null } \
               ]\
       },\
       {\
          "D": "val",\
          "E": null,\
          "F": [\
               { "G": null },\
               { "G": "val"} \
               ]\
       }\
       ]\
}]')

def dig(x):
    if x is None:
        return {'null': x, 'not_null': set()}

    ret = {'null': set(), 'not_null': set()}
    
    if isinstance(x, dict):
        for k in x:
            if isinstance(x[k], dict) or isinstance(x[k], list):
                sub_ret = dig(x[k])
                ret['null'].update(sub_ret['null'])
                ret['not_null'].update(sub_ret['not_null'])
            elif x[k] is None:
                ret['null'].add(k)
            else:
                ret['not_null'].add(k)

    elif isinstance(x, list):
        for i in x:
            if isinstance(i, dict) or isinstance(i, list):
                sub_ret = dig(i)
                ret['null'].update(sub_ret['null'])
                ret['not_null'].update(sub_ret['not_null'])

    else:
        return {'null': set(), 'not_null': x}

    return ret

result = dig(j)
print(result['null'] - result['not_null']) # -> {'E'}