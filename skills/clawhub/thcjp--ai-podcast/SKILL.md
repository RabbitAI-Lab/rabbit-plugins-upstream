---
slug: "ai-podcast"
name: "ai-podcast"
version: 1.0.12
displayName: "AI播客生成"
summary: "将PDF、文本、笔记和链接转化为双主持人对话播客，几分钟生成可分享的音频节目"
license: "Proprietary"
description: |-
  基于MagicPodcast API将PDF文档、文本内容、笔记和网页链接转化为
  自然流畅的双主持人对话式播客节目。支持多语言生成，返回可分享的
  播客链接。适用于内容创作者、教育工作者、研究人员等需要将文字
  内容转化为音频场景的用户.
tags:
  - Creative
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"

---
# AI播客生成 - PDF与文本转对话式播客

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | AI播客生成处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| AI播客生成几分钟生成 | 不支持 | 支持 |
| 高清分辨率与无损输出 | 不支持 | 支持 |
| 批量生成与风格预设 | 不支持 | 支持 |
| 自定义模型微调 | 不支持 | 支持 |
| 商用版权授权 | 不支持 | 支持 |

## 依赖说明

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
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 核心能力

将PDF文档、纯文本、笔记内容或网页链接转化为两位主持人自然对话的播客节目。通过MagicPodcast API完成音频合成，返回可直接分享的播客链接.
支持的具体能力：
- 从PDF URL提取内容并生成播客
- 从粘贴的纯文本生成播客
- 多语言播客生成（需用户明确指定语言）
- 异步任务状态查询
- 返回可分享的播客链接和仪表板地址
#
## 使用流程

1. **环境确认**: 确认Agent平台已加载本skill，检查依赖说明中的环境要求
2. **指令输入**: 向Agent描述需要执行的任务，引用`ai-podcast`的相关能力
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
## 引导式交互流程

与用户交互时，每次只提一个问题，等待用户回答后再提下一个：

1. 询问播客主题
2. 询问内容来源：PDF的URL地址或直接粘贴的文本
3. 询问播客语言（不要自行假设语言）
4. 最终确认后调用API创建播客
5. 创建后立即返回仪表板地址供用户查看进度
6. 用户询问时才检查任务状态
7. 完成后返回标题和可分享的播客链接

## API调用方式

### 安全校验

所有用户输入在拼接到命令前必须经过校验，使用jq进行JSON编码，严禁直接插入原始文本.
```bash
safe_job_id() {
  printf '%s' "$1" | grep -Eq '^[A-Za-z0-9_-]{8,128}$'
}
# ...
safe_http_url() {
  printf '%s' "$1" | grep -Eq '^https?://[^[:space:]]+$'
}
```

### 从PDF创建播客

```bash
if ! safe_http_url "$PDF_URL"; then
  echo "Invalid PDF URL" >&2
  exit 1
fi
# ...
payload="$(jq -n --arg pdfUrl "$PDF_URL" --arg language "$LANGUAGE" '{pdfUrl:$pdfUrl,language:$language}')"
# ...
curl -sS -X POST "$MAGICPODCAST_API_URL/agent/v1/podcasts/pdf" \
  -H "Content-Type: application/json" \
  -H "x-api-key: $MAGICPODCAST_API_KEY" \
  --data-binary "$payload"
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

### 结果处理规则

- 创建后立即引导用户打开 https://www.magicpodcast.app/app 查看仪表板
- 仪表板可查看已创建播客、实时进度和已完成节目
- 优先返回 outputs.shareUrl 作为完成链接
- 若 shareUrl 缺失则回退到 outputs.appUrl
- 完成时回复用户播客链接地址
- statusLabel 为 complete 时返回分享链接
- statusLabel 为 failed 时返回错误信息
- API返回错误时如实展示错误消息和详情
- 提醒用户不要发送敏感文档，除非同意外部处理

## 适用场景

### 学术论文音频化

研究人员将PDF格式的学术论文转化为播客，在通勤或运动时收听。双主持人对话形式比纯朗读更易理解复杂概念，适合快速了解论文核心观点和研究背景.
### 内容团队音频化运营

内容创作团队将博客文章、周报、行业分析等文字内容批量转化为播客节目，扩展内容分发渠道，覆盖偏好音频的受众群体，提升内容触达率.
### 教育内容多语言转化

教育工作者将课程笔记、教学材料转化为多语言播客，为不同语言背景的学习者提供音频学习资源。需在创建时明确指定目标语言，系统不会自行假设语言.
### 企业内部知识传播

企业将内部文档、培训材料、会议纪要转化为播客，员工可在碎片时间收听，降低知识获取门槛，提升组织内部信息流转效率.
## 案例参考

### 案例一：论文转播客

一位研究人员需要阅读大量PDF论文，希望利用通勤时间收听。将论文PDF上传至可访问的URL后，通过PDF创建接口生成播客。API返回任务ID，约3分钟后任务完成，获得可分享的播客链接。两位虚拟主持人以对话形式讨论论文的研究背景、方法、结果和意义，帮助研究人员快速把握论文要点.
### 案例二：周报转播客

一个内容团队每周发布行业分析周报，希望同时提供音频版本。将周报文本粘贴到文本创建接口，指定语言为中文，API在约2分钟内生成播客。团队将返回的分享链接嵌入到周报邮件中，读者可选择阅读或收听，提升了周报的打开率和传播效果.
### 案例三：多语言内容扩展

一位博主将英文博客文章转化为西班牙语播客，面向西班牙语受众扩展内容覆盖面。通过文本创建接口指定语言为西班牙语，生成的播客保持原文核心观点的同时以西班牙语对话形式呈现，帮助博主触达更多国际读者.
## 异常处理

### API密钥缺失或无效

当MAGICPODCAST_API_KEY未设置或已失效时，API返回401认证错误。需引导用户访问 https://www.magicpodcast.app/skill-platform 获取有效密钥。提示用户注册免费，一分钟内即可完成，使用Google账号登录后复制API密钥.
### PDF URL不可达

当提供的PDF URL无法访问时，API返回URL获取失败错误。需检查URL是否为公开可访问地址，本地PDF文件需先上传至可公开访问的存储服务。URL必须以http://或https://开头，不能包含空格.
### 文本内容为空或过短

当输入的文本内容为空或字数过少时，API可能返回内容不足错误。需确保文本内容包含足够信息供生成有意义的对话。建议文本长度不少于200字，内容过于简短会导致对话缺乏深度.
### 任务生成超时

播客生成通常需要2-5分钟。若超过10分钟仍未完成，建议用户检查仪表板状态或重新创建任务。不要频繁轮询状态接口，仅在用户询问时查询，避免对API造成不必要的负载.
### 语言参数不支持

当指定的语言不在支持列表中时，API返回语言不支持错误。需提示用户确认目标语言，常见支持语言包括英语、中文、西班牙语、法语、德语、日语等。不支持的语言需更换为相近的替代语言.
### 网络连接错误

当无法连接到API服务器时，必要时联系网络管理员开放访问权限.
### 任务状态查询失败

查询任务状态时若返回404，说明任务ID无效或已过期。需确认使用的是创建任务时返回的正确job ID。job ID应为8-128位的字母数字、连字符或下划线组成的字符串，格式不符时校验函数会拦截.
### 返回结果缺少分享链接

当任务完成但outputs.shareUrl缺失时，回退使用outputs.appUrl。若两者均缺失，引导用户直接访问 https://www.magicpodcast.app/app 在仪表板中查找已完成的播客节目.
## 常见问题

### 如何获取API密钥？

访问 https://www.magicpodcast.app/skill-platform ，使用Google账号登录，复制API密钥。注册过程免费，约一分钟完成。将密钥配置到MAGICPODCAST_API_KEY环境变量中即可开始使用.
### 生成一个播客需要多长时间？

通常需要2-5分钟。生成时间取决于内容长度和当前服务器负载。创建任务后可访问 https://www.magicpodcast.app/app 查看实时进度，任务完成后会返回可分享的播客链接.
### 支持哪些输入来源？

支持两种输入：PDF的公开URL地址和直接粘贴的纯文本。本地PDF文件需先上传至可公开访问的存储服务获取URL。不支持加密文件破解，不支持直接上传本地文件.
### 支持哪些语言？

支持多种主流语言，包括但不限于英语、中文、西班牙语、法语、德语、日语。生成时必须明确指定语言，系统不会自行假设。具体支持列表可参考API返回的错误提示.
### 免费额度是多少？

登录用户可生成免费播客。具体免费额度可能根据账户类型和当前政策有所不同，建议查看官方平台 https://www.magicpodcast.app/skill-platform 了解最新的额度信息.
### 如何查看生成进度？

创建任务后，访问 https://www.magicpodcast.app/app 打开仪表板。仪表板显示已创建的播客列表、实时生成进度和已完成的节目。也可通过任务ID调用状态查询接口获取程序化状态.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要有效的MagicPodcast API密钥，无密钥无法使用
- PDF文件需通过公开URL提供，本地文件需先上传至可访问的存储服务
- 播客生成需要2-5分钟，不适合实时场景
- 不支持加密文件破解
- 生成质量取决于原始内容的信息量和结构
- 敏感文档需谨慎处理，内容将发送至外部服务处理
- 单次请求处理一个来源，不支持多文件合并生成
- 性能取决于底层API服务能力和网络状况
