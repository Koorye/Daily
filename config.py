from munch import DefaultMunch
from importlib import import_module


def load_cfg(cfg_name='DEFAULT_CFG'):
    """根据名称动态加载配置"""
    module = import_module('config')
    cfg = getattr(module, cfg_name)
    return cfg

def compact_cfg(cfg, args):
    """将配置字典与命令行参数合并, 并转换为object"""
    for k in vars(args):
        v = getattr(args, k)
        keys = k.split('.')
        
        cfg_ = cfg
        for idx, key in enumerate(keys):
            if idx == len(keys) - 1:
                cfg_[key] = v
            else:
                cfg_ = cfg[key]
    
    return DefaultMunch.fromDict(cfg)


DEFAULT_CFG = dict(
    mail = dict(
        host='your mail host',
        username='your mail username',
        password='your mail password',
        to='mail send to'))
