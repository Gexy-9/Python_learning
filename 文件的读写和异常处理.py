"""
'r':读取
'w':写入（会先截断之前的内容）
'x':写入
'a':追加
'b':二进制模式
't':文本模式（默认）
'+':更新（既可以读又可以写）
"""

file=open('实验文件.txt','r',encoding='utf-8')
print(file.read())
file.close()
print()

file=open('实验文件.txt','r',encoding='utf-8')
for line in file:
    print(line,end='')
file.close()

print()
print()
file=open('实验文件.txt','r',encoding='utf-8')
lines=file.readlines()
for line in lines:
    print(line,end='')
file.close()

file=open('实验文件.txt','a',encoding='utf-8')
file.write('\n日期：8.15')
file.write('\n内容：文件读写')
file.close()

file=open('实验文件.txt','r',encoding='utf-8')
print(file.read())
file.close()
print()

#Python的异常机制
file=None
try:
    file=open('实验文件.txt','r',encoding='utf-8')
    print(file.read())
except FileNotFoundError:
    print('无法打开指定文件')
except LookupError:
    print('指定了未知的代码')
except UnicodeDecodeError:
    print('读取文件时解码错误')
finally:
    if file:
        file.close()
#except块来捕获异常并进行相应的处理
#文件找不到会引发FileNotFoundError，
#指定了未知的编码会引发LookupError，
#而如果读取文件时无法按指定编码方式解码文件会引发UnicodeDecodeError
#else代码块，这是try 中的代码没有出现异常时会执行的代码，而且else中的代码不会再进行异常捕获
#也就是说如果遇到异常状况，程序会因异常而终止并报告异常信息
#finally块的代码不论程序正常还是异常都会执行

#Python异常类型继承结构
"""
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning
"""