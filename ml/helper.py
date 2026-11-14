import logging
import time
from functools import wraps

"""
Informed by https://ankitbko.github.io/blog/2021/04/logging-in-python/
"""

logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def time_log_wrap(func):
    """
    Wrapper that both times and logs the info and errors from the given function. 
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Starting {func.__name__}...")
        start = time.time()
        try:
            result = func(*args, **kwargs)
            logger.info(f"{func.__name__} finished in {time.time() - start} time.")
            return result
        except Exception as e:
            logger.error(f"{func.__name__} errored after {time.time() - start} time with {str(e)}")
            raise e
        
    return wrapper