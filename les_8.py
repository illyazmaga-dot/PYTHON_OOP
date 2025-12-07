import logging
"""
logging.basicConfig(level=logging.DEBUG,
                    filename="logs.log",
                    filemode="w",
                    format="We have next logging message:%(asctime)s:%(levelname)s - %(message)s"
                    )
logging.debug("my_debug")
logging.info("my_info")
logging.warning("my_warning")
logging.error("my_error")
logging.critical("my_critical")
assert 2+2 == 5, "My error"


def adder(*args, **kwargs):
    result = 0
    for _ in args:
        result += _
    for _ in kwargs.values():
        result += _
    return result
"""
def adder(*args, **kwargs):
    result = 0

    for _ in args:
        if isinstance(_, (int, bool, float)):
            result += _
        else:
            try:
                result += float(_)
                continue
            except (ValueError, TypeError):
                pass
            try:
                result += int(_)
                continue
            except (ValueError, TypeError):
                pass

    for _ in kwargs.values():
        if isinstance(_, (int, bool, float)):
            result += _
        else:
            try:
                result += float(_)
                continue
            except (ValueError, TypeError):
                pass
            try:
                result += int(_)
                continue
            except (ValueError, TypeError):
                pass

    return result
