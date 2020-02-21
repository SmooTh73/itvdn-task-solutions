sites = {}

def link_record(site_name, site_link):
    sites[site_name] = site_link

def show_link(site_name):
    try:
        return sites[site_name]
    except (KeyError, TypeError):
        return 'Name not found'

def _found_name(dictionary, site_link):
    for value in dictionary.value():
        if value == site_link:
            return value 

def show_name(site_link):
    return _found_name(sites, site_link)

def delete_link(site_name):
    for name in sites.keys():
        if name == site_name:
            del sites[site_name]
            return 'Site {} was deleted'.format(site_name)
        else:
            return 'Site not found'
