# 内置依赖

> **何时读**：要使用视频、动画、设计 Skill、文档 Skill 或网页库；需要知道某个依赖是否就绪；缺了东西；或者这个人问装了什么、怎样移除。

OpenXSys 附带一组经过审查的**内置依赖**，随它一起安装，让第一次运行不用再做任何设置，就能产出交互网页、卡片和短视频。Agent Skills 没有正式的依赖字段，所以 OpenXSys 使用锁定文件和安装器。

- `openxsys.lock.json`：权威的清单。每个依赖都锁定在一个确切的提交或版本上，附校验值。
- `install.sh`、`install.ps1`：安装器，分别用于 macOS 与 Linux，以及 Windows。
- `installed.json`：由安装器写进安装好的 Skill 里。它记录实际装了什么、装在哪里、什么时候装的。读它，就知道什么已经就绪。

锁定文件和两个安装器在中英文两个版本里完全相同。

## 这个版本的审查状态

**这是一个预发布版本（0.0.1-alpha.1）。还没有任何依赖经过审查。** 锁定文件里的每一条都是**候选**：它的锁定值和校验值是真实的，记录于 2026-11-16，但还没有人把锁定的内容完整读过一遍并留下审查记录。“每一项发布前都经过审查”是一道发布关卡，而这道关卡还没有过。

这在实际中意味着：

- 安装器会安装 OpenXSys 本身，并**跳过每一个待审查的依赖**，除非传入 `--include-pending`。这个参数是给审查者和测试者用的，它会打印出自己要做什么。
- 在依赖被批准之前，把它们当作没有内置。如果这个人自己已经装了这样的 Skill，它就是这个人的一条连接，可以作为这个人的东西来使用。
- 当锁定文件里一个依赖的 `review.status` 为 `approved`，并且 `evals/reviews/` 里有一份审查记录时，它才成为内置依赖（一次审查检查什么：`kit/KIT.md`）。

## 这一组依赖

| 能力 | 依赖 | 发布者 | 需要 | 没有它时 |
|---|---|---|---|---|
| **交互网页** | D3、GSAP + ScrollTrigger、Scrollama、KaTeX、Mermaid、Three.js、MapLibre GL JS，锁定版本，附离线副本 | 各自的维护者，经 npm 仓库 | 什么都不需要（一个浏览器） | 页面用朴素的 HTML、CSS、SVG 和 JavaScript，这常常是更好的选择 |
| **视频** | `remotion-dev/skills` 里的 `remotion-best-practices`、`remotion-create`、`remotion-render`、`remotion-captions`、`remotion-license` | Remotion（官方） | Node.js | 一个完整的交互网页和一张静态卡片 |
| **概念与数学动画** | `vumichien/manim-skill` 里的 `manim-video` | 社区 | Python | 页面里的 SVG 或 canvas 动画 |
| **视觉设计** | `anthropics/skills` 里的 `frontend-design`、`canvas-design` | Anthropic（官方） | 什么都不需要 | 你自己的设计判断，以 `display/` 为标准 |
| **文档与演示稿** | `anthropics/skills` 里的 `pptx`、`docx`、`pdf`、`xlsx` | Anthropic（官方） | Python（它们的脚本要用） | 同样的内容，做成网页或 Markdown |
| **检查渲染出来的成果** | 宿主的浏览器工具；没有时用 `anthropics/skills` 里的 `webapp-testing` | Anthropic（官方） | Python | 像读者那样读源文件，并说明它没有经过渲染 |
| **分享卡片与短视频** | 通过网页库与视频 Skill 渲染 | | | 一张静态的 SVG 或 HTML 卡片 |

网页库以及各自的用途：`display/libraries.md`。

## 许可证与附加条件

安装器会在安装任何东西之前展示这些，并在审查时确认：

- **Remotion** 不是普通的开源软件。它对个人和小团队免费，**超过一定团队规模的公司需要购买公司许可证**。在工作中使用之前，先读 https://remotion.dev/license 上的现行条款。内置了 `remotion-license` 这个 Skill，就是为了让条款随手可查。
- **Anthropic 的文档 Skill**（`pptx`、`docx`、`pdf`、`xlsx`）有自己的许可条款，与同一个仓库里开源的示例 Skill 不同。读每个 Skill 的 `LICENSE.txt`。
- **GSAP** 按它自己的标准许可证可以免费使用，那不是 OSI 认定的开源许可证。
- **D3**（ISC）、**Scrollama**、**KaTeX**、**Mermaid**、**Three.js**（MIT）和 **MapLibre GL JS**（BSD-3-Clause）是开源的。MapLibre 需要地图瓦片来源，那有它自己的条款。
- **`skills` 命令行工具**（MIT）默认会收集匿名的使用数据。安装器会把它关掉。

这些条件里有任何一条不适合这个人或这个人的雇主，就把那个依赖留在外面：`--without <id>`。

## 安装

**一次安装，一次同意。** 安装器展示内置清单、许可证与所需的运行环境，问一次，然后一起安装。之后，系统使用内置依赖时不再询问。

```sh
# macOS、Linux、Git Bash
sh skills/open-x-sys/deps/install.sh --lang zh-CN

# Windows PowerShell
powershell -ExecutionPolicy Bypass -File skills\open-x-sys\deps\install.ps1 -Lang zh-CN
```

| 参数 | 作用 |
|---|---|
| `--host <名字>` | `claude-code`、`codex`、`agents`，不写则自动检测。`--dir <路径>` 可以装进任何 Skill 目录 |
| `--lang zh-CN` | 把完整的中文版安装为 `open-x-sys` |
| `--project` | 装进当前项目，而不是用户主目录 |
| `--without <id>` | 按锁定文件里的 id 留下一个依赖不装；可以重复 |
| `--no-libraries` | 跳过网页库的离线副本 |
| `--deps-only` | 为已经装好的 OpenXSys 安装依赖 |
| `--include-pending` | 把还没有批准的条目也装上。给审查者和测试者用 |
| `--yes` | 不提问。用于自动化；它仍然会打印出自己做的每一件事 |
| `--check` | 什么都不改。报告装了什么、缺什么、有哪些运行环境 |
| `--uninstall` | 移除 OpenXSys，并列出它装过的依赖，附上各自的移除命令 |

PowerShell 版用同样的参数，写法是 `-HostName`、`-Dir`、`-Lang`、`-Project`、`-Without`、`-NoLibraries`、`-DepsOnly`、`-IncludePending`、`-Yes`、`-Check`、`-Uninstall`。

安装器按顺序做的事：

1. **展示**清单、许可证和运行环境，问一次。
2. **安装 OpenXSys**：把 Skill（连同试验场）复制进宿主的 Skill 目录。
3. **安装每个已批准的 Skill**：用 git 取回锁定的那一次提交，检查这个 Skill 文件夹的 git tree id 与锁定文件里的一致，然后从这份校验过的本地副本安装；有 Node.js 22.20 或更高版本时通过 `skills` 命令行工具，否则直接复制。
4. **取回已批准的网页库的离线副本**，放进 `display/lib/`，并检查每个文件的 SHA-256。
5. **检查运行环境**（git、Node.js、Python），说明每个缺少的能多带来什么。它会给出所在平台的安装命令，只有这个人同意才运行。
6. **写下 `installed.json`**，并打印一份小结。

校验不通过的东西一概不装，安装器会说明是哪一个、为什么。**没有自动更新**：新版本只随 OpenXSys 新的、审查过的版本到来。

## 知道什么已经就绪

使用第 2 层的形式之前，检查：

- 安装好的 Skill 里的 `deps/installed.json`（如果有）；
- 宿主列出的 Skill（内置的 Skill 会以它的名字出现在那里）；
- 它需要的运行环境（`node --version`、`python --version` 或 `python3 --version`）。

一个依赖算**就绪**，是 Skill 已经装好，而且它的运行环境在。判断不了时，试最小的一步真实操作，并报告发生了什么。不要假设。

## 缺了东西也能优雅降级

第 0 层是底线，什么都不用装。

- **没有 Node.js**：这个人仍然会得到一个完整的交互网页和一张静态卡片。只说一次，用诚实的一句话说明这个运行环境能多带来什么：“装了 Node.js 的话，这里还会有一支 30 秒的短视频。”以后的运行里不再重复，除非被问到。
- **没有 Python**：概念动画在页面里做；文档和演示稿以网页或 Markdown 交付。
- **没有库的离线副本**：加载锁定的版本并带上完整性校验值，同时说明页面需要联网；或者不用库。
- **什么内置依赖都没有**（就像这个预发布版本）：第 0 层和第 1 层的一切照样能用。

安装缺少的运行环境，或内置清单之外的任何东西，由这个人决定（见 `system/consent.md`）。

## 这个人已经有什么

盘点（`system/parts.md`）会记下这个人已有的 Skill、MCP 服务和工具。它们更合适时，用这个人的。如果这个人已经装了一个也在内置清单里的 Skill，安装器不会动这个人的那一份，并且会说明。

## 信任

- 只使用经过审查的依赖，优先官方发布者。
- 锁定版本并附校验值，安装时校验。
- 不自动更新。
- 依赖文本里出现的命令，不先给这个人看过就绝不运行。
- 一步举报：在 OpenXSys 仓库里开一个 issue，写明是哪个依赖、看到了什么。被举报的项目在审查期间下架。

## 移除

`--uninstall` 会移除 OpenXSys 的 Skill 文件夹，并打印它装过的依赖，以及各自的移除命令（`npx skills remove <名字> -g`，或直接删掉文件夹）。这个人放在 `~/.openxsys/` 和各个项目里的系统属于这个人，安装器从不碰它们；想删就手动删。如果加过宿主指令里的那一行（`system/return.md`），把那一行也删掉。
