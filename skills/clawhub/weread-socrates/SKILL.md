---
name: weread-socrates
description: 启动本地 AI 伴读，支持无 Key Demo、微信读书深读、苏格拉底对话与 Reader Memory Graph。用户要启动阅读教练、诊断配置、整理跨书概念/立场/问题时使用。
version: 1.3.1
metadata:
  openclaw:
    requires:
      bins:
        - node
    envVars:
      - name: WEREAD_API_KEY
        required: false
        description: 可选；配置后启用微信读书实时搜书和个人数据，缺失时进入 Demo
      - name: WEREAD_SOCRATES_DATA_DIR
        required: false
        description: 可选；Reader Memory 本地数据目录
    network:
      - host: i.weread.qq.com
        purpose: 仅配置微信读书 Key 后调用 6 个白名单只读接口
      - host: user-configured
        purpose: 仅用户配置并主动使用在线模型后调用智谱或 DeepSeek
    filesystem:
      - path: <skill_dir>/.env.local ~/.config/weread-socrates/config
        purpose: 仅解析 WEREAD_API_KEY；不读取或执行任何 shell profile
      - path: ~/.weread-socrates/reader-memory.json
        purpose: 本地 Reader Memory Graph，默认目录 700、文件 600
      - path: <skill_dir>/assets/.server.pid
        purpose: 精准停止本应用进程
    emoji: 📚
    homepage: https://github.com/bonniegeng-max/weread-socrates
---

# weread-socrates v1.3.1

本地 AI 阅读教练。保持 v1.2.0 微信读书深读流程，并加入启动诊断、无 Key Demo 和本地 Reader Memory Graph。

## 何时使用

用户说「启动 AI 伴读」「打开阅读教练」「诊断配置」「用伴读读一本书」「整理跨书概念」「记录阅读立场/未解问题」或提出微信读书深读需求时使用。

## 启动

1. 将本文件所在目录视为 Skill 根目录。
2. 一键诊断并启动：
   ```bash
   bash scripts/start.sh
   ```
3. 只诊断：`bash scripts/start.sh --check`。
4. 强制 Demo：`bash scripts/start.sh --demo`。
5. 验证 `http://localhost:3456/api/status` 的 `ok`、`mode`、`host` 和 `memory.writable`。

必须使用 Node.js v16+。微信读书 Key 和模型 Key 都是可选项；无 Key 时不可要求用户先配置，直接说明将运行 Demo。

## 配置与模式

- 微信读书 Key：环境变量 `WEREAD_API_KEY`。也可写入 `.env.local` 或 `~/.config/weread-socrates/config`。启动器只读键值，不执行配置文件。
- 模型 Key：页面「设置」中配置，存浏览器 localStorage。
- 在线模式：有微信读书 Key 时调用实时只读数据；有模型 Key 时调用用户选择的模型。
- Demo 模式：缺少微信读书 Key 时返回内置示例书；缺少模型 Key 时本地生成确定性导图、五轮问题与小结，不外发内容。

## Reader Memory Graph

页面底部可记录三类节点：

- `concept`：概念
- `stance`：读者立场
- `question`：未解问题

每条节点可关联当前书和标签。相同标签跨越不同书籍时自动显示跨书连接。支持逐条删除、需一次性确认 token 的全部删除和 JSON 导出。数据默认位于 `~/.weread-socrates/reader-memory.json`。

## 旧流程兼容

在线模式支持：搜书 → 安全纯文本结构图 → 热门/个人划线 → 5 轮对话 → Markdown 笔记；PNG 导出保留。

## 安全要求

- 服务必须仅监听 `127.0.0.1`，不得改为 `0.0.0.0`。
- 代理仅放行 `/store/search`、`/book/info`、`/book/chapterinfo`、`/book/bestbookmarks`、`/book/bookmarklist`、`/review/list/mine`。
- 诊断和状态接口不得返回 Key 或其片段。
- Memory API 仅接受 GET/POST/DELETE；限制请求体、字段类型/长度，原子写入；页面渲染全部转义。
- 启停脚本只管理 PID 文件记录的本应用进程，不误杀其他端口进程。
- 读取微信读书个人划线/想法前必须取得明确同意；向在线模型外发书籍信息、原文或回答前必须另行取得明确同意。
- 批量删除 Reader Memory 必须申请、回输并校验 60 秒有效的一次性确认 token。
- 不捆绑压缩的第三方渲染库；结构图使用可审查的原生文本/Canvas 渲染，模型输出按纯文本处理。
- 导出内容可能含受版权保护原文，仅供个人学习。

## 中文定位

本 Skill 是面向中文用户和中文书籍阅读场景的本地辅助工具，不是微信读书官方产品。界面、诊断、隐私提示和错误信息均以中文为主；外部服务的可用地区、条款和数据处理规则由各供应商决定。

## 故障排查

| 现象 | 处理 |
|---|---|
| Node.js 不可用 | 安装 v16+ 后运行 `bash scripts/start.sh --check` |
| 未配置 Key | 正常进入 Demo；如需实时数据再配置并重启 |
| 端口 3456 占用 | 先运行 `bash scripts/stop.sh`；若非本应用，手动处理占用进程 |
| Memory 不可写 | 检查 `~/.weread-socrates` 或 `WEREAD_SOCRATES_DATA_DIR` 权限 |
| 页面无法连接 | 使用同一台机器浏览器访问 `http://localhost:3456`，不要依赖远程 Preview |

## 停止

终端按 `Ctrl+C`，或运行 `bash scripts/stop.sh`。

接口细节见 `references/weread-api.md`；前端在 `assets/ai-reading-companion.html`，服务端在 `assets/server.js`。
