class Input():
    def ep_options():
        end_point = input('[!] Please provide an endpoint\
        \n(Mark your entry Ex: http://myvulnsite.com/index.php?id=[]): ')

        return end_point

    def req_options():
        request_type = input('[!] GET, POST, PUT, DELETE? ')

        return request_type
