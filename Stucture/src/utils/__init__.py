from functools import wraps
import os


def init_vars():
    """Initialize component"""

    def inner(func):
        @wraps(func)
        def decorator(*args, **kwargs):
            component = func(*args, **kwargs)
            component.set_env_variable(
                name="ENV_FOR_DYNACONF",
                value=os.environ["ENV_FOR_DYNACONF"],
            )
            return component

        return decorator

    return inner
