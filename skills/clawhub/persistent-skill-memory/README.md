# persistent-skill-memory v2.0.0

把"已安装技能集合"变成**确定性、幂等、最小 token** 的索引，注入 agent 系统提示——任意模型零额外加载即可看见可用技能，索引漂移可机器校验。

v1 两大缺陷（本包为何全部可执行）：
1. v1 文档引用了两个**包内不存在的脚本**，整包零可执行文件——模型照文档执行必失败（幻觉源 #1）。
2. "每域截断 10 条"与记忆目的相悖（记忆工具截断 = 记忆失真）。

v2 附带全部被引用的脚本（一个 stdlib-only CLI + 自检），截断由"每域一行"的紧凑性取代。

## 快速开始

```bash
S=scripts/skill_memory.py
python3 $S index  --root /path/to/skills                        # 看分类（stdout 单行 JSON）
python3 $S prompt  --root /path/to/skills                       # 看将注入的块
python3 $S inject  --root /path/to/skills --prompt-file PROMPT.md   # 幂等注入（双跑字节不变）
python3 $S verify --root /path/to/skills --prompt-file PROMPT.md    # rc0 干净 / rc3 漂移
python3 $S stats  --root /path/to/skills --prompt-file PROMPT.md    # token 预算
python3 $S hook   --root /path/to/skills --prompt-file PROMPT.md \
                 --out skill_add.sh                             # 安装后自动三步
python3 scripts/selftest.py                                      # 交付前必须 100% PASS
```

退出码：0 成功 · 2 用法/IO/标记异常 · 3 仅 verify 漂移。错误一律 stderr JSON `{tool,error,hint}`。

## v1 → v2 变更摘要

| 项 | v1.0.6 | v2.0.0 |
| --- | --- | --- |
| 可执行 | 0（文档引用不存在的脚本） | `skill_memory.py`（6 子命令）+ `selftest.py` |
| 注入 | 无实现（"手动"描述） | 标记块幂等注入；半开/多对/倒序 → rc2 不自动修 |
| 截断 | 每域 10 条 | 无（预算靠每域一行紧凑性，`stats` 可查） |
| 分类 | 未定义 | 固定 10 域优先级表，first-match-wins |
| 校验 | 无 | `verify` rc0/3 + `hook` 包装器 |
| 自检 | 无 | 全合成 9 夹具，stdlib-only，离线 |
| README | 逐字复述 SKILL.md（~4KB 冗余） | 精简版，无复述 |

## 文档入口

`SKILL.md`（命令契约 + 设计决策 + 加载地图）；解析/分类/注入细则在 `references/*.md`（各标"供参考"，按需加载）。

## 发布完整性

- **TREE-SHA256-v1（7 文件，排除 README.md 以破 hash-in-file 循环）：`3ab256c7a8d41495d26048ede89a8d43ae12c71ae4a8bda5a8b6c831529b294a`**
  算法：对每文件 entry=`<relpath>|<sha256(bytes)>`，按 entry 字典序排序后以 `\n` 连接整体 sha256；
  排除 readme.md/skill-card.md/_meta.json/.published/.DS_Store 与 .git/.clawhub/__pycache__/.pytest_cache
  （构建目录与现场安装目录同算法可比；与仓库其它 skill 同一约定）。
- 自检：`python3 scripts/selftest.py` → **67/67 PASS**（离线、确定性、全合成数据）。
