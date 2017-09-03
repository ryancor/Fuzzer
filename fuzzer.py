import time
import requests
from services.options import Input

Input.welcome()

end_point = Input.ep_options()
request_type = Input.req_options()

user, passwd = Input.auth_options()

injection_type = Input.injection_options()

ops = []
if injection_type == 'SQL':
    ops.append(Input.sql_injections())
elif injection_type == 'XSS':
    ops.append(Input.sql_injections())
elif injection_type == 'Command':
    ops.append(Input.sql_injections())
elif injection_type == 'RCE':
    ops.append(Input.sql_injections())
elif injection_type == 'RCE':
    ops.append(Input.sql_injections())
elif injection_type == 'Fuzzer':
    ops.append(Input.sql_injections())
elif injection_type == 'LDAP':
    ops.append(Input.sql_injections())
else:
    ops.append(Input.sql_injections())

for arr in ops[0]:
    try:
        time.sleep(2)

        if '[]' in end_point:
            new_ep = end_point.replace('[]', arr)

            if request_type == 'GET' or request_type == 'get':
                r = requests.get(new_ep, auth=(user, passwd))
            elif request_type == 'POST' or request_type == 'post':
                r = requests.post(new_ep, auth=(user, passwd))
            elif request_type == 'PUT' or request_type == 'put':
                r = requests.put(new_ep, auth=(user, passwd))
            elif request_type == 'DEL' or request_type == 'del':
                r = requests.delete(new_ep, auth=(user, passwd))
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
