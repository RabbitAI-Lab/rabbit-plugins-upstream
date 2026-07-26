---
slug: "aws-wechat-article-writing"
name: "aws-wechat-article-writing"
version: 1.0.26
displayName: "公众号长文写作引擎"
summary: "公众号长文AI写作,从提纲或话题生成完整初稿,支持改写续写润色与多模型切换"
license: "Proprietary"
description: |-
  面向微信公众号长文的 AI 写作引擎。从选题卡、提纲或口述话题生成完整初稿,
  覆盖改写、续写、润色、开头结尾优化等环节。写作约束来自 .aws-article/config.yaml
  与本篇 article.yaml 叠加,支持 target_reader / tone / writing_style 等文风字段,
  可调用 DeepSeek / GPT / Claude 等 Chat Completions 兼容端点,或在模型未配置时
  自动降级为当前对话模型按相同约束代写。集成业务资料库引用、配图占位、发布意图管理.
tags:
  - Creative
  - Writing
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"

---
# Aws Wechat Article Writing

公众号长文 AI 写作引擎 —— 从提纲或话题生成完整初稿,支持改写、续写、润色,多模型可切.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 公众号长文写作引擎处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| 公众号长文写作引擎从提纲或话题生成 | 不支持 | 支持 |
| 多渠道消息批量发送 | 不支持 | 支持 |
| 消息模板与变量注入 | 不支持 | 支持 |
| 送达状态实时回调 | 不支持 | 支持 |
| 通信记录归档与检索 | 不支持 | 支持 |

## 能力披露

本 skill 调用 `write.py` 生成文章初稿,会把文章内容发送给用户配置的 LLM 端点。使用前请阅读以下行为说明:

- 凭证读取:`write.py` 读取仓库根 `aws.env` 的 `WRITING_MODEL_API_KEY`
- 凭证外发:该 API key 以 `Authorization: Bearer <key>` 头发送到用户在 `config.yaml.writing_model.base_url` 配置的外部端点(常见为 DeepSeek / OpenAI / Anthropic 等 Chat Completions 兼容 API)。请使用专用 key 并配置可信端点或内部代理
- 内容外发:Prompt 内包含本篇 `article.yaml` / `topic-card.md` / 合并配置 / 用户通过 `--reference` 指定的参考文档全文,整体 POST 给上述端点
- 文件读(仓库内):`.aws-article/config.yaml`、本篇 `article.yaml`、`topic-card.md`、`.aws-article/products/{产品名}/*.md`
- 文件写:仅本篇目录下 `draft.md`、`article.md`
- shell:仅 `python3 {baseDir}/（请参考skill目录中的脚本文件）`

可使用 `write.py prompt` 子命令只输出 prompt JSON 不调用 LLM,由 Agent 代写 —— 想避免把内容发给第三方时用这条路径.
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

- 从选题卡 / 提纲 / 口述话题生成公众号长文初稿,产出 `draft.md`
- 改写(rewrite)、续写(continue)、润色、开头结尾优化四种写作模式
- 写作约束叠加:全局 `.aws-article/config.yaml` + 本篇 `article.yaml`,同键以本篇为准
- 文风字段驱动:`target_reader` 控深度与用词,`tone` 控语气,`writing_style` 控结构表达
- 多模型切换:`writing_model` 段配 `provider` / `base_url` / `model`,兼容 Chat Completions 协议
- 业务资料库引用:本篇涉及自身业务时必读 `.aws-article/products/{产品名}/*.md`,可传 `--reference`(最多 5 个)
- 配图占位生成:按 `image_density`(默认每节一图)产出 `![类型名:画面内容](placeholder)`,封面占位置于标题前
- 发布意图管理:`publish_method` 取 `draft` / `published` / `none`,默认 `draft`
- 降级机制:模型未配置(退出码 2)自动取 prompt 由 Agent 代写;网络类失败自动重试一次
#
## 使用流程

1. **环境确认**: 确认Agent平台已加载本skill，检查依赖说明中的环境要求
2. **指令输入**: 向Agent描述需要执行的任务，引用`aws-wechat-article-writing`的相关能力
3. **执行处理**: Agent按照核心能力章节的指令执行任务
4. **结果验证**: 检查输出结果是否符合预期，参考错误处理章节处理异常

## 配置检查

任何操作执行前,必须检查 `.aws-article/config.yaml` 中 `article_category`、`target_reader`、`default_author` 三键(trim 后均非空)。任一项缺失须逐项询问用户,取得明确答复后写回文件,再进入写作流程。禁止从 `article.yaml` 等其它文件静默推断并写盘;禁止仅在对话里确认却不落盘.
写作模型:`writing_model`(`provider`、`base_url`、`model`)在 `.aws-article/config.yaml`;`WRITING_MODEL_API_KEY` 在仓库根 `aws.env`.
交互约定:未通过环境校验且未获用户明确「本次例外」时,不得默认改由当前 Agent 代写并假装流程完整。环境检查未通过时只处理配置选项,不要在同一条回复里混入写稿、草稿路径或多草稿选择;配置闭环后再进入写作流程.
## 工作流

写稿进度:

- 第0步:首次引导与检测顺序
- 第1步:全局账号三键(`article_category`、`target_reader`、`default_author`)落盘,须先于续旧/新开
- 第2步:在不了解用户要续写既有草稿还是新开一篇时,须先询问并确定本篇 `drafts/...` 目录,再进入以下步骤;禁止未确认就调用写作脚本
- 第3步:读取本篇约束与写作规范,写稿前先判断是否查阅业务资料库或传 `--reference`
- 第4步:确认发布方式 `publish_method`
- 第5步:确定输入与写作方式
- 第6步:写作
- 第7步:自检与修正(仅粗扫,不替代 review)
- 第8步:展示并等待用户确认

确认轮次优化:Step 1 三键已非空则静默通过;Step 4 已是合法值则静默通过;Step 2 与 Step 4 可合并为一轮提问。用户意图明确时(如给出主题加写一篇文章),理想轮次为 1 轮(确认标题/摘要)加写完后展示结果.
### 续旧稿还是新稿

当不清楚用户要续写 `drafts/` 下某篇进行中草稿还是新开一篇时,须先询问(可列出候选目录),待用户选定后再进入第 3 步。已明确时跳过询问.
目录命名:新开一篇时目录名必须为 `YYYYMMDD-标题slug`(如 `drafts/20260406-wechat-article-skills/`)。`YYYYMMDD` 为当日日期,`slug` 为小写、连字符分隔的标题缩写。禁止省略日期前缀.
### 关键字段不得空跑

调用 `write.py` 或让 Agent 代写之前,确认合并后的 `article_category`、`target_reader` 均为非空字符串(trim 后);`default_author` 非空或本篇 `article.yaml` 的 `author` 非空。若任一项不满足,须暂停写稿，引导用户补全 `.aws-article/config.yaml`(及/或本篇 `article.yaml`),并实际写入文件.
约束来源:`write.py` 先读全局 `.aws-article/config.yaml`,再读本篇目录下 `article.yaml`,把两边键叠成一张表用于生成写作提示 —— 同一键在两份文件里都有时以本篇 `article.yaml` 为准.
- `.aws-article/config.yaml`:文风、结构预设、禁用词、字数、`embeds` 等顶层字段进入这张表。`writing_model` / `image_model` 只给脚本连 API 用,不整段放进给大模型的写作说明
- 本篇 `article.yaml`:本篇标题、作者、摘要、`publish_completed` 等;与 config 重名的键会覆盖 config

`default_structure` / `default_closing_block` 指向的预设正文来自 `.aws-article/presets/`,在本篇 `article.yaml` 中必须为单元素列表 `[名]`(或空列表)。多候选时 Agent 须读取每个候选预设文件,结合主题判断最匹配的一个写入 `article.yaml`,禁止盲选第一个.
### 业务资料库

`.aws-article/products/{产品名}/` 是用户业务的原始资料库,业务介绍 `.md` 直接挂在产品根,`images/` 子目录存业务配图.
触发口径:

- 本篇主题涉及用户自身业务(对外介绍 / 教程 / 案例 / 自家业务安利)时,必须先 `ls .aws-article/products/`,对相关产品根下 `*.md` 必读,已有同主题文档优先增量改写而非另起炉灶
- 本篇主题与用户自身业务无关(行业资讯 / 通用教程等)时不读、不强求查阅

写作两种方式:

方式一(智能体直接写稿):写稿前先 `ls .aws-article/products/`,涉及产品则必读相关 `.md`;写作时将业务资料转化为账号文风后引用;`draft.md` 中凡实际引用某份业务介绍处用括号附上该文件仓库相对路径;配图占位按 `image_density` 生成,格式 `![类型名:画面内容](placeholder)` 独占一行,封面占位放标题前.
方式二(`write.py` 写稿):有相关文档时在仓库根执行 `write.py` 传 `--reference <路径>`(可重复，最多 5 个,路径形如 `.aws-article/products/<产品名>/<文件名>.md`,不接受 `images/` 子目录下的图片说明 `.md`);无相关文档时不传 `--reference`,仅靠选题卡与合并配置写稿。若 API 因上下文超限失败,减少 `--reference` 篇数或换更短文档后重试.
### 发布意图

调用 `write.py` 或进入写作之前,确认 `.aws-article/config.yaml` 中 `publish_method`:

- `draft`(默认):定稿后若走 `publish.py full`,只把图文写入公众号草稿箱,不自动发出去
- `published`:定稿后 `publish.py full` 会在创建草稿后再提交发布(异步),也可用 `full --publish` 单次强制带发布
- `none`:用户明确不想填微信配置,`publish.py full` 直接跳过不调微信,写稿/审稿/排版照常

规则:默认保持或写入 `publish_method: draft`,除非用户明确要对外发布改为 `published`;明确不填微信、不走上传改为 `none`。已是合法值可不重复盘问。禁止在 `publish_method` 非法时调用 `write.py`;禁止未经同意默认 `published`.
### 写作方式优先级

1. 优先调用第三方模型(`write.py draft/rewrite/continue`)—— 依赖 `config.yaml` 的 `writing_model` 加 `aws.env` 的 `WRITING_MODEL_API_KEY`
2. 自动降级:模型未配置(退出码 2)—— 先 `write.py prompt <mode> <input>` 获取提示词 JSON,再由 Agent 按相同提示词直接写,无须本次例外确认
3. 故障降级:调用失败(退出码 1)—— 按重试/排错逻辑处理

必须告知用户当前使用的方式:已配置且调用脚本告知使用的模型;模型未配置自动降级告知由当前对话模型直接写稿;故障降级告知第三方 API 不可用由对话模型代写并说明原因.
### write.py 退出码处理

运行脚本后须把终端里的具体报错原样摘要给用户,勿只说调用失败。按退出码与报错类型分支:

- 未配置(退出码 2):stderr 含 `[NO_MODEL]` —— 自动降级,运行 `write.py prompt <mode> <input>` 获取提示词 JSON,Agent 按该 `system_prompt` 和 `user_prompt` 写文章,无须用户确认
- 网络类(退出码 1):超时、连接失败、`URLError`、临时性 502/503 等 —— 必须自动再试 1 次(告知正在重试);第二次仍失败则改用 `write.py prompt` 取提示词后由 Agent 按相同约束代写,并明确告知第三方 API 网络不可用本次由对话模型代写
- 配置/凭证类(退出码 1):401/403、Key 无效、YAML 解析失败等 —— 不要为省事自动降级掩盖问题,列出须检查项(`config.yaml` 的 `writing_model`、`aws.env` 的 `WRITING_MODEL_API_KEY`、本篇目录是否有 `article.yaml`),请用户修正后重跑;用户明确打字愿意本次改由 Agent 代写,再按本次例外处理并留痕
- 业务/内容类(退出码 1):4xx 中除鉴权外(如 400 参数)、模型返回空等 —— 将 API 返回体摘要给用户,可先改 `model` / 请求参数再试一次,仍失败则与用户商定是否 Agent 代写

### 写作

写作时必须遵循读取的 `target_reader`、`tone`、`writing_style`:深度与用词贴合读者,语气贴合调性,结构与表达方式贴合文章风格.
用户供图分支(`image_source: user`):用户图片须先放入本篇 `imgs/`;由智能体读图分析并生成或补全 `img_analysis.md`(可用 `user_image_prepare.py` 先生成模板再填写);未落盘 `img_analysis.md` 不得调用 `write.py`;`img_analysis.md` 中推荐用途为封面必须且只能有 1 处;写稿时直接使用用户图片路径 `imgs/xxx.png`,不再输出 `placeholder`。`image_source` 只允许 `generated` 或 `user`,禁止写 `user_provided`.
状态切换规则(`article.yaml`):新建文章默认 `image_source: generated`、`publish_completed: false`;进入用户上传图片替换/重写流程时改为 `user` 并将 `publish_completed` 置回 `false`;重新发布成功且有回执后写回 `publish_completed: true`.
文章结构按优先级加载:用户指定、本篇 `article.yaml` 的 `default_structure`、`.aws-article/presets/structures/` 下的文件、内置默认。文末区块按优先级加载:本篇 `article.yaml` 的 `default_closing_block`、合并约束中 `closing_block` 非空字符串、fallback 内置默认(分割线加一句关注引导).
### 自检与修正

仅做粗扫:禁用词、段落长度、开头吸睛度、小标题密度,发现明显问题自动修正。不替代 review skill 的内容审 —— 完整的合规、敏感词、文末 embed、引用标注剥离均归 review 处理;本步禁止越界做 review 的工作.
配图占位自检(默认模式):当 `image_source != user` 时,核对 `draft.md` 是否满足 `image_density`(未配置则按每节一图);缺失或格式不合法时先补齐/修正 `![类型名:画面内容](placeholder)` 再进入审稿或配图步骤.
续写新增 `![...](placeholder)` 时,必须把该占位计入待配图清单。进入发布相关步骤前,必须复核本篇正文产物:`article.md` / `article.html` 若仍含 `placeholder`,只能标记为正文配图未完成,禁止宣称发布闭环完成.
### 产物边界

本 skill 产出只到 `draft.md`。禁止在 writing 阶段:自行写入 `article.md`(`article.md` 是 review 的 BLOCKING 产物,须含文末 `{embed:...}` 且已剥离引用标注);自行剥离 `(资料路径:...)` 引用标注(剥离动作由 review 调用 `write.py strip-citations` 完成);跳过 review 直接进入 formatting.
## 适用场景

### 新话题开篇写稿
用户提供选题卡或口述主题,从零生成一篇符合账号文风的公众号长文初稿。先落盘全局三键,再确认新开目录命名,按合并约束与结构预设产出 `draft.md`,配图占位按 `image_density` 生成.
### 续写既有草稿
用户指明 `drafts/` 下某篇进行中草稿,读取本篇 `article.yaml` 与已有 `draft.md`,按 `continue` 模式续写后续章节。续写新增配图占位须计入待配图清单,发布前复核正文产物是否仍含 `placeholder`.
### 基于业务资料库改写润色
本篇主题涉及用户自身业务(产品对外介绍、教程、案例),先 `ls .aws-article/products/` 必读相关业务介绍 `.md`,已有同主题文档优先增量改写。走 `write.py` 时传 `--reference`(最多 5 个)注入系统提示参考资料库,模型在依据处标注资料路径.
### 多草稿配图占位管理
一篇正文涉及生成配图与用户供图混合,通过 `image_source` 在 `generated` / `user` 间切换;用户供图分支须先落盘 `img_analysis.md` 才能调用 `write.py`,封面推荐用途必须且只能 1 处;写后自检占位密度并补齐缺失占位.
## 案例

### 撰写产品介绍长文并注入业务资料
用户提出为自家 SaaS 产品写一篇公众号长文。Agent 先 `ls .aws-article/products/` 发现 `saas-product/项目介绍.md` 与 `saas-product/功能清单.md`,判断主题涉及自身业务必读两份文档。确认 `.aws-article/config.yaml` 中三键非空、`publish_method: draft`。因有相关业务文档,在仓库根执行 `write.py draft topic-card.md --reference .aws-article/products/saas-product/项目介绍.md --reference .aws-article/products/saas-product/功能清单.md -o drafts/20260406-saas-intro/draft.md`。脚本把两份资料全文注入系统提示参考资料库,模型在依据处标注资料路径。产出 `draft.md` 后粗扫禁用词与小标题密度,自检配图占位每节一图,封面占位置于标题前,展示给用户确认后移交 review.
### 模型未配置自动降级代写
用户未配置 `writing_model`,`write.py draft` 退出码 2 且 stderr 含 `[NO_MODEL]`。Agent 不打断用户,自动运行 `write.py prompt draft topic-card.md` 取回 `system_prompt` 与 `user_prompt` 的 JSON,按相同写作约束(相同 target_reader / tone / writing_style / 结构预设)由当前对话模型直接写稿,输出到 `-o` 指定路径。完成后告知用户:写作模型未配置,本次由当前对话模型直接写稿(使用相同写作约束)。无须用户确认或本次例外.
### 网络类失败重试后降级
用户已配置 DeepSeek 端点,`write.py draft` 退出码 1,stderr 显示 `URLError` 与连接超时。Agent 告知正在重试,简短等待后重跑同一命令;第二次仍超时,改用 `write.py prompt` 取提示词后由 Agent 按相同约束代写,并明确告知:第三方 API 网络不可用,本次由对话模型代写。整个过程未掩盖问题、未静默切换.
## 异常处理

### write.py 退出码 2(模型未配置)
stderr 含 `[NO_MODEL]`。自动降级:运行 `write.py prompt <mode> <input>` 取提示词 JSON,Agent 按该 `system_prompt` 和 `user_prompt` 写文章输出到 `-o` 指定路径。无须用户确认或本次例外.
### write.py 退出码 1 网络类失败
stderr 含超时、连接失败、`URLError`、临时性 502/503。必须自动再试 1 次并告知正在;第二次仍为网络类失败则改用 `write.py prompt` 取提示词后由 Agent 按相同约束代写,必须明确告知第三方 API 网络不可用本次由对话模型代写.
### write.py 退出码 1 配置/凭证类失败
stderr 含 401/403、Key 无效、`未找到写作约束`、YAML 解析失败。不要为省事自动降级掩盖问题。列出须检查项(`config.yaml` 的 `writing_model`、`aws.env` 的 `WRITING_MODEL_API_KEY`、本篇目录是否有 `article.yaml`),请用户修正后重跑 `write.py`。用户明确打字愿意本次改由 Agent 代写,再按本次例外处理并留痕.
### 全局三键缺失
`article_category`、`target_reader`、`default_author` 中任一项 trim 后为空。须暂停写稿,逐项询问用户,取得明确答复后写回 `.aws-article/config.yaml`,再进入写作流程。禁止从 `article.yaml` 等其它文件静默推断并写盘;禁止仅在对话里确认却不落盘.
### publish_method 非法值
`publish_method` 不在 `draft` / `published` / `none` 中。禁止调用 `write.py`。按规则与用户确认:默认 `draft`,明确要对外发布改 `published`,明确不填微信改 `none`,写回文件后再进入写作.
### img_analysis.md 缺失(用户供图分支)
`image_source: user` 但本篇未落盘 `img_analysis.md`。不得调用 `write.py`,否则脚本报错退出。先用 `user_image_prepare.py` 生成模板并填写,确保推荐用途为封面处必须且只能 1 处,再调用 `write.py`.
### --reference 篇数过多导致 token 超限
写作 API 因上下文/token 超限失败。减少 `--reference` 篇数(如从 5 个降到 2 个)或换更短文档后;仍失败则与用户商定是否由 Agent 代写.
### 跨 skill 引用文件未找到(单独安装)
单独安装本 skill 时,跨 skill 引用(如 `../aws-wechat-article-main/references/*.md`)的步骤在读取阶段遇到 file not found。本 skill 内的纯本地步骤仍可用;需要跨 skill 引用的步骤建议装齐一条龙套件到同一 `skills/` 根目录.
## 常见问题

### Q1:如何配置写作模型?
在 `.aws-article/config.yaml` 的 `writing_model` 段填 `provider` / `base_url` / `model`(base_url 指向 Chat Completions 兼容端点);在仓库根 `aws.env` 填 `WRITING_MODEL_API_KEY`。键名对照参考 `references/env.example.yaml`。未配置时 `write.py` 退出码 2 自动降级.
### Q2:draft.md 与 article.md 有什么区别?
`draft.md` 是本 skill 的产物,含配图标记与括号引用路径,用于事实溯源。`article.md` 是 review skill 的产物,由 review 调用 `write.py strip-citations` 剥离括号路径、追加文末 `{embed:...}` 后写入。writing 阶段禁止自行命名 `article.md` 或自行剥离引用标注.
### Q3:什么时候该传 --reference?
本篇主题涉及用户自身业务(对外介绍、教程、案例、自家业务安利)且 `.aws-article/products/{产品名}/` 下有相关业务介绍 `.md` 时传;路径形如 `.aws-article/products/<产品名>/<文件名>.md`,可重复最多 5 个,不接受 `images/` 子目录下的图片说明 `.md`。主题与自身业务无关时不传.
### Q4:publish_method 三个值分别什么效果?
`draft`(默认)定稿后 `publish.py full` 只写入公众号草稿箱不自动发出;`published` 在创建草稿后再提交发布(异步),也可 `full --publish` 单次强制;`none` 用户明确不填微信,`publish.py full` 直接跳过不调微信,写稿/审稿/排版照常.
### Q5:多草稿时如何确定写哪一篇?
不了解用户要续写某篇还是新开时须先询问(可列出 `drafts/` 候选目录),待用户选定后再进入写作;禁止未确认就自动选中某一 `drafts/...` 跑写作脚本。已明确路径或意图时跳过询问。新开目录名必须为 `YYYYMMDD-标题slug`,禁止省略日期前缀.
### Q6:什么情况下会自动降级为对话模型代写?
两种:模型未配置(退出码 2)自动取 prompt 由 Agent 代写,无须确认;网络类失败(退出码 1)自动重试一次,第二次仍失败则取 prompt 由 Agent 代写并明确告知。配置/凭证类失败不会自动降级,须用户修正或明确打字愿意本次例外。所有降级路径都先运行 `write.py prompt` 取相同 `system_prompt` 和 `user_prompt`,确保写作约束一致.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 依赖外部 LLM 端点,网络不通时降级为对话模型代写,质量受对话模型能力影响
- `write.py` 会把 `article.yaml` / `topic-card.md` / 参考文档全文 POST 给配置的端点,内容外发须用户知情并配置可信端点
- 本 skill 产出只到 `draft.md`,合规审、敏感词、文末 embed、引用标注剥离均归 review skill,writing 阶段不得越界
- `--reference` 最多 5 个且路径须直接挂在产品根,token 超限时须减少篇数
- 跨 skill 引用依赖一条龙套件装齐到同一 `skills/` 根目录,单独安装时部分步骤会 file not found
- 需要人工判断的复杂决策场景不适用,本 skill 不保证 100% 确定性

## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "公众号长文写作引擎处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "aws-wechat-article-writing"
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
