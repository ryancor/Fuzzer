import sys
import time
import requests
from services.options import Input
from services.injections import Injections

def all_options():
    ## Welcome Message
    Input.welcome()

    ## Input the endpoint to inject & asking for request type
    end_point = Input.ep_options()
    request_type = Input.req_options()
    request_case = request_type.casefold()

    ## Incase user wants to have basic auth
    user, passwd = Input.auth_options()

    ## Option for user to include headers
    header_q = Input.header_num_options()
    head = {}
    if header_q.isdigit():
        for x in range(0, int(header_q)):
            head_type, head_content = Input.header_options()
            head.update(dict(((head_type, head_content),)))
    else:
        head = {}

    return end_point, request_type, request_case, user, passwd, head


def inject_options():
    ## Type of injection
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
    elif inject_case == 'UrlSnoop'.casefold():
        ops.append(Injections.url_snoop())
    else:
        print('\n[-] Not a valid injection type.')
        sys.exit(0)

    return injection_type, ops

def main():
    end_point, request_type, request_case, user, passwd, head = all_options()
    injection_type, ops = inject_options()

    print('\n[+] Running {0} Scan'.format(injection_type.upper()))

    for arr in ops[0]:
        try:
            time.sleep(2)

            if '[]' in end_point:
                new_ep = end_point.replace('[]', arr)

                if request_case == 'GET'.casefold():
                    r = requests.get(new_ep, auth=(user, passwd), headers=head)
                elif request_case == 'POST'.casefold():
                    r = requests.post(new_ep, auth=(user, passwd), headers=head)
                elif request_case == 'PUT'.casefold():
                    r = requests.put(new_ep, auth=(user, passwd), headers=head)
                elif request_case == 'DEL'.casefold():
                    r = requests.delete(new_ep, auth=(user, passwd), headers=head)
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

if __name__ == '__main__':
    main()
