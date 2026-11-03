# 安全说明

本技能只做一件事：把本机已有的会话记录整理成文章和图片。全部处理在本地完成。

## 数据流

```
会话记录(.jsonl)  ──读──►  净化  ──►  transcript.md  ──►  文章 / 卡片数据  ──►  PNG
   （本机）              （占位符）    （本机）           （本机）          （本机）
```

没有任何一步向外部发送数据。

| 环节 | 读什么 | 写什么 | 出网 |
| --- | --- | --- | --- |
| `extract_session.py` | 当前会话自身的 `.jsonl` 消息正文 | `transcript.md` | 否 |
| `redact.py` | 内存中的文本 | 不落盘 | 否 |
| `render_cards.py` | `cards.json`、HTML 模板 | PNG / JPG | 否 |

## 会话选择策略

这是本技能最敏感的一步：读错文件就会把别人的对话整理成准备发布的内容。因此定位逻辑是**单一身份来源**，而不是"找一个可用的"。

| 情况 | 行为 |
| --- | --- |
| 运行环境提供了 `CODEBUDDY_SESSION_ID`，且拼出的路径存在 | 只读这一个文件 |
| 变量缺失、格式非法，或路径不存在 | **停止**，返回 `ok=false`，不读取任何会话 |

**脚本不接受任何会话选择器。** 它不提供用于指定会话路径、会话 ID 或工作区目录的参数——不是默认禁止，而是语法上不存在。调用方（包括被诱导的智能体）无法表达"请读那个对话"这个请求。

这带来一个真实的限制：在不注入该变量的客户端里，本技能会直接不可用。这是有意的取舍——宁可停下，也不提供一个能指向任意对话的开关。

明确不做的事：

- 不按修改时间在多个会话里挑「最新的那个」。
- 不跨工作区查找——`~/.workbuddy/projects/` 下每个目录对应一个工作区，跨目录读取等于读别人的对话。
- `--list` 只列当前工作区目录下的文件名与修改时间，**不解析内容**，也不构成读取入口。

`--check` 的输出带 `selection.source` 字段（`session_id` / `explicit`），调用方可以据此向用户说明这次读的到底是哪个文件。

## 权限边界

**文件系统**：只读当前会话那一个 `.jsonl` 文件。只往用户给定的 `--out-dir` 写文件，不写系统目录，不改动原有会话记录。

**网络**：脚本不导入 `urllib`、`requests`、`socket`、`http.client` 等任何网络库，不发起任何请求。截图渲染指向本地 `file://` 地址。

**凭据**：不读取 `~/.ssh`、`.env`、配置文件、密钥链，也不读取任何密钥类环境变量。唯一读取的变量是 `CODEBUDDY_SESSION_ID`，它是会话标识，不是凭据。

**子进程**：仅调用本机已安装的浏览器（Edge / Chrome / Chromium）做无头截图。可执行文件必须通过白名单校验（只能来自固定候选路径或 PATH 中的同名命令），参数以列表传递且 `shell=False`，不经过 shell 解析。

## 输入面

| 入口 | 处理方式 |
| --- | --- |
| 命令行参数 | 只接受输出目录、阈值、尺寸、倍率等值，作为数据处理，不拼进任何 shell 命令 |
| 卡片数据 | 只从磁盘上的 `cards.json` 读取，且必须位于进程当前工作目录内；目录外路径与 `--data -` 都被拒绝 |
| 会话记录 | 唯一的读取入口，且只指向当前会话，见上节 |
| `redact.py` | 纯函数库，**没有命令行入口**，不接收任何文件路径，不存在独立的读取面 |
| MCP / 插件 / 远程资源 | 均无 |

截图命令的每一个元素都由脚本内部生成：浏览器路径来自固定候选清单并通过白名单校验，输出路径与 HTML 路径由 `--out-dir` 与临时目录拼出，尺寸与倍率经整数解析。卡片 JSON 里的文字只进入 HTML，不进入命令行。

## 子进程环境隔离

浏览器子进程**不继承**宿主环境。只透传渲染必需的系统变量：

```
PATH  HOME  LANG  LC_ALL  LC_CTYPE  TERM  TMPDIR
SYSTEMROOT  SYSTEMDRIVE  WINDIR  COMSPEC  PATHEXT  TEMP  TMP
USERPROFILE  APPDATA  LOCALAPPDATA  PROGRAMFILES  PROGRAMFILES(X86)
PROGRAMDATA  NUMBER_OF_PROCESSORS
```

宿主环境里的 `OPENAI_API_KEY`、`*_TOKEN`、`AWS_*` 等变量不会进入子进程。

## 素材净化

会话原始记录里可能夹带密钥、手机号、内网 IP、本机绝对路径。这些内容在写入 `transcript.md` **之前**就被替换为占位符，下游的文章与卡片因此拿不到原文。

| 类别 | 处理 |
| --- | --- |
| API key（`sk-` / `rk-` / `pk-`） | `<REDACTED_API_KEY>` |
| GitHub token（`ghp_` / `gho_` / `ghu_` / `ghs_` / `ghr_`） | `<REDACTED_GITHUB_TOKEN>` |
| AWS Access Key（`AKIA…`） | `<REDACTED_AWS_KEY>` |
| 阿里云 Access Key（`LTAI…`） | `<REDACTED_ACCESS_KEY>` |
| JWT | `<REDACTED_JWT>` |
| 私钥块（`BEGIN … PRIVATE KEY`） | `<REDACTED_PRIVATE_KEY>` |
| `api_key=` / `password:` 等键值对 | `<REDACTED>` |
| 手机号 / 邮箱 / IP | `<REDACTED_PHONE>` / `<REDACTED_EMAIL>` / `<REDACTED_IP>` |
| 本机路径（Windows、macOS、Linux、`~/`） | `<LOCAL_PATH>` |

规则保守：只匹配明确特征，宁可漏掉长串编号，也不误伤正文数字（版本号 `3.12.4`、尺寸 `1080x1440` 不受影响）。

`--no-redact` 可关闭净化，仅建议在完全离线的私人环境使用。

## 已知限制

- 净化基于正则，不做语义判断。自定义格式的密钥（如无前缀的随机字符串）可能漏过。
- 会话记录本身由客户端写入，本技能只读取、不回写，因此不会修改既有数据。
- 卡片截图经本机浏览器渲染，HTML 内容来自本技能模板 + 用户提供的卡片数据，不加载任何外部资源（无远程字体、无远程图片、无统计脚本）。

## 报告问题

发现安全问题请开 issue，不要附带真实密钥或他人隐私数据。
