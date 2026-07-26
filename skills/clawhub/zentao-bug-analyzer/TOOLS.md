# zentao-bug-analyzer 工具与环境

## 环境依赖

- **Node.js** 18+（脚本运行）
- **Playwright**：`npm install playwright && npx playwright install chromium`
- **Git** 2.5+（`git worktree`、`git branch --contains`）
- 禅道服务器可访问：`http://zentao.gxatek.com:20080`

## 禅道交互 · 统一 Playwright 模式

企业版 12.1 不支持 Bearer Token，所有操作在同一 Playwright 会话中完成。通过 `scripts/` 下的 5 个固定脚本实现，一个脚本一个功能。

### 单会话铁律

一个 Bug 全程只启动一次 Playwright 浏览器。登录后读详情、下载附件、写评论全部复用同一 `browser`/`page`/`context`。

### 脚本

| 脚本 | 功能 | 用法 |
|------|------|------|
| `scripts/zentao-login.js` | 登录禅道，输出 WS endpoint | `node scripts/zentao-login.js [--port=9224]` |
| `scripts/zentao-get-bug.js` | 获取 Bug 详情 JSON | `node scripts/zentao-get-bug.js --ws=<WS> --bug-id=<id>` |
| `scripts/zentao-download-files.js` | 下载 Bug 附件到本地 | `node scripts/zentao-download-files.js --ws=<WS> --bug-id=<id> --dir=<dir>` |
| `scripts/zentao-build-comment.js` | Markdown 报告 → HTML 评论 | `node scripts/zentao-build-comment.js <report.md> [--out <output.html>]` |
| `scripts/zentao-post-comment.js` | 发布 Bug 评论 | `node scripts/zentao-post-comment.js --ws=<WS> --bug-id=<id> --comment-file=<path>` |

### 典型调用流程

```
1. node scripts/zentao-login.js --port=9224
   → WS=ws://localhost:9224/devtools/browser/{id}, PID={pid}

2. node scripts/zentao-get-bug.js --ws={WS} --bug-id=1432606
   → JSON (stdout)

3. node scripts/zentao-download-files.js --ws={WS} --bug-id=1432606 --dir=bugs/1432606
   → 文件路径列表 (stdout)

4. node scripts/zentao-build-comment.js bugs/1432606/report.md --out bugs/1432606/comment.html
   → HTML 文件路径 (stdout)

5. node scripts/zentao-post-comment.js --ws={WS} --bug-id=1432606 --comment-file=bugs/1432606/comment.html
   → OK / FAIL
```

### login 脚本输出格式

`zentao-login.js` 输出两行 key=value（可直接 shell `eval`）：

```
WS=ws://localhost:9224/devtools/browser/{browser-id}
PID={chromium-pid}
```

其他脚本通过 `--ws` 参数复用会话。

### 参数说明

- `--ws`：login 脚本返回的 WebSocket endpoint
- `--bug-id`：禅道 Bug ID（数字）
- `--dir`：附件下载目标目录（自动创建）
- `--comment-file`：评论文件路径（推荐，由 build-comment.js 生成的 HTML 文件）
- `--comment`：评论内容（原始 HTML 字符串，脚本自动编码。备选方案，推荐用 `--comment-file`）
- `--port`：CDP 调试端口（默认 9224）
- `--zentao-url`：禅道实例地址（默认 `http://zentao.gxatek.com:20080`）

## 本文件定位

TOOLS.md 仅放环境依赖和脚本用法。完整 API 参考见 `references/zentao-api-reference.md`，流程规范见 `SKILL.md`。
