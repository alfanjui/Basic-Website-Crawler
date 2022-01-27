#!/usr/bin/env python 3

import requests
import optparse

def user_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-d", "--domain", dest="domain", help="dominio objetivo")
    parser.add_option("-w", "--wordlist", dest="wordlist", help="wordlist a usar")
    parser.add_option("-o", "--output", dest="output", help="path para el output")
    return parser.parse_args()

def request(url):
    try:
        return requests.get("https://" + url)
    except requests.exceptions.ConnectionError:
        pass

def save_output(path, content):
    with open(path, "wb") as crawler_out:
        crawler_out.write(content)
        return 0

options = user_arguments()

with open(options.wordlist, "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = word + "." + options.domain
        response = request(test_url)
        if response:
            while response:
                print("[+] Found a subdomain! -->" + test_url)
                results_list = str("[+] Found a subdomain! -->" + test_url)

if options.output:
    result = save_output(options.output, results_list)
    if result == 0:
        print("Everything is saved and went without bugs!")
    else:
        print("Something went wrong! please try to save again!")

else:
    pass
