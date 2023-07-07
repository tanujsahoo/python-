import sys
import whois
import dns.resolver
import shodan
import requests
import argparse
import socket

argparse = argparse.ArgumentParser(description="this is basic information tool.",usage="pyhton3 info_gathering.py -d DOMAIN [-s IP ]")
argparse.add_argument("-d", "--domain", help="Enter the domain name for footprinting.")
argparse.add_argument("-s", "--shodan", help="Enter the IP for search shodan ")

args = argparse.parse_args()
domain = args.domain
ip = args.shodan

# print("[+] Domain {} and IP {}".format(domain, ip))

# whois module
print("[+] getting whois info.")
# whois module is library, creating instance
try:
    py = whois.query(domain)
    print("[+] whois  info found.")
    print("Name: {}".format(py.name))
    print("Name: {}".format(py.registrar))
    print("Name: {}".format(py.registrant))
    print("Name: {}".format(py.creation_date))
    print("Name: {}".format(py.emails))
    print("Name: {}".format(py.expiration_date))
    print("Name: {}".format(py.last_updated))
    print("Name: {}".format(py.admin))
    print("name: {}".format(py.registrant_country))
except:
    pass


#DNS Module
print("[+] getting DNS info..")
try:
    for a in dns.resolver.resolve(domain,'A'):
        print("[+] A record: {}".format(a.to_text()))
    for mx in dns.resolver.resolve(domaian, 'TXT'):
        print("[+] MX record: {}".format(mx.to_text()))
    for txt in dns.resolver(domain, 'TXT'):
        print("[+] TXT Record: {}".format(txt.to_text()))
    for ns in dns.resolver.resolve(domain, 'NS'):
        print("[+] NS record: {}".format(ns.to_txt()))
except:
    pass
#Geolocaiton module
print("[+] Getting geolocation info..")

#implementing request for web request
try:
    response = requests.request('Get', "https://geolocation-db.com/json/" +_socket.gethostname(domain)).json()
    print("[+] Country: {}".format(response['country_name']))
    print("[+] Latitude: {}".format(response['latitude']))
    print("[+] longitude: {}".format(response['longitude']))
    print("[+] City: {}".format(response['city']))
    print("[+] State: {}".format(response['state']))
except:
    pass
# shodan module
if ip:
    print("[+] Getting info from shodan for ip {}".format(ip))
    #shodan api
    api = shodan.shodan("6tiO5gP3SliqyT5WbAKqQQawKQwP7sZu")
    try:
        results = api.search(ip)
        print("[+] Result found: {}".format(results['total']))
        for result in results['matches']:
            print("[+] IP: {}".format(result['ip_str']))
            print("[+] Data: \n{}".format(result['data']))
            print()

    except:
        print("[-] shodan search error")















