# systems-thinking

<!-- Language toggle / 语言切换 -->

> **中文** | [English](README.md)

---

## 简介

`systems-thinking` 是一个思维模式 skill。它把控制论的思想装进 LLM 的思考过程里，让模型在写代码、改代码、做架构之前，先想清楚：状态是什么、怎么观测、稳不稳定、边界在哪、耦合怎么处理。

> **一句话：用系统视角写代码——先识别状态，再动手，最后闭环验证。**

这不是给人类做的知识测试，也不是一本排错手册。它是一个脚手架，改变的是模型**怎么想**，而不是怎么拼 diff。

源自钱学森、宋健《工程控制论》。语言和框架无关，拿来就能用。

## 它解决什么问题

写代码时常见的做法是：先动手，再祈祷测试能过。这个 skill 要改变的是这个顺序。

它特别适合这些场景：

- 改一段你不完全理解的遗留代码
- 调试一个时好时坏、复现不了的问题
- 重构几个互相牵制的模块
- 做任何"既要正确又要稳"的改动

在这些场景里，"写个最小补丁"往往不够。你需要先搞清楚系统的状态，再动手。

## 核心思想

一句话：**程序是一个动态系统，你是控制器。**

每次改动都在往系统里注入一个控制信号。你只能部分观测系统的真实状态。bug 是不稳定或欠阻尼的轨迹。调试就是状态估计。测试是反馈回路的传感器。**闭环永远比开环好。**

## 安装

本 skill 面向支持自定义 skill 的 AI 编程助手（Kilo、Claude Code、Aider、Cursor 等）。

### npx 一键安装（推荐）

```bash
npx skill-systems-thinking install
```

默认情况下，安装程序会扫描你机器上已安装的 agent，并将 skill 链接到它们的全局和项目本地目录。只有实际检测到的 agent 才会被安装。

- 选择特定 agent 安装：`npx skill-systems-thinking install --agents kilo,claude-code`
- 仅全局安装：`npx skill-systems-thinking install --global`
- 仅项目本地安装：`npx skill-systems-thinking install --local`
- 强制覆盖已存在的链接：`npx skill-systems-thinking install --force`

### npm install（仅下载）

```bash
npm install skill-systems-thinking
```

这只会**下载**包到 `node_modules/skill-systems-thinking`，并不会把 skill 链接到你的 agent skill 目录。下载后仍需运行安装命令：

```bash
npx skill-systems-thinking install
```

### GitHub 下载

```bash
git clone https://github.com/ShrimpLeon/systems-thinking.git
cp -r systems-thinking <agent-skills-dir>/
```

### Gitee 下载

```bash
git clone https://gitee.com/leon0903/systems-thinking.git
cp -r systems-thinking <agent-skills-dir>/
```

### 符号链接（开发用）

```bash
ln -s /absolute/path/to/systems-thinking <agent-skills-dir>/
```

### 各 agent 配置

npx 安装会自动将 skill 链接到各 agent 的 skill 目录。手动安装时，各 agent 的 skill 目录如下。

| Agent | Skill 目录 |
|---|---|
| Kilo | `~/.config/kilo/skills/` 或项目 `.kilo/agent/` |
| Claude Code | `~/.claude/plugins/custom-skills/` 或项目 `.claude/` |
| Aider | `--skills-dir` 路径 |
| Cursor | 项目 `.cursor/rules/` 或全局设置 |
| OpenAI Codex | `~/.codex/skills/` |
| GitHub Copilot | `~/.copilot/skills/` |
| Windsurf | `~/.windsurf/skills/` |
| Zed | `~/.zed/skills/` |

> **注意：** 如果你的 agent 未出现在上方，请查阅其文档获取自定义 skill/plugin 路径。

### 验证安装

```bash
pwsh init.ps1
```

看到 `Verification Complete — OK` 即表示安装成功。

## 兼容性

npm 包 `skill-systems-thinking` 兼容以下 AI 编程助手：

| Agent | npm 安装兼容 | 说明 |
|---|---|---|
| Kilo | ✅ | 通过 `~/.config/kilo/skills/` 或 `.kilo/agent/` 链接 |
| Claude Code | ✅ | 通过 `~/.claude/plugins/custom-skills/` 或 `.claude/` 链接 |
| Aider | ✅ | 通过 `--skills-dir` 参数指定链接目录 |
| Cursor | ✅ | 通过 `.cursor/rules/` 或全局设置链接 |
| OpenAI Codex | ✅ | 通过 `~/.codex/skills/` 链接 |
| GitHub Copilot | ✅ | 通过 `~/.copilot/skills/` 链接 |
| Windsurf | ✅ | 通过 `~/.windsurf/skills/` 链接 |
| Zed | ✅ | 通过 `~/.zed/skills/` 链接 |

npx 安装会自动将 skill 链接到各 agent 的 skill 目录。

## 使用方式

### 1. 触发时机

在涉及以下任务时加载本 skill：

- 架构设计
- 调试非确定性行为
- 跨模块重构
- 任何"正确且稳健必须同时满足"的改动

### 2. 读 SKILL.md

先读 `SKILL.md`，里面的运行时提示块会安装认知法则。下面的工作流是自然延伸。

### 3. 动手之前，先命名

改代码之前，必须说清楚四个东西：

- `x` — 被控变量，什么必须保持正确
- `u` — 控制变量，你实际会动的那个杠杆
- 可观测性 — 你怎么知道 `x` 的当前值
- 边界 — 每个执行器都会饱和，不接受无界循环

### 4. 七步循环

| 步骤 | 原则 | 参考文件 |
|---|---|---|
| 1 | 识别：命名 `x`、`u`、可观测性、边界 | `references/state-and-control.md` |
| 2 | 分析：复现、测量、定位故障、建立模型 | `references/modeling.md` |
| 3 | 稳定：在加新功能之前先消灭发散/振荡/泄露 | `references/stability.md` |
| 4 | 综合：最小 `u`；解耦有害，协调有益 | `references/multivariable.md` |
| 5 | 闭环：观察实际结果，修正直到偏差有界 | `references/closed-loop-workflow.md` |
| 6 | 补偿：可测扰动用前馈；有延迟就加阻尼 | `references/disturbance.md` |
| 7 | 优化：稳定之后才谈性能调优 | `references/bounded-control.md` |

涉及采样和测试节奏的问题，额外参考 `references/discrete-systems.md`。

### 5. 模板

以下文件位于 skill 安装目录下的 `templates/` 子目录中：

- **调试时**：把 `templates/debugging-checklist.md` 复制进会话
- **规划改动时**：用 `templates/change-proposal.md` 写控制计划

### 6. 自审计

宣布完成之前，必须通过 `evals/checks.json` 中所有的 MUST 检查项。

## 认知法则

这个 skill 强制执行 8 条认知法则：

1. 先命名 `x` 再命名 `u`。没名字的目标就没法调节。
2. 先观测再猜测。综合方案之前先测量当前行为。
3. 稳定优先于优化。扰动下发散就是失败。
4. 闭环。观察实际结果，不断修正直到偏差有界。
5. 可测扰动用前馈，其余用反馈。绝不在延迟回路上提高增益。
6. 解耦有害耦合，协调有益耦合。调节关系，不只是绝对值。
7. 最小控制。移动 `x` 到目标所需的最小 `u`，不做多余的改动。
8. 收敛。修正幅度必须越来越小。如果越来越大，说明不稳定——停下来重新识别。

## 工作示例

**问题**：一个 API 接口在负载下间歇性返回 500。

| 步骤 | 控制论行动 |
|---|---|
| 识别 | `x` = 错误率；`u` = 重试/超时/缓存逻辑；边界 = 请求预算。 |
| 分析 | 在负载下复现；测量错误率随并发上升（不稳定）。 |
| 稳定 | 加熔断器 + 带退避的有界重试 → 错误率有界。 |
| 综合 | 最小改动，不要重写服务。 |
| 闭环 | 再次压测；错误率收敛到接近 0。 |
| 补偿 | 对可测依赖故障快速失败（前馈）+ 其余用反馈。 |
| 优化 | 此时才 trim p99 延迟。 |

**没有这套视角的常见失败**：无限制加重试 → 重试风暴（不稳定延迟环）→ 比原来更糟。

## 参考文件

8 篇深度参考，每篇对应一个控制论原则，附带 LLM 行为模式说明：

| 主题 | 文件 |
|---|---|
| 闭环工作流 | `references/closed-loop-workflow.md` |
| 状态、控制、可观测性、边界 | `references/state-and-control.md` |
| 稳定性 | `references/stability.md` |
| 建模与模型有效性 | `references/modeling.md` |
| 多变量：解耦与协调 | `references/multivariable.md` |
| 扰动补偿与时延 | `references/disturbance.md` |
| 有界控制 | `references/bounded-control.md` |
| 离散系统与测试节奏 | `references/discrete-systems.md` |

## 自审计

`evals/checks.json` 列出了一组 MUST/SHOULD 检查项，供 LLM 或评审者确认思维 discipline 被遵循。在所有 MUST 项通过之前，不得宣布任务完成。

## 贡献

- `SKILL.md` 中的每条主张都必须追溯到某个参考文件
- 每个引用链接必须能解析到存在的文件
- 保持 skill 精简，与原著保持一致
- 提交前运行 `./init.ps1`

完整工作规则见 `AGENTS.md`。

## 版本

本 skill 遵循 [Semantic Versioning](https://semver.org/)（`X.Y.Z`）。

| 版本 | 日期 | 说明 |
|---|---|---|
| 0.2.0 | 2026-07-26 | 安装 CLI 新增 agent 选择和安装位置 flags |
| 0.1.5 | 2026-07-25 | 分离 README.md / README_CN.md；统一版本号 |
| 0.1.4 | 2026-07-25 | 缺陷修复 |
| 0.1.3 | 2026-07-25 | 统一项目版本号；添加 XYZ 版本约定到 AGENTS.md；移除 postinstall 脚本 |
| 0.1.2 | 2026-07-25 | 添加 Gitee 下载链接；更新 repository 和 homepage 到 Gitee |
| 0.1.1 | 2026-07-24 | 修复 repository.url；扩展 keywords；添加 homepage 和 bin 字段 |
| 0.1.0 | 2026-07-24 | 首次公开发布 |

完整变更记录见 [CHANGELOG.md](CHANGELOG.md)。

## 协议

MIT License。详见 [LICENSE](LICENSE)。

---

## Source

Qian Xuesen (Tsien Hsue-shen‌; 钱学森) & Song Jian (宋健), *Engineering Cybernetics* (工程控制论). The original book and its mathematical foundations are the authoritative source; this skill is a faithful interpretation, not a replacement.
