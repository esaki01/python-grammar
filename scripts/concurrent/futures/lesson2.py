"""
並列処理（マルチプロセス）より簡単に実装できる.
"""

import concurrent.futures
import logging

logging.basicConfig(level=logging.DEBUG, format='%(processName)s: %(message)s')


def worker(x, y):
    logging.debug('start')
    r = x * y
    logging.debug(r)
    logging.debug('end')
    return r


if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
        f1 = executor.submit(worker, 2, 5)
        f2 = executor.submit(worker, 2, 5)
        logging.debug(f1.result())
        logging.debug(f2.result())
