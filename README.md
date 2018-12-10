# mock-useragent



项目出现的原因：

有个叫fake-useragent的项目，在国内用起来 总是出现乱七八糟的网络问题，所以我就弄了这个项目，更好的支持离线
，目前项目刚起步，后期会慢慢完善， 有问题请 留言给我




-------------------------


警告！！ 

由于该项目刚起步，所以接下来 接口变动会比较大，所以安装使用的时候，一定要指定版本号， 以免出现意外哦








-------------------------


安装：

pip install mock-useragent==2018.12.10.3

如果安装的时候提示  Could not find a version that satisfies the requirement mock-useragent==2018.12.10.3 (from versions: )
No matching distribution found for mock-useragent==2018.12.10.3


请这样安装  pip install mock-useragent==2018.12.10.3 -i https://pypi.org/simple

-------------------------
用法

from mock_useragent import MockUserAgent

m = MockUserAgent()

print(m.random_chrome)


