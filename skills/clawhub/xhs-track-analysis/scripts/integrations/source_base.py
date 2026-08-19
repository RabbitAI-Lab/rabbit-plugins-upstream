# -*- coding: utf-8 -*-
"""
scripts/integrations/source_base.py
A 方案（官方/第三方合规数据平台）的数据源抽象层。
定义统一接口与记录结构，使 蒲公英/聚光/千瓜·新红 等都能归一化到同一主表 schema，
与 scripts/collector（B 方案）共享下游分析。
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass, field


@dataclass
class NoteRecord:
    """归一化后的单篇笔记记录，对应主表「三、采集记录 / 四、重点笔记与达人」字段。"""
    keyword: str = ""                 # 命中的关键词（保留全部）
    sort: str = ""                    # 排序角度
    note_id: str = ""
    url: str = ""
    title: str = ""
    author: str = ""
    author_type: str = "unknown"      # self(达人本人) / third_party(讲该达人的其他账号) / unknown
    commercialization: str = "unknown"  # natural(自然) / suspected_promo(疑似投放) / paid(明确合作) / unknown
    likes: int = 0
    collects: int = 0
    comments: int = 0
    comment_sample: list = field(default_factory=list)  # 抽样评论（按四行为预归类留待分析）
    captured_at: str = ""


class DataSource(ABC):
    """所有数据源适配器统一实现此接口。"""

    name = "base"

    def __init__(self, config: dict = None):
        self.config = config or {}

    @abstractmethod
    def authenticate(self):
        """鉴权：读取 config 中的 token/cookie/key，失败抛错。"""
        ...

    @abstractmethod
    def search_notes(self, keyword: str, sort: str, limit: int) -> list:
        """按关键词+排序返回 NoteRecord 列表。"""
        ...

    @abstractmethod
    def get_note_detail(self, note_id: str) -> NoteRecord:
        """获取单篇笔记详情（正文/素材/互动量）。"""
        ...

    @abstractmethod
    def get_comments(self, note_id: str, limit: int) -> list:
        """获取笔记评论（用于四行为归类）。"""
        ...

    @abstractmethod
    def get_creator_profile(self, creator_id: str) -> dict:
        """获取达人画像（粉丝/领域/合作报价等）。"""
        ...
