import sys, os

inp, out, depth = sys.argv[1:]
depth = int(depth)
for path, _, files in os.walk(inp):
    pwd = path.replace(inp, '')
    pwd = pwd.split('/')
    st = len(pwd) - (depth - 1)
    for i in range(st, len(pwd)):
        os.system(
            f'mkdir -p {out}/{'/'.join(pwd[i:])}'
        )
    for file in files:
        os.system(
            f"cp {path}/{file} {out}/{'/'.join(pwd[st:])}"
        )
