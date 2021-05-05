import unittest
import time
import HtmlTestRunner

suit = unittest.defaultTestLoader.discover(start_dir="./case/", pattern="unit*.py")


now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
filename="./report/"+now+".html"
print(filename)
with open(filename, "wb") as f:
    runner = HtmlTestRunner.HTMLTestRunner(f,\
                                           title="登录", description="用例测试")
    runner.run(suit)
