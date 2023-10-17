import os
import subprocess


def print_sum(var1, var2):
    result = int(var1) + int(var2)
    print(f'result is - {result}')
    cmd = f"echo res={result} >> $GITHUB_OUTPUT"
    print('cmd is - {}'.format(cmd))
    subprocess.call(cmd, shell=True)


if __name__ == '__main__':
    NUM1 = os.environ['INPUT_NUM1']
    NUM2 = os.environ['INPUT_NUM2']
    print_sum(NUM1, NUM2)
