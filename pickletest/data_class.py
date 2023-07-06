import process_class

class host:
    def __init__(s,name,ip):
        s.name = name
        s.ip = ip

    def __repr__(s):
        return (f"name:{s.name} ip:{s.ip}")
    def change_ip(self):
        process_class.increase_ip(self)
        return self

