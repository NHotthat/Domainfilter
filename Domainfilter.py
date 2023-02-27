import requests
import time
import platform
import requests
import queue
import threading
import sys
import argparse


def main():
    while not url.empty():
        f = url.get()
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}
        if 'https' in f or 'http' in f:
            try:
                code = requests.get(url=f, headers=headers, timeout=10)
                if code.ok == True:
                    if sys == "Linux":
                        print(
                            f"\033[36m{time.strftime('%H:%M:%S',time.localtime(time.time()))}\033[0m\033[32m[{str(code.status_code)}][+]\033[0m{f}\n", end='')
                    else:
                        print(
                            f"{time.strftime('%H:%M:%S',time.localtime(time.time()))}[{str(code.status_code)}][+]{f}\n", end='')
                    with open(f'{args.outfile}', 'a+', encoding='utf-8') as file:
                        file.write(f + "\n")
                else:
                    if sys == "Linux":
                        print(
                            f"\033[36m{time.strftime('%H:%M:%S',time.localtime(time.time()))}\033[0m\033[31m[{str(code.status_code)}][-]\033[0m{f}\n", end='')
                    else:
                        print(
                            f"{time.strftime('%H:%M:%S',time.localtime(time.time()))}[{str(code.status_code)}][-]{f}\n", end='')
            except requests.exceptions.Timeout as Timeout:
                if sys == "Linux":
                    print(
                        f"\033[36m{time.strftime('%H:%M:%S',time.localtime(time.time()))}\033[0m\033[34m[TIMEOUT]\033[0m{Timeout}\n", end='')
                else:
                    print(
                        f"{time.strftime('%H:%M:%S',time.localtime(time.time()))}[TIMEOUT]{Timeout}\n", end='')
            except requests.exceptions.RequestException as ERROR:
                if sys == "Linux":
                    print(
                        f"\033[36m{time.strftime('%H:%M:%S',time.localtime(time.time()))}\033[0m\033[34m[ERROR]\033[0m{ERROR}\n", end='')
                else:
                    print(
                        f"{time.strftime('%H:%M:%S',time.localtime(time.time()))}[ERROR]{ERROR}\n", end='')
        else:
            for i in range(0, 2, 1):
                if i == 0:
                    flag = f
                    f = "https://"+f
                elif i == 1:
                    f = "http://"+flag
                try:
                    code = requests.get(url=f, headers=headers, timeout=10)
                    if code.ok == True:
                        if sys == "Linux":
                            print(
                                f"\033[36m{time.strftime('%H:%M:%S',time.localtime(time.time()))}\033[0m\033[32m[{str(code.status_code)}][+]\033[0m{f}\n", end='')
                        else:
                            print(
                                f"{time.strftime('%H:%M:%S',time.localtime(time.time()))}[{str(code.status_code)}][+]{f}\n", end='')
                        with open(f'{args.outfile}', 'a+', encoding='utf-8') as file:
                            file.write(f + "\n")
                        break
                    else:
                        if sys == "Linux":
                            print(
                                f"\033[36m{time.strftime('%H:%M:%S',time.localtime(time.time()))}\033[0m\033[31m[{str(code.status_code)}][-]\033[0m{f}\n", end='')
                        else:
                            print(
                                f"{time.strftime('%H:%M:%S',time.localtime(time.time()))}[{str(code.status_code)}][-]{f}\n", end='')
                except requests.exceptions.Timeout as Timeout:
                    if sys == "Linux":
                        print(
                            f"\033[36m{time.strftime('%H:%M:%S',time.localtime(time.time()))}\033[0m\033[34m[TIMEOUT]\033[0m{Timeout}\n", end='')
                    else:
                        print(
                            f"{time.strftime('%H:%M:%S',time.localtime(time.time()))}[TIMEOUT]{Timeout}", end='')
                except requests.exceptions.RequestException as ERROR:
                    if sys == "Linux":
                        print(
                            f"\033[36m{time.strftime('%H:%M:%S',time.localtime(time.time()))}\033[0m\033[34m[ERROR]\033[0m{ERROR}\n", end='')
                    else:
                        print(
                            f"{time.strftime('%H:%M:%S',time.localtime(time.time()))}[ERROR]{ERROR}\n", end='')


if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.argv.append("-h")
    parser = argparse.ArgumentParser(argument_default="-h")
    parser.add_argument("-f", "--file", help="Choose file")
    parser.add_argument("-o", "--outfile", default="result.txt",
                        help="Output file, default result.txt")
    parser.add_argument("-t", "--thread", default=30,
                        help="Num of threads, default 30")
    args = parser.parse_args()
    sys = platform.system()
    if sys == "Linux":
        print(
            f"\033[33m[*] Starting @ {time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))}\033[0m\n")
    else:
        print(
            f"[*] Starting @ {time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))}\n")
    urls = []
    file = open(f'{args.outfile}', 'w').close()
    with open(f'{args.file}', 'r', encoding='utf-8') as file:
        for line in file.readlines():
            line = line.strip("\n")
            urls.append(line)
    url = queue.Queue()
    for i in urls:
        url.put(i)
    for i in range(int(args.thread) + 1):
        thread = threading.Thread(target=main)
        thread.start()

