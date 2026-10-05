# 子项目登记（SUBPROJECTS）

本仓库是「小说连载工程」的技能仓库（方法论 + 共用脚本）。具体小说作品以**独立子项目**形式存在：
每个子项目保留自己的 git 仓库与远端，独立提交、独立发布；共用能力（脚本）统一取自本仓库 `scripts/`。

## 关系约定

| 项 | 约定 |
|---|---|
| 独立性 | 子项目有独立 `.git` 与远端，不并入本仓库的工作树（不搞 submodule，避免双向绑定） |
| 物理位置 | 子项目可位于任意目录，无需放进本仓库目录树 |
| 脚本来源 | 一律调用本仓库 `scripts/`（见 `scripts/README.md`），子项目内**不再建 `tools/`** |
| 项目根判定 | 以子项目根目录为工作目录执行脚本；不在根目录时用 `--root` 指定 |
| 文档口径 | 子项目的 `CONTRIBUTING` / `STYLE-GUIDE` 等只写调用方式，不复制脚本本体 |

## 子项目清单

| 子项目 | 位置 | 远端 | 状态 | 使用脚本 |
|---|---|---|---|---|
| **《奉天1928》** `-1928` | `C:\Users\Admin\-1928` | `https://github.com/JohnSmithfan/-1928.git` | 进行中：第一卷 55 章，正文约 22.3 万字 | `humanizer_check.py`、`_list_hits.py`、`_promote_draft.py`、`_sync_draft.py`、`review_all.py`、`review_scale.py`、`review_continuity.py`、`review_rationality.py`、`review_punctuation.py` |

### 《奉天1928》（`-1928`）

- **题材**：民国东北架空历史（1928—1955），全书规划 5 卷 1000 章。
- **目录约定**（子项目自定义，与通用 `ch-001-title.md` 不同）：
  - 正文定稿：`chapters/{第X卷 卷名}/{第Y幕 幕名}/第NNN章 四字标题.md`
  - 草稿：`notes-personal/{对象}草稿.md`（平铺单文件，不分子目录）
  - 设定：`worldbuilding/`；角色：`characters/`；幕讨论：`issues/`；报告：`.workbuddy/reports/`
- **改动顺序（强制）**：先改 `notes-personal/` 草稿 → `humanizer_check.py` 自审 → 归档审核报告 → 审核 PASS → `_promote_draft.py <章号>` 同步 `chapters/` 定稿 → 记 `CHANGELOG.md` / `progress.md`。反向 `_sync_draft.py` 仅勘误用。
- **脚本迁移记录（2026-09-27）**：原 `-1928/tools/` 4 个脚本迁入本仓库 `scripts/`，子项目 `tools/` 目录删除；`_promote_draft.py` 改为以当前工作目录为项目根（新增 `--root`），humanizer 按脚本自身目录定位。
- **审稿脚本（2026-09-27 新增）**：`review_all.py`（综合，一次跑完全部门禁）+ 四个单维度脚本（规模／一致性／合理化／标点），共用 `_review_lib.py`；命名兼容通用 `ch-001-title.md` 与本子项目 `第NNN章 标题.md`，支持 `--draft` 直审草稿。送审前跑 `review_all.py`，FAIL 未清零不得 promote。

## 新增子项目

1. 建独立 git 仓库并配置远端；
2. 在上表追加一行（位置／远端／状态／使用脚本）；
3. 在子项目 `CONTRIBUTING.md` 写明脚本调用方式（相对本仓库 `scripts/` 的路径）；
4. 需要新脚本时加在本仓库 `scripts/` 并更新 `scripts/README.md`。
