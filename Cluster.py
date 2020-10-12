from Vendors.AWS import AWS
from Server import Server
from TxtBundler import TxtBundler

def c_main() -> int:
    _server = Server("UDP")


if __name__ == '__main__':
    try:
        exit(c_main())
    except KeyboardInterrupt:
        print(TxtBundler().getString(56))
