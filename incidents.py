from typing import Callable
class incidentresult(object):
    alive:bool
    def __init__(self,alive:bool):
        self.alive=alive
class incident(object):
    incident_func:Callable
    incident_name:str
    def __init__(self,incident_func:Callable,incident_name:str,incident_type:int):
        '''
        incident_func 是事件函数，应当返回一个结果类（也就是incidentresult）
        incident_name 是事件名字
        incident_type 是特定标识符，可用于用户自定的事件处理
        '''
        self.incident_func=incident_func
        self.incident_name=incident_name
    def do(self) -> incidentresult:
        return self.incident_func()

def _shop():
    print(23433)
    return incidentresult(True)

def incident_generator()->list:
    '''
    使用这个generator可以一次性获得所有的事件
    '''
    return [
        incident(_shop,"shop")
    ]