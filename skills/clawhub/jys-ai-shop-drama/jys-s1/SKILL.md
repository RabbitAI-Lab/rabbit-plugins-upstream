---
name: jys-s1
description: |
  执行JYS的S1选套路与数据库入库：选择或推荐内核与变体，解析用户上传的新剧本并同步归档剧本及产品，或单独维护产品数据库。默认由$jys主控调度；仅当用户明确调用$jys-s1或JYS状态的next_skill为jys-s1时直接使用。普通“制作带货短剧”请求交给$jys。
---

# S1 选套路

## 调用与共享契约

- 开始前完整读取 [../jys/references/workspace-contract.md](../jys/references/workspace-contract.md)。
- 默认由 `jys` 主控调度；用户明确调用 `$jys-s1` 或状态中的 `next_skill` 为 `jys-s1` 时可直接执行。
- 直接执行也必须绑定同一 `JYS_WORKSPACE`、读取或迁移 `status.md`，不得另建临时项目状态。
- 每轮结束前更新当前/下一 Skill 和动作，并按共享契约输出默认下一步尾注。

## 职责

确定本项目使用的套路内核和变体；负责共享数据库中的剧本与产品入库。不要执行S2替换或S4写作。

## 输入与输出

- 输入：用户的套路需求、上传的新剧本或新产品资料。
- 数据库：`../jys/assets/kernels/`、`../jys/assets/products/`。
- 输出：已确认的内核名称、内核完整内容和变体。
- 完成后：写入 `JYS_WORKSPACE/status.md` 的S1区域，并将 `s1` 标记为 `confirmed`。

若直接调用S1选择项目套路，先按JYS的项目绑定规则确定 `JYS_WORKSPACE`。只执行共享数据库入库维护时，不需要创建项目工作区，也不更新项目S1状态。

## 流程

### 使用已有内核

1. 读取内核索引。
2. 用户有明确方向时，展示候选内核：内核名、简介、变体数、剧本数。
3. 用户没有方向时，读取各内核定义文件并展示变体；需要比较或排序时，只使用关联剧本的参考价值（优 > 良 > 中 > 差）。
4. 用户选中内核后，展示其全部变体：变体名、一句话概括、核心剧情段落；不要展示剧本文件名。
5. 用户确认内核和变体。

### 处理上传的新剧本

1. 读取 [references/raw-script-parser.md](references/raw-script-parser.md)，将原始台词解析为结构化大纲。
2. 与已有内核比较；由用户决定复用已有内核还是创建新内核。
3. 写库前读取 [../jys/references/db-write-guide.md](../jys/references/db-write-guide.md)，先创建单份 `.bak` 回滚副本；需要新命名或改名时同时读取 [../jys/references/naming-guide.md](../jys/references/naming-guide.md)。
4. 相似版本只看主要人物设定与关系、核心结构拆解；产品不同不影响判定。
5. 判为相似版本时合并，不新建重复剧本；保留参考价值更高的主文件并记录差异。参考价值相同时沿用已有主文件。
6. 先将剧本完整写入内核数据库并校验可读，再原子更新内核索引，最后更新 `../jys/assets/library-version.json`。
7. 剧本含带货产品时，读取 [references/产品录入规范.md](references/产品录入规范.md)，检查黑名单并完成产品查重、创建或补充；黑名单产品跳过产品入库，但剧本照常归档。
8. 用户确认最终内核和变体。

### 维护产品数据库

1. 用户单独上传或要求录入产品时，读取 [references/产品录入规范.md](references/产品录入规范.md) 和 [../jys/references/naming-guide.md](../jys/references/naming-guide.md)。
2. 检查黑名单和现有产品，缺少不可变产品事实时向用户索取，不得编造。
3. 用户确认后先创建或补充 product 文件并校验可读；新建产品时再原子更新 `../jys/assets/products/index.md`，最后更新 `../jys/assets/library-version.json`。
4. 此流程只维护共享数据库，不代表当前项目已经完成S1选套路或S3选产品。

## 交互规则

- 宽泛描述必须列出候选项，不能直接确定。
- 参考价值是剧本选取、推荐和主版本判断的唯一指标；不得使用其他指标。
- 是否复用旧内核或创建新内核，由用户最终决定。
- 剧本入库与产品入库必须在同一次S1流程中完成；不得只归档剧本而遗漏其非黑名单产品。
- 数据库写入前必须按数据库写入指南建立 `.bak` 回滚副本；先写内容文件，再更新索引和数据库版本，任一步失败时保留原文件并报告。
- 产品查重按产品本质归类，忽略品牌、营销名称和机器识别差异；同类产品只保留一个product文件。
- 用户确认前不要更新S1完成状态。
- 用户确认前将 `s1` 保持为 `in_progress`，并把 `next_skill` 保持为 `jys-s1`；确认后按共享契约决定进入S2或S3。

## 资源索引

- 原始剧本解析：[references/raw-script-parser.md](references/raw-script-parser.md)，收到新剧本时读取。
- 数据库写入：[../jys/references/db-write-guide.md](../jys/references/db-write-guide.md)，查重或写库前读取。
- 产品录入：[references/产品录入规范.md](references/产品录入规范.md)，剧本含产品或用户要求维护产品库时读取。
- 命名规范：[../jys/references/naming-guide.md](../jys/references/naming-guide.md)，创建或修改内核、变体、剧本名称前读取。
