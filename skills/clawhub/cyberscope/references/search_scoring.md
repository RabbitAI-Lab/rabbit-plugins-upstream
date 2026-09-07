# 搜索评分算法（供参考 · 定性）

> 目的：确定性、可文档化、全整数运算（无浮点/随机）。实现见 `cyberscope.py`
> `score_method()`；自检 G2 锚定关键数值。

## 归一化（查询与字段同一函数）

小写；`-` `_` `&` 视为空格；空白折叠为单空格。
→ "Living-Off-the-Land" = "living off the land"；"DDoS" = "ddos"。
边界：符号折叠仅限 ASCII 的 `-` `_` `&`；全角符号（如 `＋` `·`）**不折叠**——此类词需按原文匹配。
空白折叠基于 Python 正则 `\s`（Unicode-aware）：全角空格 `　` **会**被折叠为普通空格。

## 分词与匹配语义

- 查询 = 归一化后按空白切分的 token 列表；匹配 = **token 是字段归一化文本的子串**。
- 多词查询免引号：`search dns poisoning` 等价于 `search "dns poisoning"`（位置参数 nargs=+，空格连接）。
- **AND 语义**：方法命中当且仅当**每个** token 在
  {title, keywords, description, resources.title, resources.description} 的并集中至少命中一次
  （同一 token 可在不同字段各命中一次并累加）。
- 0 token（空查询）→ 退出码 2。

## 权重（每 token 每字段至多一次）

| 字段 | 权重 |
|---|---|
| title | 1000 |
| keywords（连接后整体） | 500 |
| description | 200 |
| resources.title（全部资源连接） | 100 |
| resources.description（全部资源连接） | 50 |

**短语加分**（一次性）：整串查询（token 空格连接）出现在 title → +500；
出现在任一资源 title（连接文本）→ +100。（两个条件可同时满足。）

## 排序与输出

- score 降序；**平局按 methodNumber 升序**（确定性，自检以属性测试锁定）。
- 默认 `--fields basic`：`id,title,category,category_name,score`（token 经济）；
  `--fields all` 追加 `description,keywords,resources`。
- `--category SLUG` 先过滤再评分；`--limit` 1..62（默认 10）。
- 0 命中：`results: []`、rc 0（有效响应，非错误）。

## 锚定样例（selftest G2）

| 查询 | 结果 |
|---|---|
| `ransomware` | m50 = 2450（title+kw+desc+res_title+res_desc+短语×2）、m27 = 700 |
| `solarwinds` | 仅 m13（只存在于 keywords；v1 搜索会漏） |
| `living off the land` | top1 = m17（三 token AND + 短语） |
| `vpn --category censorship-control` | [m36, m35] |
| `zzzqqqxx` | 0 命中，rc 0 |
