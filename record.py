try:
    from inspect import signature
except ImportError:
    from funcsigs import signature

import logging
import functools


LOG = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

def recording(f):
    """Decorator function that records calls to functions (methods).
       It outputs the received parameter and return value to the log
    """
    @functools.wraps(f)
    def _recording(*args, **kwargs):
        result = f(*args, **kwargs)
        sig = signature(f)
        bound_args = sig.bind(*args, **kwargs)
        func_name = f.__name__
        func_args = ','.join('{k}={v}'.format(k=k, v=v)
                             for k, v in bound_args.arguments.items())
        fmt = '{func_name}({func_args}) -> {result}'
        msg = fmt.format(func_name=func_name,
                         func_args=func_args,
                         result=result)
        LOG.debug(msg)
        return result
    return _recording


"""Usage:
@recording
def add(a, b):
    return a + b


def main():
    logging.basicConfig(level=logging.DEBUG)
    print(add(1, 2))


if __name__ == '__main__':
    main()
"""
