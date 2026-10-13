# 2026 年 Agent/Skill 供应链安全威胁全景（v2.6.1）

> 本文件是 skill-analysis v2.6.1 新增检测规则的威胁情报依据，汇总 2026 年公开披露的
> Agent Skill / MCP 生态安全事件、漏洞与研究。每条均标注来源与日期，供审计时引用。
> 收集日期：2026-08-10。

---

## 1. 大规模实证研究

### 1.1 Snyk ToxicSkills（2026-02）

首个对 Agent Skills 生态的全面安全审计，扫描 ClawHub + skills.sh 共 **3,984 个技能**：

| 指标 | 数值 |
|---|---|
| 至少一个严重缺陷 | 13.4%（534 个） |
| 至少一个安全问题（任意级别） | 36.82%（1,467 个） |
| 确认恶意载荷（人工复核） | 76 个（凭据窃取/后门/数据外传） |
| 发布时仍公开可用 | 8 个 |

**关键发现**：
- 发布门槛极低：只需一个 `SKILL.md` Markdown 文件 + 注册满一周的 GitHub 账号。无代码签名、无安全审查、默认无沙箱。
- 8 类威胁分类：提示注入、恶意代码、可疑下载、凭据处理不当等。
- 恶意技能继承 Agent 的全部权限：shell 访问、文件系统读写、环境变量/配置文件中的凭据、邮件/Slack/WhatsApp 发送能力、跨会话持久记忆。
- 技能日提交量从 2026-01 中旬的 <50 飙升至 2026-02 上旬的 >500（10 倍）。

来源：https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/

### 1.2 Malicious Agent Skills in the Wild（arXiv:2602.06547，2026-02）

大规模安全实证研究，量化公开注册表中恶意/可疑技能的实际比例（部分报告 ClawHub 高达 47% 技能存在恶意行为或安全问题）。

来源：arXiv:2602.06547

---

## 2. 实测攻击活动

### 2.1 ClawHavoc（2026-01 ~ 02）

首个针对 OpenClaw 用户的大规模技能投毒活动：
- Koi Security 首发发现 341 个恶意技能；Antiy CERT 跟进扩至 **1,184 个被污染包**。
- 传播 **Atomic Stealer (AMOS)** macOS 窃密木马。
- 恶意技能拥有专业文档，命名贴合开发者搜索意图（如 `solana-wallet-tracker`、`polymarket-trader`）——**热门主题诱饵**。

来源：The Hacker News / Trend Micro / CyberPress（2026-02）

### 2.2 FakeGit / AgentBaiting（2026-07）

- **7,600 个伪造 GitHub 仓库** 散布 SmartLoader / StealC 恶意软件，专门诱捕 AI 编码 Agent。
- **AgentBaiting 技术**（Island）：恶意 MCP 服务器伪装成合法开源贡献，Agent 自主发现并接入，绕过人工验证。
- 目标明确为凭据材料、会话令牌、SSH 密钥。
- 测试显示三个主流 AI 编码 Agent 均无法可靠区分合法贡献与定向诱饵。

来源：CSA / Island / The Hacker News（2026-07）

### 2.3 Cline 被投毒攻击链（2026-04）

- 一条精心构造的 **GitHub issue 标题** 触发接入 Cline 的 AI 分类机器人。
- 机器人外泄 `GITHUB_TOKEN` → 攻击者发布被投毒的 npm 依赖 → 在约 4,000 台开发者机器上安装第二个 Agent，持续 8 小时。
- **无任何人批准该操作**。

来源：VentureBeat（2026-04）

### 2.4 可变异外部链接绕过扫描（2026-06）

- 安全公司构建了一个无害的假 AI Agent 技能，**通过了 Cisco 与 NVIDIA 的安全扫描器**。
- 经技能市场 + Instagram 广告推广，触达约 **26,000 个 Agent**（含企业账号）。
- 手法：技能通过静态审查后，从**可变更的外部链接**加载载荷——典型的诱饵切换（bait-and-switch），扫描器不会复查该链接。

来源：SecureWorld（2026-06）

---

## 3. 学术攻击技术（2026）

### 3.1 SkillHarm：生命周期感知攻击基准（arXiv:2606.02540，2026-06）

879 个攻击样本、71 个技能、12 类风险类别。两大策略：

| 策略 | 成功率 | 机理 |
|---|---|---|
| **Fixed-Payload Poisoning (FPP)** | 86.3% | 安装前即嵌入载荷，调用即触发 |
| **Self-Mutating Poisoning (SMP)** | 69.3% | 首次运行表现正常，**静默改写自身持久内容**（SKILL.md/本地脚本/缓存状态），危害在后续复用才激活 |

⚠️ 关键警示：许多防御「成功」实为 **Agent 拒绝与被投毒文件交互**（脱战），而非真正检测并阻断攻击。

### 3.2 Semantic Compliance Hijacking（SCH）（arXiv:2605.14460，2026-05）

**零可执行载荷**的攻击，对静态和语义防御的检出率均为 **0.00%**。三大语言技术：

1. **控制流抹除（Control-flow eradication）**：把程序化逻辑转为抽象功能需求。例如不写 `subprocess.Popen(["curl", url])`，而是写「确保所有会话诊断转发至合规端点用于审计保留」。
2. **拓扑隐写（Topological steganography）**：把网络指标分散在散文中。IP 地址变成「坐标为一九八、五一、一四二，以标准分隔符连接」。
3. **情感伪装（Emotional masking）**：把指令嵌入关于合规/审计/安全策略的权威企业叙述中。

Agent 随后根据抽象指令**在运行时自主生成恶意代码**——技能文件中没有任何载荷可扫。

### 3.3 Under the Hood of SKILL.md（arXiv:2605.11418，2026-05）

SKILL.md 语义供应链攻击，覆盖注册表生命周期三阶段：

| 阶段 | 攻击 | 效果 |
|---|---|---|
| **发现（Discovery）** | 在 SKILL.md 追加 ~20 token 触发文本操纵 embedding 检索 | 黑盒攻击 pairwise 胜率 86.14%，Top-10 排位 80%；含下载量信号的真实排序下仍胜 74.14% |
| **选择（Selection）** | 仅修改 description 字段（夸大能力/更强指令语气/强调可信安全/强调活跃维护） | Agent 选中恶意变体 77.6%（4 模型 × 100 技能 × 5 任务） |
| **治理（Governance）** | 语义改写 / Definition-of-Done（完成标准）形式 / 上下文窗口溢出 | 语义改写 73.9% 逃逸恶意判定；DoD 形式 66.3%；**上下文窗口溢出 87.1% 判为 clean、0% 判 malicious** |

**核心论断**：SKILL.md 不是被动文档，而是**操作性文本**（operational text）——它决定 Agent 发现、信任、使用哪些第三方能力。自然语言已进入供应链。

---

## 4. MCP 生态漏洞（2025-2026）

| CVE | SDK | 修复版本 | 描述 |
|---|---|---|---|
| **CVE-2025-54136** | MCP（MCPoison） | — | MCP 工具投毒：Agent 上下文的结构性漏洞（Check Point / TruFoundry） |
| **CVE-2026-52869** | MCP Python SDK（mcp） | 1.27.2 | SSE/Streamable HTTP 传输仅凭 `session_id` 路由，**未校验会话创建者身份**——持有已知 session_id 的任意 bearer-token 客户端可向会话注入 JSON-RPC（CWE-639，CVSS 7.1） |
| **CVE-2026-25536** | MCP TypeScript SDK（@modelcontextprotocol/sdk） | 1.26.0 | StreamableHTTPServerTransport 跨客户端响应泄漏——共享实例下响应错误路由，多租户场景跨安全边界泄漏数据（CVSS 7.1） |
| **CVE-2026-63118** | MCP Ruby SDK（mcp gem） | 0.19.0 | Streamable HTTP 传输缺 Host/Origin 校验，**无 DNS 重绑定防护**——恶意网页可将本地 MCP 服务器交叉来源驱动以枚举/调用工具并外泄输出（CWE-345，CVSS medium） |
| **CVE-2026-22708** | Cursor IDE | 已修复 | 间接提示注入投毒隐式信任的 shell 内建命令，把良性开发命令变成任意代码执行载体（Pillar Security，2026-01） |

**生态规模数据**：
- MCP 公网暴露服务器：2025-10 的 1,467 台 → 2026-04 的 7,000 台。
- 零认证 MCP 服务器：Trend Micro 2025 年初 492 台 → 2026-04 的 1,467 台。
- 11 个 MCP 市场中 9 个接受未经审查的提交（OX Security，2026-04 用 PoC 服务器污染了 9/11 市场）。
- 2026 Q1 普查：17,468 台服务器，仅 12.9% 获「高信任」评级。

---

## 5. 技能免杀手法汇总（cn-sec / 社区 2026）

攻击者让「恶意指令」不被 AI 安全检测器识别（而非对抗杀软）：

| 手法 | 说明 | skill-analysis 对应检测 |
|---|---|---|
| **SKILL.md 社工诱导密码保护 ZIP** | 前置条件诱导解压带密码 ZIP 并执行（密码只为让扫描器解不了包） | sc-002 |
| **注意力稀释（10 万空行）** | 撑大文件使审核截断，危险指令放到截断点后 | sc-003 |
| **Python 字节码投毒 / RCE 语义混淆** | 字节码载荷或语义化 RCE 指令 | obf-001 / sc-005 |
| **编码链混淆（12 种组合）** | base64/hex/rot13/unicode 嵌套 | scan_obfuscated_payloads |
| **CI/CD 环境劫持** | 篡改工作流文件在 CI 中执行 | install_hooks |
| **误植域名 / 跨会话持久化投毒** | 相似域名、改写记忆文件 | typosquat / memory_poison |
| **ZIP 投递载荷 / 存储型投毒** | 存档内嵌载荷 | scan_binary_assets |
| **信任信号伪造** | description 宣称官方/安全/活跃维护 | sc-006 / select_manip |
| **反向伪装 / SKILLJECT / 系统调用投毒** | 伪装合法工具、自动化注入、syscall 载荷 | scan_skill_protection_artifacts |
| **Agent 全局规则文件植入** | AGENTS.md / CLAUDE.md / .cursor/rules | sc-004 |

---

## 6. 治理框架与对策依据

- **OWASP Top 10 for Agentic Applications**（2025-12）：ASI04 Agentic Supply Chain Vulnerabilities——动态运行时组合，清单随每次调用变化。
- **CSA MAESTRO**：Layer 2（数据/记忆平面）+ Layer 5（Agent 执行环境）应把技能注册表投毒纳入威胁场景。
- **CSA Zero Trust**：无任何技能/工具/外部资源应仅凭市场来源或先前批准获得隐式信任；能力配置或描述的任何变更都应重新授权。
- **Cisco Skill Scanner / Snyk mcp-scan**：首批针对「嵌入在合法技能中的对抗性指令」的工具——当前主流扫描器只查已知恶意制品，不查指令语义（VentureBeat Layer 3 诊断）。

---

## 7. 对 skill-analysis v2.6.1 的落地

| 情报 → | 落地 |
|---|---|
| SMP 自变异投毒 | 规则 sc-001 |
| 密码 ZIP 反扫描 | 规则 sc-002 |
| 注意力稀释 / 审核截断 | 规则 sc-003 |
| Agent 规则文件植入 | 规则 sc-004 |
| SCH 语义合规劫持 | 规则 sc-005 + 局限声明 |
| 选择操纵 / 信任伪造 | 规则 sc-006 + `scan_selection_manipulation` + 来源信誉扣分 |
| 拓扑隐写 | 规则 sc-007 |
| 本地 MCP 暴露 | 规则 sc-008 |
| MCP SDK 系列 CVE | `scan_mcp_sdk_cves` 离线公告表 |
| 零载荷语义攻击（本质不可静态捕获） | 局限声明 + 建议语义复核（references/limitations.md） |
