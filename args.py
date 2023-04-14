def my_country(country="Rwanda"):
    print(f"Hello from{country}")

def greet(*names):
    for name in names:
        print(f"Hello {name}")
    
def sum(*numbers):
    answer=0
    for number in numbers:
        answer+=number
    return answer

def multiply(*numbers):
    answer=1
    for number in numbers:
        answer*=number
    return answer 

def student_attributes(**kwargs): 
    for key,value in kwargs.items():
        print(f"{key}:{value}")  


def concatenate_args(*detail):
    answer = ""
    for dit in detail:
        answer +=" "+dit
    return answer


def concatenate_kwargs(**kwargs):
    result = ""
    for key, value in kwargs.items():
        result +=" "+value
    return result           