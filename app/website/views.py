from django.http import HttpResponse


def fibonacci(request, int_input):
    result=calculate_fib(int_input)
    return HttpResponse(
        result,
        content_type='text/plain'
    )
def calculate_fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

