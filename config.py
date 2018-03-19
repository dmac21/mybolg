

#默认的基类配置
class Config(object):
    pass

#开发配置，继承于基类配置
class DevConfig(Config):
    pass

#测试配置，继承于基类配置
class TestConfig(Config):
    pass

#生产配置，继承于基类配置
class ProductConfig(Config):
    pass