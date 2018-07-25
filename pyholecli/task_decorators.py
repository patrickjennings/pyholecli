from functools import wraps
from fabric import task
from pyholecli.services import HostnameUtility, PiholeCLI


def task_decorator_wrapper(service, *args, **kwargs):
    def decorator(f):
        @task(*args, **kwargs)
        @wraps(f)
        def wrapper(connection, *args, **kwargs):
            return f(service(connection), *args, **kwargs)
        return wrapper
    return decorator


def piholetask(*args, **kwargs):
    return task_decorator_wrapper(PiholeCLI, *args, **kwargs)


def hostnametask(*args, **kwargs):
    return task_decorator_wrapper(HostnameUtility, *args, **kwargs)
