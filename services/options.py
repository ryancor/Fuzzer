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
