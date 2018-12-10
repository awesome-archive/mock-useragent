from setuptools import setup


PY_MODULES = ['offline_datas',]

setup(name='mock-useragent',
      version='2018.12.10.3',
      description='类似fake-useragent，国内的网络导致用fake-useragent不太方便，所以诞生了mock-useragent这个项目',
      url='https://github.com/find456789/mock-useragent',
      author='find456789',
      # author_email='None',
      license='MIT',
      keywords=['useragent','mock-useragent','user agent'],
      packages=['mock_useragent','mock_useragent.offline_datas',],
      # package_data = {'mock_useragent':['offline_datas/*.json']},  # 包数据文件，与包的执行相关
      # package_dir={'':'mock_useragent'}, # 表示包都在lib文件夹下

      zip_safe=False)