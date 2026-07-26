---
slug: "ai-podcast-free"
name: "ai-podcast-free"
version: 1.0.1
displayName: "AI播客生成(免费版)"
summary: "将文本内容转化为双主持人对话播客的基础工具"
license: "MIT"
description: |-
  基于MagicPodcast API将纯文本内容转化为双主持人对话式播客.
  支持多语言生成，返回可分享的播客链接。适用于个人用户快速
  将文字内容转为音频场景.
tags:
  - Creative
tools:
  - read
  - exec
homepage: "https://skillhub.cn"

---
# AI播客生成(免费版) - 文本转对话式播客

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | AI播客生成(免费版)处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-----|:-----|:-----|:-----|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 核心能力

将纯文本内容转化为两位主持人自然对话的播客节目。通过MagicPodcast API完成音频合成，返回可直接分享的播客链接.
支持的基础能力：
- 从粘贴的纯文本生成播客
- 支持多种语言生成（需用户明确指定）
- 异步任务状态查询
- 返回可分享的播客链接
#
## 使用流程

1. **环境确认**: 确认Agent平台已加载本skill，检查依赖说明中的环境要求
2. **指令输入**: 向Agent描述需要执行的任务，引用`ai-podcast-free`的相关能力
3. **执行处理**: Agent按照核心能力章节的指令执行任务
4. **结果验证**: 检查输出结果是否符合预期，参考错误处理章节处理异常

#
## 环境配置

使用前需配置以下环境变量：

```bash
export MAGICPODCAST_API_URL="https://api.magicpodcast.app"
export MAGICPODCAST_API_KEY="your_api_key_here"
```

API密钥获取地址：https://www.magicpodcast.app/skill-platform

登录后复制API密钥即可使用。注册过程免费，约一分钟内完成.
## 引导式交互

每次只提一个问题，等待用户回答后再提下一个：

1. 询问播客主题
2. 询问内容来源：粘贴的文本内容
3. 询问播客语言（不要自行假设）
4. 确认后调用API创建播客
5. 创建后返回仪表板地址供用户查看进度
6. 完成后返回可分享的播客链接

## API调用方式

### 安全校验

```bash
safe_job_id() {
  printf '%s' "$1" | grep -Eq '^[A-Za-z0-9_-]{8,128}$'
}
```

### 从文本创建播客

```bash
payload="$(jq -n --arg text "$SOURCE_TEXT" --arg language "$LANGUAGE" '{text:$text,language:$language}')"
# ...
curl -sS -X POST "$MAGICPODCAST_API_URL/agent/v1/podcasts/text" \
  -H "Content-Type: application/json" \
  -H "x-api-key: $MAGICPODCAST_API_KEY" \
  --data-binary "$payload"
```

### 查询任务状态

```bash
if ! safe_job_id "$JOB_ID"; then
  echo "Invalid job id" >&2
  exit 1
fi
# ...
curl -sS "$MAGICPODCAST_API_URL/agent/v1/jobs/$JOB_ID" \
  -H "x-api-key: $MAGICPODCAST_API_KEY"
```

### 结果处理

- 创建后引导用户打开 https://www.magicpodcast.app/app 查看仪表板
- 优先返回 outputs.shareUrl 作为完成链接
- 若 shareUrl 缺失则回退到 outputs.appUrl
- 完成时回复用户播客链接地址
- statusLabel 为 complete 时返回分享链接
- statusLabel 为 failed 时返回错误信息
- API返回错误时如实展示错误消息

## 案例参考

### 案例一：博客文章转播客

一位博主希望将博客文章转化为音频版本。将文章文本粘贴到创建接口，指定语言为中文，API在约2分钟内生成播客。返回的分享链接可直接嵌入到博客页面，读者可选择阅读或收听，提升了博客内容的可及性.
### 案例二：学习笔记转播客

一位学生将课程笔记转化为播客，在通勤时复习。将笔记文本粘贴到接口，指定语言后生成播客。双主持人对话形式帮助加深对知识点的理解，相比单纯阅读笔记提升了复习效率.
## 异常处理

### API密钥缺失或无效

API返回401认证错误时，引导用户访问 https://www.magicpodcast.app/skill-platform 获取有效密钥。注册免费，使用Google账号登录后一分钟内完成，复制API密钥配置到环境变量.
### 文本内容为空或过短

输入文本为空或字数过少时，API可能返回内容不足错误。确保文本内容包含足够信息，建议不少于200字。内容过于简短会导致对话缺乏深度和连贯性.
### 任务生成超时

播客生成通常2-5分钟。超过10分钟未完成时，建议用户检查仪表板状态或重新创建任务。不要频繁轮询状态接口，仅在用户询问时查询.
### 网络连接错误

无法连接API服务器时，检查网络连接和配置后重试和代理配置，确保能访问 https://api.magicpodcast.app 域名。企业内网环境需配置相应的网络出口.
### 任务状态查询失败

查询返回404时，任务ID无效或已过期。确认使用创建时返回的正确job ID，格式为8-128位字母数字、连字符或下划线，校验函数会拦截格式不符的ID.
## 常见问题

### 如何获取API密钥？

访问 https://www.magicpodcast.app/skill-platform ，使用Google账号登录，复制API密钥配置到MAGICPODCAST_API_KEY环境变量。注册免费，约一分钟完成.
### 生成需要多长时间？

通常2-5分钟，取决于内容长度和服务器负载。可访问 https://www.magicpodcast.app/app 查看实时进度.
### 支持哪些语言？

支持多种主流语言，包括英语、中文、西班牙语、法语、德语、日语等。生成时必须明确指定语言，系统不会自行假设.
### 如何查看生成进度？

访问 https://www.magicpodcast.app/app 打开仪表板，查看已创建播客列表和实时进度。也可通过任务ID调用状态查询接口获取程序化状态.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 检查网络连接和配置后重试；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要有效的MagicPodcast API密钥
- 仅支持纯文本输入，不支持PDF URL转播客
- 播客生成需要2-5分钟
- 不支持加密文件破解
- 敏感内容将发送至外部服务处理
- 单次请求处理一个文本内容
- 性能取决于底层API服务能力

## 升级提示

本免费版支持基础的文本转播客功能。如需PDF文档转播客、多来源内容处理、高级引导式交互流程等完整能力，请升级到完整版 ai-podcast 获取全部功能.
## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "AI播客生成(免费版)处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "ai-podcast"
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
