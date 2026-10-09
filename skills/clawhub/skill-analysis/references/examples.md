# 高级功能使用示例（v2.6.2）

> 本文档为 Skill Analysis 的高级功能提供**完整的命令 → 输出示例**，帮助理解
> 批量模式、SARIF/SBOM 导出、OSV 依赖查询、策略引擎、信任注册表、规则包、
> CI 门禁、watchdog 自动模式与发布自检的用法。基础用法见 `SKILL.md` 三、使用指南。

---

## 1. 快速上手：一条命令看懂判定

```bash
# 单 Skill 深度审计（Markdown 报告）
python scripts/analyze_skill.py ~/my-skill

# 关键输出（报告第 9 节）：
# ### 【最终判定】NEED_REVIEW（需人工复核）｜风险评分 62/100（需关注）
# - **综合评级**：🟠 **中高风险**：存在 P1 级危险模式……
# - **准入卡点**：NEED_REVIEW（需人工复核）

# 判定速查：PASS（可准入）/ REVIEW（建议关注）/ NEED_REVIEW（需人工复核）/ BLOCK（禁止准入）
#          ERROR（无法完成扫描——路径错误/缺 SKILL.md，会给出具体原因）
```

---

## 2. 批量扫描（Mode A）

```bash
# 扫描目录下所有含 SKILL.md 的技能，输出汇总表
python scripts/analyze_skill.py ~/skills-collection --dir
```

**输出示例**：

```
## 🔍 Skill 安全扫描结果

共扫描 3 个 Skill：

| # | Skill 名称 | 来源 | 检测结果 |
|---|-----------|------|---------|
| 1 | wallet-tracker | 本地 | 🔴 发现风险 |
| 2 | pdf-helper | 本地 | ⚠️ 需关注 |
| 3 | notes-organizer | 本地 | ✅ 未发现风险 |

**结论**：成功扫描 3 个，失败 0 个。全部扫描完成。
```

> v2.6.2 起：若有 Skill 扫描失败（如缺少 SKILL.md），会以 `❌ 扫描失败` 行显示，
> 并在结论中标注「成功 N 个，失败 M 个」——不再静默跳过。

```bash
# 批量 + JSON（结果数组，便于二次处理）
python scripts/analyze_skill.py ~/skills-collection --dir --json
```

---

## 3. SARIF 2.1.0 导出（与 CI 集成）

```bash
# 导出 SARIF（P0/P1→error，P2→warning，P3→note）
python scripts/analyze_skill.py ~/my-skill --sarif out.sarif

# 查看关键字段
python -c "import json; d=json.load(open('out.sarif')); print(d['runs'][0]['results'][0]['level'], d['runs'][0]['results'][0]['message']['text'][:60])"
# error 违反安全基线（P0/P1）
# warning 建议关注（P2）
```

---

## 4. SBOM 导出（CycloneDX 1.5 风格）

```bash
python scripts/analyze_skill.py ~/my-skill --sbom out.bom.json

# 内容概览：组件 + 文件级 SHA-256 + 能力/权限属性
python -c "import json; d=json.load(open('out.bom.json')); print(d['metadata']['component']['name'], len(d['components']))"
```

---

## 5. OSV 依赖漏洞查询（联网，默认关闭）

```bash
# 需要联网；失败自动降级为提示，不阻断
python scripts/analyze_skill.py ~/my-skill --osv

# 输出（若有依赖清单且检出已知漏洞）：
# - **OSV 依赖漏洞（--osv）**：
#   - **[P2] 依赖已知漏洞：requests 2.25.1（CVE-2023-xxxxx）**：……
```

> 离线替代：v2.6.1 起内置 `MCP_SDK_ADVISORIES` 公告表，扫描时会自动检查
> requirements.txt / package.json / Gemfile 中的 MCP SDK 版本（CVE-2026-52869 等），无需联网。

---

## 6. 策略引擎（standard / strict / paranoid）

```bash
# 查看默认策略
cat config/policy.json

# 使用 strict 策略（P1 也阻断）：
python scripts/analyze_skill.py ~/my-skill --policy config/policy.json
# 或在 config/policy.json 中把 "active" 改为 "strict"
```

**策略档位效果**：

| 档位 | block_at | review_at | 网络上传 |
|------|----------|-----------|----------|
| standard | P0 | P1 | warn |
| strict | P0、P1 | P2 | block |
| paranoid | P0、P1、P2 | P3 | block |

---

## 7. 信任注册表（白/黑名单）

```bash
# config/trust.json 示例
cat config/trust.json
# {
#   "whitelist": ["skill-analysis"],
#   "blacklist": ["known-bad-skill"],
#   "overrides": {"my-org-skill": "standard"}
# }

# 生效说明：白名单内的 Skill 直接 PASS；黑名单内的 Skill 直接 BLOCK；
# overrides 可按名称覆盖策略档位。改动后重新扫描即可生效。
```

---

## 8. 自定义规则包

```bash
# 用外部规则包目录覆盖内置规则（更新规则无需改引擎代码）
python scripts/analyze_skill.py ~/my-skill --rules-dir ~/my-rules

# 规则包结构（与内置 rules/ 同构）：
#   ~/my-rules/manifest.json   ← pack_version + 每个文件的 SHA-256
#   ~/my-rules/risk-rules.json ← 数据驱动规则
# 规则文件被篡改（SHA-256 校验失败）时自动回退内置默认规则

# 新增规则文件后重新生成 manifest：
python - <<'PY'
import hashlib, json, os
rules_dir = "~/my-rules"
files = {f: hashlib.sha256(open(os.path.join(rules_dir, f), 'rb').read()).hexdigest()
         for f in os.listdir(rules_dir) if f.endswith('.json') and f != 'manifest.json'}
json.dump({"pack_version": "1.0.0", "files": files},
          open(os.path.join(rules_dir, 'manifest.json'), 'w'), indent=2)
PY
```

---

## 9. CI 门禁（--exit-on）

```bash
# 命中 ≥ P1 时退出码 2（默认），0 = 通过
python scripts/analyze_skill.py ~/my-skill --exit-on P1; echo $?
# 2  → 存在 P0/P1 命中，CI 失败
# 0  → 通过

# 更严格：P0 即失败
python scripts/analyze_skill.py ~/my-skill --exit-on P0; echo $?
```

---

## 10. watchdog 自动模式（Agent 模式）

```bash
# 首次全量扫描（启动时）
python scripts/watchdog.py --check

# 安装新 Skill 后静默扫描
python scripts/watchdog.py --check ~/new-skill

# 安全状态报告
python scripts/watchdog.py --report
# 输出示例：
# Skill Analysis · 安全状态报告
#   已扫描 12 个 Skill：🔴 1  ⚠️ 2  ✅ 9
#   最近 30 天发现 3 个风险事件

# 后台轮询（每日一次）
python scripts/watchdog.py --daemon --interval 86400

# 日志：~/.workbuddy/skills/skill-analysis/logs/scan_YYYY-MM.log（30 天轮转）
# 事件：SCAN_START/END、SKILL_SCANNED、FINDING、SKILL_ADDED/MODIFIED/REMOVED、UPDATE_POISONING、ALERT/QUARANTINE
```

---

## 11. 发布前自检（selfcheck）

```bash
python scripts/selfcheck.py
# 输出示例：
# Skill Analysis 回归自检
#   [PASS] 自扫描零误报：自扫描 PASS（可准入），score 100
#   [PASS] 恶意样例命中：恶意样例 BLOCK，P0 命中 4 条
#   [PASS] 版本一致性：版本一致 v2.6.2
# 结论：✅ 全部通过，可发布

# 可选：加载包外对抗基准库，量化检出率/误报率
python scripts/selfcheck.py --corpus ~/benchmark-corpus
```

---

## 12. 典型判定解读

| 场景 | 预期判定 | 处理建议 |
|------|----------|----------|
| 简单工具类 Skill，无危险模式 | PASS | 可直接使用 |
| Skill 含运行时安装依赖（pip install） | REVIEW | 确认安装行为符合预期 |
| Skill 含提示注入特征 / PyArmor 混淆 | NEED_REVIEW | 查看命中明细，确认意图 |
| Skill 含反向 Shell / 恶意 IOC / 混淆载荷 | BLOCK | 禁止使用，隔离复核 |
| 路径错误 / 缺 SKILL.md | ERROR | 按提示修正路径或目录结构 |
