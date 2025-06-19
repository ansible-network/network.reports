def flatten_dict(data, parent_key='', sep='_'):
    items = {}
    for k, v in data.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_dict(v, new_key, sep=sep))
        elif isinstance(v, list):
            for i, item in enumerate(v):
                if isinstance(item, dict):
                    items.update(flatten_dict(item, f"{new_key}{sep}{i}", sep=sep))
                else:
                    items[f"{new_key}{sep}{i}"] = str(item)
        else:
            items[new_key] = str(v)
    return items


class FilterModule:
    def filters(self):
        return {'flatten_dict': flatten_dict}
