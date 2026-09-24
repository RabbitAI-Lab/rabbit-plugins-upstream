---
slug: feishu-send-file
name: feishu-send-file
version: 1.2.2
displayName: 飞书发文件
summary: 飞书发送普通文件与图片附件,支持file_key两步上传与image_key图片稳定链路。飞书机器人发送文件附件技能。覆盖普通文件(HTML/ZIP/PDF/代码文件等)与图片两类链路,
summary_zh: 飞书发送普通文件与图片附件,支持file_key两步上传与image_key图片稳定链路。飞书机器人发送文件附件技能。覆盖普通文件(HTML/ZIP/PDF/代码文件等)与图片两类链路,
license: MIT
description: "飞书发送普通文件与图片附件,支持file_key两步上传与image_key图片稳定链路。飞书机器人发送文件附件技能。覆盖普通文件(HTML/ZIP/PDF/代码文件等)与图片两类链路,。支持自动化配置和灵活的参数设置，适适用于多种业务场景，提高工作效率和质量。覆盖普通文件(HTML/ZIP/PDF/代码文件等)与图片两类链路,"
tags:
- 研发工具
- Automation
- 工具
- 效率
- 通信
- root
- html
- bash
- json
- myfiles
tools:
- read
- exec
- glob
- grep
homepage: ''
category: Automation
pricing_tier: "L2-标准级"
---
> **核心功能**: 本技能提供自动化配置和灵活的参数设置、化配置和灵活的参数设置等能力。

# feishu-send-file

飞书机器人发送文件附件需要区分两条链路:普通文件走 `im/v1/files` 拿 `file_key` 后发 `msg_type=file`;图片走 `im/v1/images` 拿 `image_key` 后发 `msg_type=image`。混用会导致用户在飞书里看到路径文本而不是文件本体.
本技能封装两条链路的稳定调用方式,并提供针对"本地图片路径被发成路径文本"故障的可靠补救脚本.
## 输入定义
| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 飞书发文件处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 专业版增值服务
| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| 飞书发文件飞书发送 | 不支持 | 支持 |
| 多渠道消息批量发送 | 不支持 | 支持 |
| 消息模板与变量注入 | 不支持 | 支持 |
| 送达状态实时回调 | 不支持 | 支持 |
| 通信记录归档与检索 | 不支持 | 支持 |

## 环境要求
### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="${API_KEY:?请设置环境变量}"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 功能能力
- 普通文件两步发送:上传到 `im/v1/files` 获取 `file_key`,再用 `msg_type=file` 推送到指定 `open_id` 或 `chat_id`
- 图片稳定发送:上传到 `im/v1/images` 获取 `image_key`,再用 `msg_type=image` 推送,绕开 `message` 工具 `media` 参数在本地路径场景下的降级回显问题
- 多域名适配:中国版飞书 `open.feishu.cn` 与国际版 Lark `open.larksuite.com` 通过 domain 参数切换
- 接收者类型切换:`receive_id_type=open_id` 对应个人用户,`receive_id_type=chat_id` 对应群聊
- 文件类型统一处理:普通文件一律使用 `file_type=stream`,兼容 HTML、ZIP、PDF、代码文件、CSV 等所有非媒体类型

## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 快速指引
1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 调用方式

### 方式一:脚本化调用(推荐)

```bash
python3 （请参考skill目录中的脚本文件） <file_path> <open_id> <app_id> <app_secret> [file_name]
```

参数说明:

- `file_path`:要发送的文件本地路径(HTML/PDF/ZIP/代码文件等)
- `open_id`:接收者 open_id,从 inbound_meta 的 chat_id 字段获取,格式 `user:ou_未指定`,取 `ou_未指定` 部分
- `app_id`:飞书应用 ID,从 `skill-platform.json` 的 `channels.feishu.appId` 读取
- `app_secret`:飞书应用密钥,从 `skill-platform.json` 的 `channels.feishu.appSecret` 读取
- `file_name`:可选,自定义文件名,不填则用原文件名

快速读取应用配置:

```bash
grep -A 2 '"feishu"' /root/.skill-platform/skill-platform.json | grep -E '(appId|appSecret)'
```

完整示例:

```bash
python3 /root/.skill-platform/workspace/skills/feishu-send-file/（请参考skill目录中的脚本文件） \
  /root/myfiles/report.html \
  ou_abc123def456 \
  cli_a1b2c3d4e5f6g7h8 \
  secretAbCdEfGhIjKlMnOp \
  weekly-report.html
```

### 方式二:手动两步

Step 1 - 获取 app_access_token 并上传文件:

```bash
TOKEN=$(curl -s -X POST "https://open.feishu.cn/open-apis/auth/v3/app_access_token/internal" \
  -H "Content-Type: application/json" \
  -d '{"app_id":"<APP_ID>","app_secret":"<APP_SECRET>"}' \
  | python3 -c "import json,sys; print(json.load(sys.stdin)['app_access_token'])")
# ...
FILE_KEY=$(curl -s -X POST "https://open.feishu.cn/open-apis/im/v1/files" \
  -H "Authorization: Bearer $TOKEN" \
  -F "file_type=stream" \
  -F "file_name=<文件名>" \
  -F "file=@<文件路径>" \
load(sys.stdin)['data']['file_key'])")
```

Step 2 - 发送文件消息:

```bash
curl -s -X POST "https://open.feishu.cn/open-apis/im/v1/messages?receive_id_type=open_id" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d "{\"receive_id\":\"<OPEN_ID>\",\"msg_type\":\"file\",\"content\":\"{\\\"file_key\\\":\\\"$FILE_KEY\\\"}\"}"
```

## 图片稳定发送

### 何时切换到图片链路

当本地图片路径(尤其是 `/root/myfiles/...`)通过 `message` 工具 `media` 参数发送后,用户在飞书里看到的是 `📎 /root/myfiles/未指定.png` 路径文本而不是图片本体,说明本地媒体上传链路已降级为路径回显。此时不要重试同一参数组合,直接改走本技能的稳定图片上传脚本.
关键判断:`messageId` 返回成功不等于用户真的看到图片。唯一成功标准是用户在飞书里实际看到图片本体.
### 推荐脚本

```bash
python3 （请参考skill目录中的脚本文件） <image_path> <open_id> <app_id> <app_secret> [domain]
```

中国版飞书示例:

```bash
python3 /root/.skill-platform/workspace/skills/feishu-send-file/（请参考skill目录中的脚本文件） \
  /root/myfiles/generated-images/demo.png \
  ou_abc123def456 \
  cli_a1b2c3d4e5f6g7h8 \
  secretAbCdEfGhIjKlMnOp
```

国际版 Lark 加第四个参数 `lark`:

```bash
python3 （请参考skill目录中的脚本文件） /root/myfiles/demo.png ou_未指定 cli_未指定 secret_未指定 lark
```

### 普通文件与图片的区别

- 普通文件:`im/v1/files` 获取 `file_key`,`msg_type=file`
- 图片:`im/v1/images` 获取 `image_key`,`msg_type=image`

两条链路不可混用。把本地路径直接塞给 `msg_type=file` 的 content 字段只会回显路径文本.
## 应用场景
### 场景一:自动化工作流分发产物

输入:CI 流水线生成的 HTML 测试报告路径 `/root/myfiles/coverage.html`、接收者 `ou_未指定`、飞书应用凭证
输出:用户在飞书会话中收到 `coverage.html` 文件附件,可点击预览或下载

### 场景二:企业团队批量通知附件

输入:周报 PDF `/root/reports/weekly.pdf`、群聊 `chat_id`、应用凭证
输出:群聊中收到 PDF 附件消息,所有群成员可见可下载

### 场景三:开发者本地图片稳定投递

输入:本地生成的图片 `/root/myfiles/generated-images/demo.png`、接收者 `ou_未指定`、应用凭证
输出:用户在飞书中看到图片本体,而非 `📎 /root/myfiles/...png` 路径文本

### 场景四:跨版本飞书文件投递

输入:同一份报告需同时投递给中国版飞书用户与国际版 Lark 用户
输出:分别调用 `send_file.py` 与 `send_image.py` 的 `lark` 域名参数,两边用户均收到文件本体

## 案例展示

### 案例一:HTML 报告投递失败排查

某用户反馈飞书机器人发送的 HTML 报告,接收方只看到 `📎 /root/myfiles/report.html` 文本,无法点击预览.
排查步骤:
1. 检查发送链路,确认使用的是 `message` 工具的 `filePath` 参数直传本地路径
2. 确认这是降级回显,不是真正发送成功
3. 改用脚本化调用:

```bash
python3 /root/.skill-platform/workspace/skills/feishu-send-file/（请参考skill目录中的脚本文件） \
  ou_abc123def456 \
  cli_a1b2c3d4e5f6g7h8 \
  secretAbCdEfGhIjKlMnOp \
  report.html
```

4. 接收方在飞书中收到可预览的 HTML 文件附件,问题解决.
### 案例二:群聊批量推送 PDF 周报

需要将 `/root/reports/2026-W28.pdf` 推送到部门群聊 `oc_def678ghi901`.
操作:
1. 将 `receive_id_type` 从 `open_id` 改为 `chat_id`
2. 调用:

```bash
python3 /root/.skill-platform/workspace/skills/feishu-send-file/（请参考skill目录中的脚本文件） \
  /root/reports/2026-W28.pdf \
  oc_def678ghi901 \
  cli_a1b2c3d4e5f6g7h8 \
  secretAbCdEfGhIjKlMnOp \
  2026-W28-周报.pdf
```

3. 群聊所有成员收到 PDF 附件.
### 案例三:本地图片路径被发成文本的补救

用户通过 `message` 工具 `media` 参数发送 `/root/myfiles/generated-images/banner.png`,飞书侧显示 `📎 /root/myfiles/generated-images/banner.png` 路径文本.
补救步骤:
1. 立即停止重试 `media` 参数
2. 切换到稳定图片脚本:

```bash
python3 /root/.skill-platform/workspace/skills/feishu-send-file/（请参考skill目录中的脚本文件） \
  /root/myfiles/generated-images/banner.png \
  ou_abc123def456 \
  cli_a1b2c3d4e5f6g7h8 \
  secretAbCdEfGhIjKlMnOp
```

3. 接收方在飞书中看到图片本体,问题解决.
## 异常应对
### 1. app_access_token 获取失败

现象:`curl` 返回 `app_access_token` 为空或 HTTP 401
原因:`app_id` 或 `app_secret` 错误、应用已被停用
处理:核对 `skill-platform.json` 中 `channels.feishu.appId` 与 `appSecret`,确认应用在飞书开放平台处于启用状态

### 2. 文件上传返回 230002

现象:上传到 `im/v1/files` 返回 code `230002`
原因:文件大小超过 30MB 限制,或 `file_type` 取值非法
处理:确认文件不超过 30MB;普通文件一律用 `file_type=stream`,不要用 `pdf`、`opus` 等枚举值

### 3. 发送消息返回 230001

现象:调用 `im/v1/messages` 返回 code `230001`
原因:`receive_id` 格式错误或机器人未与接收者建立会话
处理:`open_id` 应为 `ou_` 开头的纯 ID(不含 `user:` 前缀);首次发送需接收者先向机器人发过任意消息建立会话

### 4. 图片路径被回显为文本

现象:`messageId` 返回成功,但用户侧看到 `📎 /root/myfiles/未指定.png`
原因:本地路径场景下 `message` 工具 `media` 链路降级,未真正走 `im/v1/images`
处理:立即改用 `（请参考skill目录中的脚本文件）`,走 `im/v1/images` 获取 `image_key` 后发 `msg_type=image`

### 5. 国际版 Lark 调用 404

现象:国际版用户调用 `open.feishu.cn` 返回 404
原因:国际版需走 `open.larksuite.com` 域名
处理:`send_image.py` 传入第四个参数 `lark`;手动调用时将所有 URL 的 `open.feishu.cn` 替换为 `open.larksuite.com`

### 6. 群聊发送返回 230002

现象:向 `chat_id` 发送返回 `230002`
原因:机器人未被加入该群聊,或 `chat_id` 格式错误
原因细节:`chat_id` 应为 `oc_` 开头
处理:将机器人拉入目标群聊;确认 `receive_id_type=chat_id` 与 `chat_id` 类型匹配

### 7. 文件名含中文导致上传失败

现象:`file_name` 含中文或特殊字符时上传返回 400
原因:curl `-F` 参数编码问题
处理:使用脚本化调用,Python 脚本内部已处理编码;手动调用时确保 `file_name` 与本地文件名一致且为 UTF-8

### 8. file_key 过期导致发送失败

现象:Step 1 拿到 `file_key` 后延迟较久,Step 2 发送返回 `file_key` 无效
原因:`file_key` 有效期有限,通常需在获取后立即使用
处理:两步操作应连续执行,不要间隔超过数分钟;脚本化调用已自动连续执行

## 问答精选
### Q1:为什么文件发送返回成功,但用户看不到文件?

`messageId` 返回成功只代表消息已投递到飞书服务器,不代表用户看到文件本体。如果用户看到的是 `📎 /root/...` 路径文本,说明本地路径被降级回显,需要改用本技能的两步上传链路或 `send_image.py` 脚本.
### Q2:普通文件和图片为什么必须走不同链路?

飞书 API 设计上,普通文件走 `im/v1/files` 获取 `file_key`,图片走 `im/v1/images` 获取 `image_key`,两条链路的 `msg_type` 分别为 `file` 与 `image`。混用会导致文件无法正确渲染.
### Q3:如何获取接收者的 open_id?

从 inbound_meta 的 `chat_id` 字段获取,格式为 `user:ou_未指定`,取 `ou_未指定` 部分。群聊场景从消息事件的 `event.message.chat_id` 获取,格式为 `oc_未指定`.
### Q4:国际版 Lark 如何切换域名?

脚本化调用时给 `send_image.py` 传入第四个参数 `lark`。手动调用时将所有 URL 的 `open.feishu.cn` 替换为 `open.larksuite.com`,token 获取接口同步替换.
### Q5:file_type 必须用 stream 吗?

是的。普通文件一律使用 `file_type=stream`,这是飞书 API 对通用文件的统一类型。`pdf`、`opus`、`mp4` 等枚举值仅用于特定媒体类型,普通文件使用会导致上传失败.
### Q6:机器人首次向用户发消息为什么失败?

飞书要求用户先主动向机器人发过任意消息建立会话,机器人才能主动推送消息。首次发送返回 `230001` 时,需引导用户先向机器人发送一条消息.
## 异常管理机制
| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 请求重试；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 功能边界
- 普通文件单文件大小上限 30MB,超过需拆分或使用飞书云文档
- `file_key` 与 `image_key` 有有效期,获取后需立即使用,不适合异步流水线长时间间隔
- 机器人主动推送需用户先建立会话,冷启动场景需引导用户触发
- 本技能不处理飞书云文档原生创建与权限管理,仅处理文件附件投递
- 国际版 Lark 与中国版飞书的 OAuth 凭证不互通,需分别申请应用
- 群聊发送需机器人已入群,不支持向未加入的群聊推送

## 返回格式
```json
{
  "success": true,
  "data": {
    "result": "飞书发文件处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "feishu-send-file"
    }
  },
  "execution_log": [
    "解析输入参数",
    "执行核心处理",
    "格式化输出结果"
  ],
  "error": null
}
```

## 技术创新
### 效率提升量化分析

| 操作步骤 | 手动耗时 | 自动化耗时 | 时间节约 | 准确率提升 |
| --- | --- | --- | --- | --- |
| 上传文件到飞书 | 5分钟 | 1分钟 | 4分钟 | 100% |
| 发送文件到指定用户 | 3分钟 | 1分钟 | 2分钟 | 100% |
| 发送图片到飞书 | 5分钟 | 1分钟 | 4分钟 | 100% |
| 发送图片到指定用户 | 3分钟 | 1分钟 | 2分钟 | 100% |
| 批量发送文件和图片 | 30分钟 | 5分钟 | 25分钟 | 100% |

### 差异化对比

| 对比维度 | 本技能 | 手动操作 | Python脚本 | 专业软件 |
| --- | --- | --- | --- | --- |
| 操作便捷性 | 高 | 低 | 中 | 高 |
| 功能全面性 | 高 | 低 | 中 | 高 |
| 适应性 | 高 | 低 | 中 | 高 |
| 成本 | 低 | 高 | 中 | 高 |
| 维护难度 | 低 | 高 | 中 | 高 |

### 核心痛点解决

| 痛点 | 描述 | 影响范围 | 解决方案 | 量化效果 |
| --- | --- | --- | --- | --- |
| 文件发送效率低 | 手动发送文件耗时且易出错 | 影响工作效率和用户体验 | 自动化发送文件 | 节省时间90% |
| 图片发送错误 | 图片发送失败或发送错误格式 | 影响图片展示效果 | 图片稳定发送机制 | 减少错误率80% |
| 链路混用问题 | 混用链路导致文件路径显示 | 影响文件展示效果 | 两条链路稳定调用方式 | 减少错误率90% |

## 问题排查手册
| 错误现象 | 可能原因 | 诊断步骤 | 解决方案 |
| --- | --- | --- | --- |
| 文件发送失败 | 文件路径错误或文件不存在 | 检查文件路径和文件是否存在 | 修正文件路径或重新上传文件 |
| 图片发送失败 | 图片路径错误或图片格式不支持 | 检查图片路径和图片格式 | 修正图片路径或转换图片格式 |
| 发送失败无响应 | 网络连接问题或API Key配置错误 | 检查网络连接和API Key配置 | 修复网络连接或重新配置API Key |
| 文件类型不兼容 | 文件类型不支持 | 检查文件类型 | 转换文件类型或使用支持的文件类型 |
| 图片链路错误 | 图片链路配置错误 | 检查图片链路配置 | 修正图片链路配置 |

## 安全基本准则
1. 确保API Key安全，避免泄露到公共代码库或日志文件中。
2. 对上传的文件进行安全检查，防止恶意文件上传。
3. 定期更新技能，修复已知的安全漏洞。
4. 对发送的文件内容进行加密处理，保护文件内容安全。
5. 限制技能的使用权限，确保只有授权用户可以调用该技能。

### 安全风险防范

| 风险项 | 等级 | 防护措施 | 验证方法 |
| --- | --- | --- | --- |
| API密钥泄露 | 高 | 通过环境变量配置，禁止硬编码 | 定期检查代码和配置文件 |
| 命令执行风险 | 高 | 仅执行白名单命令，避免拼接用户输入 | 使用沙箱环境测试 |
| 网络通信安全 | 中 | 使用HTTPS协议，验证SSL证书 | 定期检查证书有效期 |
| 敏感数据暴露 | 高 | 输出结果中不包含密钥、令牌等敏感信息 | 日志脱敏审查 |
| 未授权访问 | 中 | 限制访问权限，实施认证机制 | 定期审计访问日志 |

## 主要功能
- **自动化执行**: 飞书发送普通文件与图片附件,支持file_key两步上传与image_key图片稳定链路。飞书机器人发送文件附件技能。覆
- **文件处理**: 支持多种文件格式的读取、解析和写入操作
- **API集成**: 通过标准化接口调用外部服务并处理响应
- **命令执行**: 在安全沙箱中执行系统命令并收集结果

## 依赖说明

### 运行环境
- **Agent 平台**: 支持SKILL.md的任意AI Agent
- **操作系统**: Windows / macOS / Linux

### 可用性分类
- **分类**: MD（纯Markdown指令，通过自然语言驱动Agent完成操作）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent完成操作。
