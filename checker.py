import os

# 파일 목록 정의
files = [
    "chmod", "clock_nanosleep", "clone", "creat", "epoll_create1", "eventfd",
    "fanotify_init", "getitimer", "get_mempolicy", "getpriority", "getrandom",
    "getrusage", "inotify_init1", "madvise", "mbind", "memfd_create", "mkdir",
    "mlock2", "mlockall", "move_pages", "mprotect", "mq_open", "mremap", "msgrcv",
    "msync", "open", "pipe2", "pkey_alloc", "pkey_mprotect", "prctl", "ptrace",
    "semop", "semtimedop", "setitimer", "set_mempolicy", "setpriority",
    "signalfd", "sigprocmask", "socket", "socketpair", "swapon", "timerfd_create",
    "timerfd_settime", "umask", "unshare"
]

# 현재 디렉토리에 .json 파일이 있는지 확인하여 결과 생성
table_rows = []
for file in files:
    filename = f"{file}.json"
    exists = os.path.isfile(filename)
    table_rows.append(f"| {file} | {'true' if exists else 'false'} |")

# Markdown 형식의 표 작성
markdown_table = "\n| File | Exists |\n| --- | --- |\n" + "\n".join(table_rows)

# README.md 파일에 표 추가
with open("README.md", "a") as readme_file:
    readme_file.write(markdown_table)

print("Markdown table appended to README.md")

