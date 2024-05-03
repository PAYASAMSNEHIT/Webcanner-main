#!/usr/bin/env python3

from src.domainator import Domainator
from src.utils import pr, choose

def main_menu(dom: Domainator):
    while True:
        cc = choose(
            ['Whois Lookup', 'Reverse IP Lookup',
             'Grab Headers & CloudFlare', 'Site Speed Check',
             'Sub-domains Scan'],
            'Choose action:'
        )
        if cc < 0:
            break
        if cc == 0:
            dom.whois()
        elif cc == 1:
            while True:
                ccc = choose(['HackerTarget', 'YouGetSignal'],
                             'Choose method:')
                if ccc < 0:
                    break
                elif ccc == 0:
                    dom.reverse_HT()
                elif ccc == 1:
                    dom.reverse_YGS()
        elif cc == 2:
            dom.banners_cloud_flare()
        elif cc == 3:
            dom.speed_check()
        elif cc == 4:
            dom.find_subdomains()


if __name__ == '__main__':
    try:
        main_menu(Domainator())
    except KeyboardInterrupt:
        pr('Interrupted!', '!')
#!/usr/bin/env python3

from src.domainator import Domainator
from src.utils import pr, choose

def main_menu(dom: Domainator):
    while True:
        cc = choose(
            ['Whois Lookup', 'Reverse IP Lookup',
             'Grab Headers & CloudFlare', 'Site Speed Check',
             'Sub-domains Scan'],
            'Choose action:'
        )
        if cc < 0:
            break
        if cc == 0:
            dom.whois()
        elif cc == 1:
            while True:
                ccc = choose(['HackerTarget', 'YouGetSignal'],
                             'Choose method:')
                if ccc < 0:
                    break
                elif ccc == 0:
                    dom.reverse_HT()
                elif ccc == 1:
                    dom.reverse_YGS()
        elif cc == 2:
            dom.banners_cloud_flare()
        elif cc == 3:
            dom.speed_check()
        elif cc == 4:
            dom.find_subdomains()


if __name__ == '__main__':
    try:
        main_menu(Domainator())
    except KeyboardInterrupt:
        pr('Interrupted!', '!')
