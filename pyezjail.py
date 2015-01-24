#!/usr/bin/env python
import sys
from jail.parser import get_jails_config


def main():
    """Main function"""

    try:
        print(get_jails_config())
    except:
        return 1
    else:
        return 0

if __name__ == "__main__":
    sys.exit(main())
