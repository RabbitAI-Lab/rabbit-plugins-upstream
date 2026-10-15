# 规则包与配置维护指南（v2.5.3）

本文件仅供 **Skill 维护者**使用：说明如何更新防御规则（无需改动引擎代码）、如何配置策略与信任注册表。

## 一、规则包结构

- 检测规则存放于 `rules/*.json`，按检测家族组织（每个家族一个文件）。
- `rules/manifest.json` 登记 `pack_version` 与每个规则文件的 SHA-256，引擎加载时校验：
  校验失败的文件**自动回退内置默认规则**，绝不使用被篡改的规则。
- 支持 `--rules-dir <dir>` 或环境变量 `SKAUDIT_RULES_DIR` 指定外部规则包（用于共享/版本化）。

## 二、规则文件 Schema

通用格式（列表型家族）：

```json
{
  "family": "risk",
  "version": 1,
  "rules": [
    {"id": "risk-00", "sev": "P0", "label": "示例标签",
     "why": "示例原因", "re": "正则表达式"}
  ]
}
```

- `re`：Python `re` 语法正则字符串（`re.I` 忽略大小写由引擎统一启用；`\s` 等按 JSON 转义）。
- `sev`：`P0` / `P1` / `P2` / `P3`；`label` / `why`：命中展示与原因。
- 单正则家族：`{"family": "...", "re": "..."}`；`ioc` 家族：`{"ips": [...], "domains": [...]}`；
  名称比对家族：`{"names": [...]}`；能力画像家族：`{"rules": [{"id","label","re"}]}`。
- 污点分析家族（`taint.json`，v2.5.3）：`{"sources": [{"id","label","re"}], "sinks": [{"id","label","re"}]}`，
  分别定义敏感源与外传汇点；同一语句/管道链内源+汇同时出现即组合命中。

**新增/修改规则流程**：
1. 编辑对应 JSON（保持 Schema 不变）；
2. 重新生成 `manifest.json`（见第三节）；
3. 跑回归：`python scripts/selfcheck.py`（自扫零误报 + 恶意样例命中 + 版本一致性，三项全 PASS 才可发布）。

## 三、manifest 重生成

```python
import hashlib, json
from pathlib import Path
rules = Path("rules")
manifest = {"pack_version": "2.5.3", "files": {}}
for f in sorted(rules.glob("*.json")):
    if f.name == "manifest.json":
        continue
    manifest["files"][f.name] = hashlib.sha256(f.read_bytes()).hexdigest()
(rules / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
```

> 注意：每改一个规则文件都必须同步更新 manifest，否则该文件会因校验失败而回退内置默认规则（这是安全设计，不是 bug）。

## 四、策略引擎（config/policy.json）

```json
{
  "pack_version": "2.5.3",
  "active": "standard",
  "profiles": {
    "standard": {"block_at": ["P0"], "review_at": ["P1"], "network_upload": "warn"},
    "strict":   {"block_at": ["P0", "P1"], "review_at": ["P2"], "network_upload": "block"},
    "paranoid": {"block_at": ["P0", "P1", "P2"], "review_at": ["P3"], "network_upload": "block"}
  }
}
```

- `block_at`：命中这些严重度 → 准入 BLOCK（CI 退出码 2 的默认依据）。
- `review_at`：命中 → NEED_REVIEW。
- `network_upload`：`warn`（仅提示）/ `block`（检出数据外传即 BLOCK）。
- 切换档位：改 `active`，或 `--policy <file>` 指定外部配置（不改包内默认）。

## 五、信任注册表（config/trust.json）

```json
{
  "pack_version": "2.5.3",
  "allowlist": ["my-trusted-skill"],
  "denylist": ["evil-skill"],
  "overrides": {"some-skill": "strict"}
}
```

- `denylist`：命中名称直接 BLOCK（无论扫描结果）。
- `allowlist`：无 block/review 级命中时标注"来源已列入信任白名单"。
- `overrides`：按 Skill 名覆盖其策略档位（名称不区分大小写）。

## 六、维护 SOP（定期更新防御规则）

1. **情报刷新**：定期跟踪权威威胁情报（框架/漏洞/供应链/威胁研究等渠道，来源自选、记录日期与编号以便溯源）。
2. **更新规则包**：新手法 → 编辑对应 JSON；新恶意指标 → 更新 ioc 家族。
3. **重生成 manifest**（第三节）。
4. **回归（必做）**：`python scripts/selfcheck.py` 三项全 PASS；`--exit-on P1` 对恶意样例退出码为 2；
   可选 `--corpus <基准库目录>` 量化检出率/误报率（语料库置于包外，不打进包）。
5. **版本与文档同步**：版本号在 `SKILL.md` frontmatter + 标题 + `CHANGELOG.md` 顶部 + `rules/manifest.json` + `config/*.json` + 引擎 docstring 一致（grep 旧版本号排查）；更新日志只写入 `CHANGELOG.md`。
6. **重打包**：保留 `skill-analysis/` 根前缀，排除 `__pycache__`，`testzip()` 通过。
