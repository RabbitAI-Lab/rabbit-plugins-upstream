# 常见失败场景与处理

## 通用原则

- **任何 step 失败** → 立即写 `step_failed` 事件到 session，中断流程
- **明确暂态错误**（如 SSO 过期）→ 引导用户修复后回复"继续"，不自动重试
- **不确定的错误** → 原样把错误信息呈现给用户，不猜测

## 常见场景

### 1. SSO 过期（401）

**触发**：任何 ee-cli 命令返回 401 或 stderr 含 "SSO token expired"。

**处理**：

> "检测到 SSO 已过期。请执行 `ee-cli login` 完成登录后回复'继续'。"

### 2. workItem 类型是 task，无法关联

**触发**：阶段 ③ Step 3.2「关联工作项」时 `session.workItem.type == 'task'`。

**处理**：**自动补建服务端子任务**（`ee-cli pingcode workitem create --work-item-type subtask ...`，父任务的 workspace/owner/business_line 全部沿用），然后用新子任务 id 关联 MR。**不要阻塞用户**。详见 `flow.md` Step 3.2。

**为什么不是 cliMissing**：CLI 层的 `associate` 命令的确应该校验类型（当前允许绑 task 是 CLI 行为 bug），但从 skill 视角看，绑不了就自动建子任务是更优的流程编排，不需要等 CLI 修。

### 3. CI 部署失败：image_tag 不能为空

**触发**：阶段 ④ Step 4.1 若尝试用 `ci run` 触发失败，报此错。

**处理**：确认 CLI 无法自动填部署参数。回退到人工阻塞路径（Step 4.1 的标准流程），追加 `cliMissing`: `"ci run 不支持部署参数透传"`。

### 4. cr merge 返回空字符串（伪成功）

**触发**：`ee-cli cr merge <mrIid>` 返回 `""` 且 exit 0。

**处理**：不要相信返回值，立即 `cr status <mrIid> --skip-checks` 复核 `state`。若非 `merged` → 追加 `cliMissing`: `"cr merge 失败时返回空字符串"`，向用户报告实际状态与 blockingReasons。

### 5. Skill 调用失败

**触发**：`Skill(pingcode-assistant-pro)` 或 `Skill(hi-docs)` 抛错。

**处理**：把子 skill 报错原样展示给用户，让用户决定是否切换成手动模式（用户自己去 PingCode / REDoc 网页做该步骤，然后回复"继续"）。

### 6. Session 文件损坏

**触发**：读 `~/.claude/e2e-sessions/<id>.json` 时 JSON 解析失败。

**处理**：备份为 `<id>.json.corrupted.<timestamp>`，询问用户"session 已损坏，重开还是放弃？"。

### 7. 用户中途放弃

**触发**：用户明确说"我不想继续了"或类似意图。

**处理**：写 `session.status = 'aborted'` + 追加 `session_aborted` 事件（可选），询问是否需要根据已有数据先生成一份"中止报告"。
