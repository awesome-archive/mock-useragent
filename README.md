# mock-useragent

警告！！ 

由于该项目刚起步，所以接下来 接口变动会比较大，所以安装使用的时候，一定要指定版本号， 以免出现意外哦


用法：

pip install mock-useragent==2018.12.10.3

如果安装的时候提示  Could not find a version that satisfies the requirement mock-useragent==2018.12.10.3 (from versions: )
No matching distribution found for mock-useragent==2018.12.10.3


请这样安装  pip install mock-useragent==2018.12.10.3 -i https://pypi.org/simple


from mock_useragent import MockUserAgent

m = MockUserAgent()

print(m.random_chrome)


