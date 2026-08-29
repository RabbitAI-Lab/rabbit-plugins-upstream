"""通道注册表：按 name 注册/查找 Channel，新增通道只需在 channels/ 加文件。"""
import importlib

_CHANNELS = {}


def register(channel_class):
    _CHANNELS[channel_class.name] = channel_class
    return channel_class


def get(name: str):
    return _CHANNELS.get(name)


def names() -> list:
    return sorted(_CHANNELS.keys())


def load_all():
    """导入所有内置通道模块（触发 @register 注册）。"""
    for mod in ("feishu", "wecom", "dingtalk", "slack", "telegram", "email"):
        importlib.import_module("channels." + mod)
    return _CHANNELS
