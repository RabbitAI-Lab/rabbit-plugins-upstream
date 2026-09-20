# CHANGELOG

## v2.4.2（2026-09-20）

- 派生为标准免费版（基于 v2.4.0）
- 锁定三个脚本入口：`confirm_gate.py`（全部子命令）、`environment_snapshot.py`（采集入口）、`desensitize.py`（`--share`）
- 锁法统一：`print("🚫 完整版功能：X。获取完整版：https://wzyp.cn/item/p0r2lb")` + `sys.exit(1)`
- SKILL.md 重写：仅保留 L1/L2 备份/校验/还原主流程，完整版能力简介 + 付费引导
- README.md 重写：免费版定位 + 快速开始 + 与市场同类差异
- 新增 `readme1.md`：付费转化页（完整版能力 + 链动链接）
- 新增 `_meta.json`：项目元数据与文件校验
- 新增 `lock_guide.md`：锁口引导文案
- LICENSE 保持不变（MIT）

---

## v2.4.0（2026-09-18）

- 整合 v2.3.0（五道闸门）与 v2.2.1（测评修复）
- 六脚本统一版本号 `2.4.0`，全部支持自报版本
- 平台边界修复：Python ≥3.8、macOS/Ubuntu 测试通过
- 六脚本全量用例 23 组通过（含 3 组一致性断言）

## v2.3.0（2026-09-15）

- 新增 `confirm_gate.py`：五道分步确认闸门（G1-G5）
- 备份默认落位改桌面
- 环境快照新增 `source_model`

## v2.2.1（2026-09-16）

- 修复 F9 中文紧邻脱敏失效
- 修复脱敏误为迁移必经步骤
- 新增 `_environment.json` + `environment_snapshot.py`
- 新增 `preflight_check.py` 入口校验

## v2.1.0（2026-09-08）

- 人格层按迁移模式恢复（persona-follow/keep）
- 新增工具与环境层（L5）
- 新增凭据管理（credentials）

## v1.0.1（2026-09-01）

- 初始版本：raw JSONL 备份 + schema/seq 校验 + 可读还原
