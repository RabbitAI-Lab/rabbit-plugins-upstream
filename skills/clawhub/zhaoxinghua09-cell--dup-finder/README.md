# 重复文件查找器 / Duplicate File Finder

[![LGD](https://img.shields.io/badge/LGD-Governance-blue)](https://github.com/zhaoxinghua09-cell/lgd-theory)

> `dup-finder` v1.0.5 · LGD-Powered Utility Family · Zero-dependency

## English

Downloads and photo folders piled high with same-name copies, eating several GB with no idea where to start — one command solves it. Three-level hashing (size → first block → full SHA1) finds real duplicates; report-only by default, `--apply` deletes extras keeping the first; `--json` for machines. rc=0 ok / rc=1 findings / rc=2 usage.

### Usage
```bash
python scripts/dup_finder.py --help
python scripts/dup_finder.py -r -d <dir>          # preview only
python scripts/dup_finder.py -r -d <dir> --apply  # delete extras
```

### Disclaimer
Efficiency aid only — back up important data before `--apply`.

## 中文

下载夹/相册里同名副本堆成山，占几个 G 不知道从哪清——一条命令搞定；三级哈希（大小→首块→全量 SHA1）找真重复；默认 dry-run 预览、`--apply` 才删多余保留首个、`--json` 机器可读；成功 rc=0 / 发现问题 rc=1 / 用法错误 rc=2。

### 用法
```bash
python scripts/dup_finder.py --help
python scripts/dup_finder.py -r -d <目录>          # 仅预览报告
python scripts/dup_finder.py -r -d <目录> --apply  # 删除多余副本
```

### 免责
效率辅助，`--apply` 前请备份重要数据。

---

## License & attribution
**分层许可（务必并读；代码许可不覆盖文档与理论文本）**

- **代码**（本包 `.py` 文件）：**MIT**
- **本 `README.md` / `SKILL.md` 及其中的理论文本、方法论与一切理论表述**：**不在 MIT 覆盖范围内**，保留所有权利（All rights reserved）

```
© 2026 SynomosAI · China. All rights reserved.
理论署名 (attribution) : LGD（Lifecycle Governance Doctrine / 全程治理论）— SynomosAI initiative
名称状态 (name status)  : "SynomosAI" — 未申请实体注册、未申请商标注册
                        (not a registered legal entity; no trademark registered)
生产参考部署 (production reference, self-reported) : 无（未声明外部生产参考部署）
                    ← 非认证、非背书、非监管认可（not a certification or endorsement）
代码许可 (code license) : 本包未附 LICENSE 文件（许可待定）
                    本文本与理论表述不在任何代码许可覆盖范围内
引用格式 (cite as)      : 本资产无 DOI
```
（上列为《LGD 对外表述规范》§3.2 统一块，**整体复制、未删改**；发布/重提前须照最新版本复核。）
