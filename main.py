import time

from package.front.routes import start_web
import threading


def main():
    t_web = threading.Thread(target=start_web)

    t_web.start()
    t_web.join()


if __name__ == '__main__':
    main()
