# 禅道 Bug 分析执行检查清单

> ⚠️ 硬约束：分析开始前通读本清单，每步必须逐项完成，缺一不可。

## 执行检查清单

- [ ] 步骤 1：消息解析（提取 Bug ID）

- [ ] 步骤 2：重复分析检查
  - 登录禅道（`zentao-login.js`，获取 WS endpoint，一个 Bug 全程复用）
  - 获取 Bug 详情 + 检查重复评论（`zentao-get-bug.js`，有我的评论 → 飞书询问是否重新分析）

- [ ] 步骤 3：模块分类（按 config aliases 子串硬匹配，不在范围 → 飞书通知 + 终止）

- [ ] 步骤 4a：下载附件（`zentao-download-files.js`）

- [ ] 步骤 4b：确定 Bug 发生时间（Bug 描述文本 > 附件截图/视频系统时间 > 飞书询问。禁止用文件名/创建时间推断）

- [ ] 步骤 4c-1：按 config commit_extract 规则提取 commit id（搜不到 → 飞书通知 + 终止，禁止近似匹配）

- [ ] 步骤 4c-2：`git branch --contains <commit-id>` 记录分支信息

- [ ] 步骤 4c-3：`git checkout <commit-id>` + `git submodule update --init --recursive`

- [ ] 步骤 4d：AI 深度分析（结合 Bug 详情 + 日志 + 代码 + 历史评论）

- [ ] 🔴 步骤 5：输出报告
  - ⚠️ 先检查 config 中 `auto_comment` 字段（默认 `true`）
  - `auto_comment === true` 或未配置：
    - 步骤 5a：禅道评论（先 `zentao-build-comment.js` 生成 HTML，再 `zentao-post-comment.js --comment-file=<file>` 发布）
  - `auto_comment === false`：跳过禅道评论，仅生成 `report.md`

- [ ] 步骤 5b：飞书摘要（简要结果 + Bug 链接）

- [ ] 🔴 步骤 6：清理 — 必须完成！
  1. `taskkill /PID <login-PID> /F /T`（PID 来自 `zentao-login.js` 输出行 `PID=<value>`，`/T` 连带杀 Chrome 子进程树）
  2. `git worktree list` 检查是否有 `.claude/worktrees/bug-{bug_id}/` 残留，有则 `git worktree remove <path>` 清理
  3. `Get-Process node` 检查无 `zentao-*.js` 残留进程，有则 `taskkill /F /PID <pid>` 清理
  4. 确认只剩 OpenClaw 自身 node 进程（gateway/worker）
