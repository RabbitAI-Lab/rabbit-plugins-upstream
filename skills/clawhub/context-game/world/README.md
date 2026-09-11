# 《上下文》世界库总览

`skill/world/` 是《上下文》游戏的所有世界定义。当前共 **1 个官方世界 + 8 个题材世界**，每个题材世界提供三层文件（骨架 / 精写 / GDD），可任选一层开局。

---

## 文件清单

| 题材 | tone_family | 骨架 JSON | 精写 JSON | GDD 文档 |
|---|---|---|---|---|
| 官方 · 硬科幻政治惊悚 | `hard-sci-fi-political-thriller` | — | `official-world.json`（《双陆纪元》v2） | — |
| 现代都市 | `modern-urban` | `modern-urban.json` | `modern-urban-detailed.json`（《明珠湾区》） | `modern-urban-gdd.md` |
| 军事 | `military` | `military.json` | `military-detailed.json`（《逐鹿大陆》） | `military-gdd.md` |
| 悬疑 | `mystery` | `mystery.json` | `mystery-detailed.json` | `mystery-gdd.md` |
| 商战 | `corporate-war` | `corporate-war.json` | `corporate-war-detailed.json` | `corporate-war-gdd.md` |
| 校园 | `campus` | `campus.json` | `campus-detailed.json`（《东岸学潮》） | `campus-gdd.md` |
| 情感 | `romance` | `romance.json` | `romance-detailed.json`（《锦城情局》） | `romance-gdd.md` |
| 穿越 | `isekai` | `isekai.json` | `isekai-detailed.json`（《双轨异界》） | `isekai-gdd.md` |
| 修仙 | `cultivation` | `cultivation.json` | `cultivation-detailed.json` | `cultivation-gdd.md` |

配套基础设施：
- `world-gen-protocol.md` — 自定义世界生成协议（含 9 个 tone_family、势力语义漂移表、8 条自洽清单、命名合规护栏）
- `world-gen-protocol.md.bak` — 协议改造前的备份

---

## 三层文件定位

| 层 | 文件 | 用途 | 密度 |
|---|---|---|---|
| **骨架** | `<topic>.json` | 仅 5 顶层字段（meta/continents/nations/neutral_port/faction_matrix），运行时可直接开局，agent 现场补 NPC/地点/历史 | 50-80 行 |
| **精写** | `<topic>-detailed.json` | 扩展 core_npcs / key_locations / history / world_tech / opening_situation 五类增强字段，与官方世界《双陆纪元》同密度 | 330-380 行 |
| **GDD** | `<topic>-gdd.md` | 设计文档：题材定位、参考作品点名、8 方势力与关系张力机器映射、玩家胜利通道、与官方世界对照表、8 条自洽清单自查报告 | 200-500 行 |

推荐开局时**直接用精写版**（用 `python scripts/save.py world-init --slot <槽位> --payload world/<topic>-detailed.json`）；骨架版只用于快速试跑或让 agent 生成变体。

---

## 跨题材一致性核查（阶段三验证结果）

所有 9 个世界（含官方）均满足以下硬性指标：

| 指标 | 要求 | 实测 |
|---|---|---|
| nation 数 | 4-6 | 全部 5 |
| faction_matrix pair 数 | 15（5 势力 + 1 中立港的完全图） | 全部 15 |
| relation 值两两互不相同 | 强制 | 全部通过（save.py 硬约束） |
| NPC 数（精写版） | 12-15 | 13-15 |
| ≤ -50 结构性敌意对 | ≥ 2 | 全部满足（2-3 对） |
| ≥ 50 表面同盟藏裂缝 | ≥ 1 | 全部满足（1-4 对） |
| tension_seeds 可追溯 | 8 条自洽清单 #3 | 全部 PASS |
| 命名与官方世界零重名 | 强制 | 全部通过 |

---

## 势力语义漂移（题材特色）

《上下文》的核心是**关系张力机器**（多方势力互算 + 结构性敌意 + 表面同盟藏裂缝 + 中立交汇点）。机器骨架不变，但"势力"的语义在题材间漂移：

| 题材 | 势力是什么 | 中立交汇点是什么 |
|---|---|---|
| 官方（硬科幻） | 国家 / 军政府 / 城邦 | 免税深水港（灰潮港） |
| 现代都市 | 财团 / 资本 / 媒体 / 军方承包商 / 市政 | 中间人 / 独立调查者 |
| 军事 | 国家 / 军政派系 / 雇佣兵团 / 情报机构 / 南方联盟 | 中立缓冲带（银湾） |
| 悬疑 | 官方调查组 / 民间侦探 / 嫌疑人方 / 掩护势力 / 真相持有者 | 医院 / 殡仪馆 / 独立记者 |
| 商战 | 敌对公司 / 友商联盟 / 投行 / 律所 / 家族企业 | 董事会 / 收购中介 / 反垄断局 |
| 校园 | 学生会 / 教师派系 / 社团联盟 / **校外势力** / 学生小团体 | 图书馆 / 匿名树洞 / 校外咖啡馆 |
| 情感 | 女方家族 / 男方家族 / 前段关系网 / 现段关系网 / 闺蜜兄弟圈 | 心理咨询 / 婚礼场地 / 共同友人 |
| 穿越 | **原时空派系 + 新时空派系**（双 matrix 共存一文件） | 两界渡（裂隙观测站） |
| 修仙 | 宗门 / 皇朝 / 秘境主 / 散修联盟 / 魔道 | 坊市 / 拍卖会 / 秘境入口 |

---

## 与官方世界《双陆纪元》的对照

- **矩阵密度**：全部 5×15，完全对齐
- **NPC 数**：官方 14，8 个题材 13-15，量级一致
- **tension_seeds 数量**：全部每国 2-3 条
- **增强字段**：官方 5 类扩展（core_npcs / key_locations / history / world_tech / opening_situation），8 个精写题材全部照做
- **命名风格**：官方音译（卡萨德/麟河/奥斯特），8 题材各自风格化（都市用场景派生、军事用硬核现代、校园用场景词、情感用姓氏、穿越双时空对比、修仙全古风音译）

---

## 使用流程

```bash
cd E:\SyncFiles\DreamWord\skill

# 1. 选题材开局（例如修仙精写）
python scripts/save.py init --slot my_xiuxian --mode custom
python scripts/save.py world-init --slot my_xiuxian --payload world/cultivation-detailed.json

# 2. 进入游戏：对 agent 说"开始游戏"
#    agent 会读取 SKILL.md，从 saves/my_xiuxian/world.json 加载世界
#    然后按 SKILL.md 开局流程问你选身份（旅人/本地人/空白身世）

# 3. 回合循环：自由文本行动 → agent 解析 → 掷骰 → 写回
```

---

## 已知的跨题材命名重叠

- **"北岭"跨 3 个题材**（现代都市=北岭资本 / 军事=北岭联邦 / 穿越=北岭集团）——但三者是**不同题材的不同实体**，跨世界"名字即契约"规则不冲突（契约只在单个 world.json 内有效）。若你希望进一步彻底区隔，可将现代都市的"北岭资本"改名（如"鼎丰资本"），我可即时重做该文件并重跑校验。
