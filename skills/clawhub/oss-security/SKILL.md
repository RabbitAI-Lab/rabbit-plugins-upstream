---
name: oss-security
description: 腾讯开源仓安全审计惯例（298 仓结构层 + 12 仓语料实测蒸馏）——SECURITY.md 家族化行为（7.4% 少数派）、安全漏洞分类路由（R11 流程兜底）、四禁公开面（Issue/评论/Commit/测试名禁载荷）、检测分层（ocr 确定性优先）、依赖响应（dependabot 单选）。触发词：安全审计、漏洞报告、安全披露、SECURITY.md、依赖漏洞、CVE、安全合规、oss security。不用于：许可证法律意见、渗透测试执行。
metadata:
  openclaw:
    requires:
      bins: [git]
---

## §0 场景闸门

本 skill 是被调度成员，不是场景入口。若当前任务会写 GitHub（提 PR / 评论 issue / commit / push / 建仓）且 .oss-task/ 下无 CHECKLIST.md：**先停下**，加载 routing/oss-workflow 按 §1 识别场景并实例化清单，再继续执行本 skill 对应步骤。无清单裸奔 = 违规交付（#752 实战：T1 裸奔 320s 被作者中止，61% 时间损耗）。运行时另有 penguin-guard 硬闸（PreToolUse）拦截无清单的 gh/git push 类命令。

# oss-security：安全审计惯例

## 0. 定位

- 腾讯仓安全惯例蒸馏：**skill 管分类路由与披露流程，ocr 管行级缺陷检测**（零降级分层）。
- 语料：298 仓 SECURITY.md 存在性 + dependabot/codeql 配置（repo-index.tsv 现场复算）+ 12 仓安全相关 issue/PR + R11 流程规则。全录 `corpus/org-sweep/drafts/out-oss-security.md`（12 规则候选 S1–S12）。

## 1. SECURITY.md 惯例（家族化少数派）

| 事实 | 数字 | 启示 |
|---|---|---|
| 仅 22/298（7.4%）仓有 SECURITY.md | TencentKona JDK 线 5 仓全有、tdesign/openclaw 新式 TS 仓、AI 安全仓 | 不是通用惯例——只有安全敏感或企业治理线才建 |
| 55 个 C++ 仓仅 MMKV 有 | 传统基础库几乎全无 | 老仓靠流程兜底不靠文件 |
| oss-scaffold 不建骨架 | settings-profiles 无 SECURITY.md 模板 | 套件自身也不默认建——跟仓现状 |

**规则 S1**：目标仓有 SECURITY.md → 引导报告者走其流程；无 → GitHub Private Vulnerability Reporting；均无 → 只说「需要私密沟通」，不在公开面讨论。

## 2. 安全漏洞分类路由（R11 兜底）

```
Issue 含安全关键词（CVE/漏洞/injection/XSS/…）
  ├─ SECURITY.md 存在 → 按文件引导
  ├─ GitHub Private Vulnerability Reporting 可用 → 引导私密提交
  └─ 均不可用 → 「请通过私密渠道报告」+ 不在 issue 正文展开技术细节
```

**规则 S2**（四禁公开面）：Issue 正文/评论/Commit message/**测试名**/PR 描述中禁止出现：载荷（payload）、复现脚本、exploit 代码。测试名也在禁令内（`test_xss_injection` 泄漏信息）。
**规则 S3**：安全漏洞是 PR 自动选题的硬排除项（pipeline.md 1.4）——不走贡献流程，走披露流程。

## 3. 检测分层（零降级）

| 层 | 工具 | 覆盖 | 缺失时 |
|---|---|---|---|
| 行级缺陷 | `ocr review --format json`（必装） | NPE/线程安全/XSS/SQL 注入 | **硬停** |
| 分类路由 | 本 skill §2 | 漏洞报告 → 正确渠道 | — |
| 依赖漏洞 | dependabot（23/296 仓配置，tdesign 家族 14 仓全配；renovate 0） | version-match advisory | 人工 `npm audit` 兜底 |

**规则 S4**：ocr CLI 的检测类型清单以 pipeline.md 转述为准（ocr help 本身不枚举——review/scan/rules check 子命令实测确认）。

## 4. 依赖漏洞响应

- **dependabot 是唯一惯例**（tdesign 家族 14 仓全配）；bot PR 被语料处理显式排除（不进人工审阅流）。
- **已公开 CVE 误报的公开说明模式**（AI-Infra-Guard #158）：在 issue 公开解释为何不影响本仓 + 给验证步骤——不隐藏不回避。
- **bot 批量 CVE 规则 PR 快合模式**（#647/#663）：dependabot 发起的批量更新走快速通道（不逐行 review，跑测试通过即合）。

## 5. [!WARNING] 警示模式（对照档案级——不主动套用）

D9 DNA 条目已被盲评退出阀降级为对照档案：目标仓已有 [!WARNING] 警示框 → 跟随其场景（部署边界/数据安全/访问控制）；仓没有 → 不主动引入。废弃 API 场景归 CHANGELOG Breaking Changes 段，不混入 WARNING。

## 6. 引用接口

- oss-contribution R11（安全流程）→ 本 skill §2 展开为三路路由。
- oss-contribution P7 自审 → ocr review 跑行级缺陷（S4 分层）。
- oss-scaffold 建仓 → 不默认建 SECURITY.md（S1 家族化行为），企业治理线仓例外。

## 7. 证据与局限

- 全部数字 298 仓结构层 + repo-index.tsv 现场复算；规则候选全录 out-oss-security.md（S1–S12）。
- 局限：渗透测试执行不在本 skill 范围（security-audit skill 管）；许可证法律意见不在范围（penguin-oss-ops 明确排除）；ocr 检测类型以 ocr CLI 实际输出为准非本 skill 枚举。


