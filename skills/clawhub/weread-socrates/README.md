# weread-socrates · AI 伴读 · 苏格拉底式阅读教练

v1.3.1 是一个只在本机运行的阅读 Web 应用：可连接微信读书和用户自己的大模型，也可在完全无 Key 的 Demo 模式下体验完整流程；新增本地 Reader Memory Graph，用于持续沉淀跨书阅读记忆。

## v1.3.1 功能

| 能力 | 说明 |
|---|---|
| 一键启动与配置诊断 | `bash scripts/start.sh` 会先运行脱敏诊断；`--check` 仅诊断，`--demo` 强制 Demo；服务从不自动打开浏览器 |
| 无 Key Demo | 未配置微信读书 Key 时使用内置示例书和划线；未配置模型 Key 时使用本地确定性导图、五轮提问与小结，不发送内容 |
| 微信读书流程 | 搜书、整书结构导图、热门划线、我的划线/想法，保持 v1.2.0 流程兼容 |
| 苏格拉底对话 | 5 轮递进提问、会话恢复、小结和带出处 Markdown 笔记导出 |
| Reader Memory Graph | 本机保存概念、立场、未解问题；按共同标签生成跨书连接；支持逐条删除、经一次性 token 确认的全部删除和 JSON 导出 |

## 快速开始

唯一硬性依赖是 Node.js v16+。

```bash
bash scripts/start.sh
```

服务不会自动打开浏览器；请手动访问 `http://localhost:3456`。未配置任何 Key 时会直接进入 Demo，不再阻塞功能体验。

常用命令：

```bash
bash scripts/start.sh --check     # 只做脱敏诊断
bash scripts/start.sh --demo      # 强制无 Key Demo
bash scripts/stop.sh              # 按 PID 精准停止
```

## 可选配置

微信读书 Key 可通过当前环境变量、Skill 根目录 `.env.local`或 `~/.config/weread-socrates/config`提供：

```bash
export WEREAD_API_KEY=你的微信读书APIKey
```

启动脚本只逐行读取 `WEREAD_API_KEY=`，不会 source 或执行配置文件。模型 Key 在页面右上角设置中填写，仅保存在浏览器 localStorage。缺失任一 Key 都有安全的 Demo 降级。

## Reader Memory Graph

1. 搜索并选择一本书（也可不关联书籍直接记录）。
2. 选择「概念 / 立场 / 未解问题」，填写内容和逗号分隔标签。
3. 相同标签出现在不同书籍时，页面自动显示跨书连接。
4. 可导出 `reader-memory.md` 或 `reader-memory.json`，也可逐条或全部删除。

数据默认写入 `~/.weread-socrates/reader-memory.json`，目录权限为 700、文件权限为 600。可用 `WEREAD_SOCRATES_DATA_DIR` 改变位置。

## 安全与隐私

- HTTP 服务固定监听 `127.0.0.1`；`PORT` 只改变端口，不改变监听地址。
- 微信读书代理仅允许 6 个只读接口，并裁剪到白名单参数；请求体限制为 64 KiB。
- `/api/status` 与 `/api/diagnostics` 仅返回布尔配置状态，不回显 Key。
- Demo 模式不访问微信读书或大模型供应商。
- 模型 Key 仅在浏览器 localStorage 中；只有用户主动调用在线模型时，所选原文才会发往所选供应商。
- Memory 文本做长度、类型和控制字符校验；前端显示时转义；服务端原子写入本机文件。
- 不读取任何 shell 启动配置；仅解析当前环境、`.env.local` 与专用 config，且从不执行配置文件。
- 读取微信读书个人数据和向在线模型外发数据分别要求用户明确同意。
- 全部删除 Memory 需要 60 秒有效的一次性确认 token；逐条删除不受影响。
- 不捆绑压缩 Mermaid；结构图由可审查的原生 JavaScript 以纯文本安全渲染，并可通过 Canvas 导出 PNG。

## 兼容性

搜书、个人/热门划线、五轮对话、安全结构图、PNG 与 Markdown 笔记导出保持可用。已配置 Key 的用户启动方式不变。

## 项目结构

```text
weread-socrates/
├── SKILL.md
├── README.md
├── skill-card.md
├── assets/
│   ├── ai-reading-companion.html
│   ├── server.js
│   ├── app.css
│   └── app.js
├── references/weread-api.md
└── scripts/
    ├── start.sh
    ├── doctor.sh
    └── stop.sh
```

## 开发与验证

```bash
node --check assets/server.js
bash -n scripts/start.sh scripts/doctor.sh scripts/stop.sh
bash scripts/start.sh --check
```

服务启动后可检查 `/api/status`、Demo 搜索、Memory 增删导出和非法接口拒绝。测试时建议设置临时 `WEREAD_SOCRATES_DATA_DIR`，避免影响真实阅读记忆。

## 中文定位

这是面向中文用户、中文书籍与中文交互习惯设计的本地阅读辅助工具，不是微信读书官方产品。默认 Demo 不外发；在线服务的数据处理地域和条款以微信读书及所选模型供应商为准。

## 版本历史

- **v1.3.1** — ClawHub 安全重构：移除自动打开浏览器与 shell 启动配置读取、移除 bundled Mermaid、拆分前端、增加外发同意和批量删除 token
- **v1.2.0** — 个人划线/想法、流式对话、会话恢复、读书小结、带出处笔记导出
- **v1.1.x** — 安全审核与加固
- **v1.0.0** — 首个版本

## License

MIT。导出的笔记和记忆可能包含受版权保护的原文，仅供个人学习，请勿公开传播。

- GitHub：https://github.com/bonniegeng-max/weread-socrates
- ClawHub：https://clawhub.ai/bonniegeng-max/skills/weread-socrates
