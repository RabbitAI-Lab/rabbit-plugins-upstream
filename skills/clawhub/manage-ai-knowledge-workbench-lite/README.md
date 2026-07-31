# AI 自动知识工作台 Lite

让具备本地文件与终端能力的 AI 智能体，把一个用户明确授权的 Markdown 文件夹或 Obsidian Vault 自动构建为 Metadata-only 派生知识索引与离线 HTML 驾驶舱，并在用户再次提出更新要求时执行确定性的按需增量刷新。

> 当前版本：`1.0.2`
>
> 许可：MIT-0
>
> 默认隐私模式：Metadata-only
>
> Obsidian：可选，不是硬依赖

## 能做什么

- 为一个本地 Markdown/Obsidian 工作区生成结构化知识索引；
- 生成可离线打开的 `AI-Dashboard/index.html`；
- 在后续请求中执行确定性增量更新；
- 检查当前状态和输出完整性；
- 默认安全卸载运行状态，同时保留事实源和派生输出。

运行时只使用 Python 标准库，不要求数据库、Docker、Node、Obsidian CLI 或社区插件。

## 从 GitHub 获取

支持 GitHub 导入的 Skills 平台或 AI 宿主，应导入本仓库根目录；根目录已经包含 `SKILL.md`。正式分发建议固定到已发布标签，不要依赖浮动分支：

```text
https://github.com/alexfengrui/manage-ai-knowledge-workbench-lite
```

待 `v1.0.2` 标签创建并推送后，可直接检出固定版本：

```bash
git clone --branch v1.0.2 --depth 1 \
  https://github.com/alexfengrui/manage-ai-knowledge-workbench-lite.git
```

不同平台的导入、审核和安装命令可能不同，请以平台详情页最终显示的仓库引用、开发者命名空间和技能标识为准。

## 在 ModelScope 中安装

在 ModelScope Skills Center 创建或更新技能时，选择 GitHub 仓库导入，并填写：

```text
https://github.com/alexfengrui/manage-ai-knowledge-workbench-lite
```

待 `v1.0.2` 标签创建并推送后，正式发布建议固定选择该标签。审核通过后，也可以使用详情页实际生成的 `modelscope skills add`、`npx skills add` 或安装脚本命令；不要手工猜测开发者命名空间或安装地址。

## 从 360 安全技能中心安装

在 360 安全技能中心选择平台当前提供的 GitHub 导入入口；如果该入口尚未对账号开放，则待 `v1.0.2` 标签创建并推送后，下载该标签对应的源码包上传。审核发布后，以详情页给出的 `secure-skills` 安装命令和最终技能 slug 为准。

## 运行前提

- 一个已经能够调用模型、访问授权目录并执行终端命令的 AI 宿主；
- Python 3.10 或更高版本，可通过 `python3`、`python` 或 Windows `py` 中至少一个真实版本探针确认；
- 对目标工作区的本地读写授权；
- 用户明确指定的 Markdown 文件夹或 Obsidian Vault。

Skill 不读取、保存或代管模型 API Key、GitHub 凭据、Cookie 或其他账号凭证。

## 行为与权限声明

| 行为 | 是否需要 | 精确范围 |
|---|---:|---|
| 执行本地代码 | 是 | 仅运行随包 Python 标准库脚本 |
| 读取本地文件 | 是 | 仅限用户明确授权的 Markdown/Obsidian 事实源和受管状态 |
| 写入本地文件 | 是 | 仅限选定工作区内 `.ai-workbench`、`AI-Knowledge`、`AI-Dashboard` |
| 修改事实源 | 否 | 默认不移动、删除、重命名或覆盖原始笔记 |
| 外部 API | 否 | 工作台核心构建、更新、状态和卸载不依赖第三方 API |
| 本地网络监听 | 临时 | 只为页面验证绑定 loopback，验证后停止 |
| 安装依赖或提权 | 否 | 缺少 Python 时停止并请求用户自行处理 |
| 后台常驻 | 否 | 不含 watcher、计划任务或持久 Web 服务 |

## 一句话开始

普通 Markdown 文件夹：

```text
请使用 AI 自动知识工作台，把这个目录自动构建成知识工作台并打开驾驶舱：<目录>
```

已有 Obsidian Vault：

```text
请使用 AI 自动知识工作台接入这个 Vault，把它同时作为工作区和事实源，不修改原笔记，完成后打开驾驶舱：<Vault 目录>
```

后续更新：

```text
请更新这个知识工作台，并告诉我实际变化和校验结果。
```

AI 应自行完成工具调用。除非遇到真实权限或安全门禁，用户不需要逐条执行工作台内部命令。

## AI 会自动完成什么

1. 探测 Python 和当前智能体宿主的实际版本；
2. 确认一个用户授权的工作区和事实源；
3. 诊断权限、路径、输出冲突和可用模式；
4. 安全初始化内部状态；
5. 扫描允许的元数据和显式 Markdown 结构；
6. 生成派生知识索引与导航；
7. 校验计数、链接、敏感边界和输出结构；
8. 生成离线 HTML 驾驶舱；
9. 启动临时 loopback 校验，并在验证后停止；
10. 返回实际产物路径和机器可读状态。

首次构建成功状态为 `AUTO_RUN_READY`。资料变化后，按需更新只处理真实差异；没有变化时不重写知识层或 HTML。

## 输出目录

默认只在选定工作区内创建三个保留目录：

| 目录 | 用途 | 是否事实源 |
|---|---|---|
| `.ai-workbench` | 配置、索引、状态与校验回执 | 否，可重建 |
| `AI-Knowledge` | 派生 Markdown 索引和导航页 | 否，可重建 |
| `AI-Dashboard` | 离线 HTML、数据和本地资源 | 否，可重建 |

用户原始 Markdown、Obsidian 笔记或指定资料目录才是事实源。请继续在原始资料中编辑，不要把 `AI-Knowledge` 当作新的输入源反复嵌套构建。

## 隐私与安全边界

Lite 固定为 Metadata-only：

- 本地确定性解析器可能读取授权 Markdown，以提取允许的 frontmatter、标题、标签和显式链接；
- 不把笔记正文发送给模型；
- 不把正文、密钥或事实源绝对路径嵌入 HTML；
- 敏感或未知敏感级别的记录默认不进入可见视图；
- 默认不移动、删除、重命名或覆盖事实源；
- 本地页面不使用远程 CDN、统计脚本或源文件写入接口；
- 临时预览只绑定 loopback，并在自动验证后停止；
- 默认不安装依赖、不提权、不创建后台常驻项。

准确边界是“正文不发送给模型”，不是“程序从不读取 Markdown 文件”。AI 宿主本身可能把用户提示、Skill 指令和结构化工具结果发送给其已配置模型；模型服务的数据政策由宿主和模型提供商决定。

以下动作必须暂停并请求用户确认：访问新的目录、安装软件、提权、处理未知输出冲突、修改或删除事实源、删除派生产物、登录、上传、付款、发布或其他外部数据传输。

详细约束见：

- [`references/PRIVACY.md`](references/PRIVACY.md)
- [`references/AUTONOMY_GATES.md`](references/AUTONOMY_GATES.md)
- [`references/RUNTIME_CONTRACT.md`](references/RUNTIME_CONTRACT.md)

## Lite 版边界

Lite 包含：

- 单工作区 Metadata-only 构建；
- 普通 Markdown 与 Obsidian Vault；
- AI 自主首次构建和离线 HTML；
- AI 触发的按需增量更新；
- 状态检查；
- 默认保留事实源和派生产物的安全卸载。

Lite 不包含：

- 模型生成的正文摘要、语义分类或关系推断；
- filesystem watch、session watch 或后台计划任务；
- 持久 Web 服务；
- 多工作区聚合；
- 付费授权、支付、订单、回调或退款模块；
- 自动安装宿主、Python、Obsidian、模型或系统服务。

因此，“自动更新”在 Lite 中表示：用户提出更新目标后，AI 自动完成整次增量更新；它不表示宿主退出后仍永久在后台监听。

## 仓库结构

```text
.
├── SKILL.md
├── README.md
├── LICENSE
├── agents/
├── references/
└── scripts/
```

本仓库是公开 Lite 分发源。付费 Pro、SkillPay、支付服务和私有开发材料不属于本仓库。

## 版本 1.0.2

- 将 GitHub 分发源的包内、运行时和对外版本口径统一为 `1.0.2`；
- 强化 AI 自主构建与按需增量更新；
- 将 Python 探针扩展为 `python3` / `python` / Windows `py`；
- 完善宿主前置条件、Metadata-only 隐私说明和安全卸载边界；
- 提供适合 GitHub 固定标签导入的根目录结构。

## 许可

本 Lite 版本使用 MIT-0。任何人均可使用、修改和再分发，且不要求署名。

## English quick start

AI Knowledge Workbench Lite lets an AI agent turn one user-authorized Markdown folder or Obsidian Vault into a derived Metadata-only knowledge index and an offline HTML dashboard.

Requirements:

- an already configured agent host with local file and terminal tools;
- Python 3.10+ available as `python3`, `python`, or Windows `py`;
- one authorized workspace/source directory;
- Obsidian is optional.

After tag `v1.0.2` has been created and pushed, import this repository from a supported Skills platform pinned to that tag. Then ask your agent:

```text
Use AI Knowledge Workbench Lite to build this folder into a local knowledge workbench and open the dashboard: <folder>
```

The deterministic local parser may read authorized Markdown to extract allowed metadata, but it does not send note bodies to a model or embed them in the dashboard. Background watching, semantic content processing, paid licensing and payment modules are not included.
