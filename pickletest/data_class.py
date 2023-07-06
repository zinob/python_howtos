from dataclasses import dataclass
import process_class

@dataclass
class host:
    name: str
    ip: int
    def change_ip(self):
        process_class.increase_ip(self)
        return self

