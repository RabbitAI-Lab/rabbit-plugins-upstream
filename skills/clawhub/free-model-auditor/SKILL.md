---
name: free-model-auditor
description: |-
  审计 WorkBuddy 自定义模型注册表（models.json）中的免费模型：跨多个 OpenAI 兼容厂商新增可发现的免费模型、
  剔除已转付费或失效的模型，保持注册表真实有效。当用户要求「审计自定义模型」「检查有没有新的免费模型」
  「测试其余平台有无遗漏」「定期巡检模型清单」或希望对免费 API 模型做健康检查时使用。
  本技能对海外平台执行 VPN 连通性门禁，按各厂商策略判定免费，活体实测每个候选，并自动把新增/移除差异应用到 models.json。
agent_created: true
license: MIT-0
---

# 免费模型审计员

## 概述

维护 WorkBuddy 自定义免费模型注册表（`models.json`）的真实有效：检测各已配置厂商新上架的免费模型、
剔除已转付费或失效的模型。本技能内置各厂商「如何判定免费」的隐性知识（通用 API 调用无法获得），并对海外
厂商先做 VPN 连通性探针。

## 何时使用

- 用户要求做模型审计：「审计自定义模型」「检查有没有新的免费模型」「测试其余平台有无遗漏」
  「定期巡检模型清单」。
- 某厂商 Key 被（重新）添加，需要将其免费模型接入。
- 作为定时自动化任务的手动目标，按计划运行本审计。

## 关键启动门禁 — VPN 连通性（务必最先执行）

免费模型中可能包含**海外平台**（如 Google Gemini、NVIDIA NIM），在本机网络下受地域封锁。做任何活体测试前，
必须先过此门禁：

1. 解析 `models.json` 路径：优先 `$WORKBUDDY_CONFIG_DIR/models.json`，其次
   `$CODEBUDDY_CONFIG_DIR/models.json`，再次 `~/.workbuddy/models.json`。三者都不存在时，向用户询问路径。
2. 解析每条目的 `url` 主机，与 `references/platforms.md` 的**海外主机集合**交叉核对（当前为
   `generativelanguage.googleapis.com`、`integrate.api.nvidia.com`）。
3. 若存在**任何海外模型**，在继续前打印以下提醒：

   > ⚠️ 检测到当前免费模型中包含**海外平台**（Google Gemini / NVIDIA NIM 等）。这些模型在本机
   > 受地域封锁，调用前需先确认已开通**有效 VPN / 代理**（如 Clash `127.0.0.1:7897`）。
   > 正在做连通性探针……

4. 对海外主机运行 `references/test_harness.py probe`。
   - **可达** → 继续审计。
   - **不可达** → 停止。说明 VPN/代理未生效，请用户开通后重新调用。绝**不要**把不可达的海外模型标为
     「失效」（这是连通性产物，不是模型缺陷）。

本门禁满足既有要求：*若确认存在海外模型，须先确认已开通有效 VPN*。

## 路径自动识别（适配任意用户，步骤 1 前必做）

本技能会被许多「配置根」与「工作区根」与作者不同的用户安装。**严禁硬编码绝对路径**（如
`D:\WorkBuddy Files\...`）。启动时自动解析这两处路径，使技能在任意环境开箱即用：

1. 运行随附的辅助脚本（仅用标准库，跨平台）：
   ```bash
   python references/resolve_paths.py
   ```
   它会输出一个 JSON，包含：
   - `config_root` + `models_json` —— 自定义模型注册表所在位置
   - `workspace_root` + `memory_dir` —— 审计报告与每日日志的写入位置
   解析优先级：
   - **配置根**：`$WORKBUDDY_CONFIG_DIR`（目录存在时）→ `$CODEBUDDY_CONFIG_DIR`（目录存在时）→
     `~/.workbuddy`（默认）。
   - **工作区根**：`--workspace` 参数 → agent 当前工作目录（用户在 WorkBuddy 中打开的文件夹）。
2. 若 `models_json_exists` 为 `false`，**向用户询问路径**——不要猜测，也不要凭空创建注册表。
3. 后续每一步都用解析出的值替换以下占位符：
   - `{{MODELS_JSON}}` → `models_json`
   - `{{WORKSPACE_ROOT}}` → `workspace_root`
   报告始终写入 `{{WORKSPACE_ROOT}}/自定义模型审计与清单_YYYY-MM-DD.md`；每日日志写入
   `{{WORKSPACE_ROOT}}/.workbuddy/memory/YYYY-MM-DD.md`。

> 可移植规则：未重定向这两个环境变量（未做目录重定向）的用户，会自动回退到 `~/.workbuddy` 作为配置根、
> 到其自己打开的文件夹作为工作区根。本技能**永远不需要**任何按用户修改。

## 关键启动门禁 — 免费模型 API Key 自检（工作流前必做）

移植给其他用户时，部分用户的 WorkBuddy 可能**完全没有配置任何免费模型 API Key**（`models.json`
不存在，或其中没有任何可用聊天模型条目）。此情形下继续审计没有意义，应**先暂停、引导申请**，而非报错或空跑。
本策略复用 `free-media-gen` 技能的首装引导范式（分支 B）：

1. 完成「路径自动识别」后，读取 `{{MODELS_JSON}}`，统计其中**可用聊天模型条目**数量（即能作为厂商
   `apiKey` 来源的条目）。
2. **分支 A — 已有可用 Key**：正常进入「步骤 1」开始审计。
3. **分支 B — 无任何可用 Key**：**立即暂停，不继续审计**，向用户输出下方「申请引导」表，请其申请并配置
   Key 后重新触发本技能；不要猜测、不要创建空注册表。

   | 提供商 | 免费聊天/模型能力 | 申请地址 |
   |---|---|---|
   | Google Gemini | 海外免费层（需 VPN） | https://aistudio.google.com |
   | NVIDIA NIM | 大量免费模型（需 VPN） | https://build.nvidia.com |
   | 商汤 SenseNova | 国内，Kimi K3 / DeepSeek-V4 等 0 元公测 | https://www.sensenova.cn |
   | Agnes | 国内，免费图文/视频 | https://agnes-ai.cn |
   | 智谱 BigModel | 国内，GLM 系列 | https://open.bigmodel.cn |
   | 硅基流动 SiliconFlow | 国内，大量免费模型 | https://cloud.siliconflow.cn |

   > 引导说明：申请后将 Key 填入 WorkBuddy 对应平台的「自定义模型」（`models.json`）配置，保存后重新执行
   > 「审计自定义模型」即可。

## 工作流

### 步骤 1 — 载入当前注册表

读取 `{{MODELS_JSON}}`（即上文「路径自动识别」解析所得）。按 `url`（厂商）对现有条目分组。从同一厂商的任一
条目中记录其 `apiKey`（新增同厂商模型时复用）。

### 步骤 2 — 逐厂商审计

对每个已存在的厂商（或用户指定的厂商），从 `references/platforms.md` 载入其章节并执行：

1. **拉取目录**：`test_harness.py catalog URL API_KEY`（调用 `/v1/models`）。
2. **判定免费**：套用该厂商在 `references/platforms.md` 的策略（计费字段扫描、官方「免费」标记、或活体实测
   推断——三者各不相同）。
3. **排除非对话接口**：剔除 embedding / reranker / image-generation / ASR / TTS 模型（它们不兼容
   WorkBuddy 的对话补全 schema）。这与商汤图像生成模型的排除规则一致。
4. **活体实测候选**：对每一个尚未入库的免费候选运行
   `test_harness.py test URL API_KEY MODEL_ID`，记录 HTTP 状态与是否返回真实内容。使用感知推理的
   `max_tokens`（≥80），避免推理模型因额度不足而输出空白。

### 步骤 3 — 计算差异

- **新增（ADD）**：免费 + 可达 + 返回内容，且尚未在注册表中。
- **移除（REMOVE）**：在注册表中但现返回 `402`/`403`/`404`/`400`（付费/失效/未部署），或用户明确确认其已
  付费。**绝不**仅因 `429`（限流，仍有效）或 VPN 关闭导致的不可达而移除。
- **待定（UNCERTAIN）**：「200 ≠ 免费」的厂商（见 `references/platforms.md` 中 SiliconFlow）。仍按官方标记
  接入确认的候选，但在报告中标注「请于控制台核对是否真 0 计费」交由用户复核。

### 步骤 4 — 应用（自动写入并报告）

按既定策略，**直接将差异应用到 `models.json`**（不再单独确认步骤），随后报告：

1. 用规范 schema 构建每个新条目：
   `id`、`name` = `"厂商 · MODEL_ID (Free[, 类型])"`、`vendor: "Custom"`、`url`、
   `apiKey`（复用）、`supportsToolCall: true`、`supportsImages` / `supportsReasoning` 依据
   `references/platforms.md` 设定、`useCustomProtocol: false`，以及 `maxInputTokens` /
   `maxOutputTokens`（取自知识库或合理默认值）。
2. 插入/删除条目；保持 JSON 合法且格式化。
3. 校验：重新解析文件；断言无重复 `id`。

> 目标文件即「路径自动识别」解析出的 `{{MODELS_JSON}}`——绝不用硬编码路径。

### 步骤 5 — 报告与日志（带日期、滚动更新）

- **带审计日期后缀的输出文档**（本技能固定约定）：审计报告为写入**已解析工作区根**
  （「路径自动识别」所得的 `{{WORKSPACE_ROOT}}`）下的 Markdown 文件，命名为
  `自定义模型审计与清单_YYYY-MM-DD.md`，其中 `YYYY-MM-DD` 为**审计执行日期**：
  - **首次运行（新用户）**：创建 `{{WORKSPACE_ROOT}}/自定义模型审计与清单_<today>.md`
    （today = 审计日期）。
  - **其后每次运行**：刷新内容**并将文件名日期滚动到当前审计日期**。具体做法：在
    `{{WORKSPACE_ROOT}}` 递归查找已有的 `自定义模型审计与清单_*.md`；若位于
    `<dir>/自定义模型审计与清单_<old>.md`，先重命名为 `<dir>/自定义模型审计与清单_<today>.md`，
    再以新报告覆盖。这样始终只保留一份权威审计文档，其日期永远反映最近一次运行。
  - 用**同一审计日期**填充模板的 `{{DATE}}` 占位符，使文件内标题与文件名一致。
- 用 `templates/audit_report.md` 输出审计报告正文（新增 / 移除 / 不变 / 待定）。
- 向工作区每日日志（`{{WORKSPACE_ROOT}}/.workbuddy/memory/YYYY-MM-DD.md`）追加一行：审计了哪些厂商、
  新增/移除数量、注册表总条数、是否有 Key 轮换 / VPN 提醒。文件/目录不存在则创建。
- **强制项 — 输出完整免费模型清单**（既有约定：未输出此清单不算审计完成）。列出 `models.json` 中
  **每一个**模型，按厂商分组，用一张汇总表，列：`id` / 显示名 / 类型 / 多模态 / 推理 / 工具 / 上下文窗口 /
  状态。格式以 `templates/audit_report.md` 的「七、全部免费模型总结列表」为准。**即便新增/移除差异为空也
  绝不省略**——用户始终应收到一份所有免费模型的唯一权威清单。
- 结尾附上固定提醒：**重启 WorkBuddy 客户端**以加载变更；**轮换 API Key**（明文存于 `models.json`）；
  **海外模型需 VPN**。

## 使用 test_harness.py

该测试工具可导入也可命令行运行。示例：

```bash
# 海外主机 VPN / 连通性探针
python references/test_harness.py probe https://generativelanguage.googleapis.com https://integrate.api.nvidia.com

# 拉取某厂商模型目录
python references/test_harness.py catalog https://api.siliconflow.cn/v1 API_KEY

# 活体实测候选模型（自动读取 HTTPS_PROXY / HTTP_PROXY 环境变量）
python references/test_harness.py test https://api.siliconflow.cn/v1 API_KEY Qwen/Qwen3-8B
```

测试工具会自动读取 `HTTPS_PROXY`/`HTTP_PROXY`，因此 VPN 生效时测试会走用户代理。请遵守厂商限流
（候选之间插入短暂 sleep）。

配套辅助脚本 `references/resolve_paths.py` 会为当前用户解析 WorkBuddy 的两处路径（存放 `models.json`
的配置根，以及写入报告/日志的工作区根）——启动时运行一次，本技能便不再依赖任何硬编码绝对路径。

## 安全与运维

- **Key 为明文**：`models.json` 中 API Key 为明文存储——务必提醒用户在疑似泄露或定期情况下于厂商控制台轮换。
- **需重启**：`models.json` 的变更仅在重启 WorkBuddy 客户端后生效。
- **沙箱提示**：部分主机（如 `googleapis.com`）可能被执行沙箱拦截；当活体测试以连接重置（`000`）失败时，
  改用沙箱绕过标志或依赖用户系统代理重试。
- **禁止破坏性猜测**：仅在出现明确的 `402/403/404/400` 或用户明确确认时才移除模型——绝不在含糊情况下移除。
