---
name: code-review
description: |
  代码审查助手。对 diff/PR/单文件做结构化审查：正确性、安全性（注入/越权/密钥）、性能、可读性、测试覆盖，按严重度分级并给出可落地修改建议。当用户需要"帮我 review 代码""检查这段有什么问题""看看这个 PR"时调用。
agent_created: true
visibility: "public"
---

# 代码审查助手

对代码变更做有结构的审查，输出分级问题 + 可落地修复建议。核心：**问题带严重度与定位，建议具体到行**。

## 审查维度
- **正确性**：空指针/越界/边界/并发/异常处理缺失
- **安全**：SQL 注入、命令注入、XSS、越权、硬编码密钥/令牌
- **性能**：N+1、不必要拷贝、阻塞调用、内存泄漏风险
- **可读/ maintain**：命名、函数过长、重复代码、魔法值
- **测试**：关键路径是否可测、缺边界用例

## 严重度分级
- 🔴 Blocker：上线前必须修（安全漏洞、必崩）
- 🟠 Major：应修（明显正确性或性能问题）
- 🟡 Minor：建议（可读性/风格）
- 🟢 Nit：可选

## 标准工作流
使用 `scripts/review_checklist.py` 对单个文件做静态 checklist 预检（命名/长度/密钥/异常）：
```bash
python scripts/review_checklist.py path/to/file.py --json
```
输出：各项命中清单（密钥字符串、超长函数、裸 except、TODO/FIXME 等）。
随后由 agent 结合 diff 上下文做语义级审查，给出分级建议。

## 质量门禁
- [ ] 是否区分"必须改"与"建议改"
- [ ] 安全类问题是否优先标注
- [ ] 建议是否具体到文件:行

## 自进化学习系统
```bash
python scripts/learner.py record . --capability "代码审查" [--fail --error <类型> --note <说明>]
python scripts/learner.py insight .
python scripts/learner.py reflect .
```
- 某类问题反复漏报 → 记录，reflect 建议扩充 checklist
- 用户关注的语言 → `prefer` 记录

## 安全边界
- 审查只读用户指定代码，不把代码内容外传第三方
- 密钥类命中只提示"存在硬编码凭据"，不打印其值
