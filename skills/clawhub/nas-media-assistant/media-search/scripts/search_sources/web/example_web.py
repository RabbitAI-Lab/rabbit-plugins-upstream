#!/usr/bin/env python3
"""示例网页源 fetcher（瘦：只抓原始文本，不做信息提取）。

接入真实站点时替换抓取逻辑。设计原则：网页抓取是脆弱外围，标题解析是稳定核心。
fetcher 只负责把页面上的标题串 + 链接抓下来，**不做任何信息提取**（年份/分辨率/
编码/音轨/字幕/大小/低质判定等全由 title_parser.py 在聚合层统一解析）。

统一接口: parse(query, source_cfg) -> [候选 dict]
- query: {title, type, year, quality}
- source_cfg: 该源在 config.json 中的配置块
候选只装网页能直接拿到的原始字段，用 common.build_candidate() 拼装。

新增网页源 = 复制本文件改名 + 实现 parse（只抓标题串+链接）+ config.json 注册一行。
信息提取零代码：标题解析逻辑全在 title_parser.py，与具体网站无关。
"""


def parse(query, source_cfg):
    """接入真实站点时实现以下步骤:
    1. 构造搜索URL: source_cfg["search_url"].format(q=query["title"])
    2. 抓取页面: make_session()/fetch_html() 或 WebFetch(代理友好)
    3. 解析结果列表: CSS Selector / XPath / 正则，**只取标题串 + 链接 + 可选大小/做种**
    4. 用 build_candidate(title=标题串, url=链接, source_cfg=source_cfg, link_type=...) 拼装
    """
    # TODO: 接入真实站点
    return []
