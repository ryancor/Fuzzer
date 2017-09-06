import sys
import time
import requests
from services.options import Input
from services.injections import Injections

Input.welcome()

end_point = Input.ep_options()
request_type = Input.req_options()
request_case = request_type.casefold()

user, passwd = Input.auth_options()

injection_type = Injections.injection_options()
inject_case = injection_type.casefold()

ops = []
if inject_case == 'SQL'.casefold():
    ops.append(Injections.sql_injections())
elif inject_case == 'XSS'.casefold():
    ops.append(Injections.xss_injections())
elif inject_case == 'Command'.casefold():
    ops.append(Injections.command_injections())
elif inject_case == 'RCE'.casefold():
    ops.append(Injections.rce_injections())
elif inject_case == 'LFI'.casefold():
    ops.append(Injections.sql_injections())
elif inject_case == 'LDAP'.casefold():
    ops.append(Injections.ldap_injections())
elif inject_case == 'Fuzzer'.casefold():
    ops.append(Injections.sql_injections())
elif inject_case == 'DAST'.casefold():
    ops.append(Injections.dast_scan())
else:
    print('\n[-] Not a valid injection type.')
    sys.exit(0)

print('\n[+] Running {0} Scan'.format(injection_type.upper()))

for arr in ops[0]:
    try:
        time.sleep(2)

        if '[]' in end_point:
            new_ep = end_point.replace('[]', arr)

            if request_case == 'GET'.casefold():
                r = requests.get(new_ep, auth=(user, passwd))
            elif request_case == 'POST'.casefold():
                r = requests.post(new_ep, auth=(user, passwd))
            elif request_case == 'PUT'.casefold():
                r = requests.put(new_ep, auth=(user, passwd))
            elif rrequest_case == 'DEL'.casefold():
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
