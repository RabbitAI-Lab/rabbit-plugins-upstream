---
name: "dknowc-gov-zhicha-public"
slug: "dknowc-gov-zhicha-public"
displayName: "深知政务智查"
description: "ClawHub Public 版深知政务智查。当用户咨询政务办事、公共服务、社保、公积金、证照、补贴、政策适用、办理条件、办理流程、材料清单、办理入口、官方依据等问题时使用；依托深知可信统一接口检索国家、省、市、区各级政策文件和行业官方网站权威信息，快速生成权威、可溯源的政务问答。"
---

# 深知政务智查（ClawHub Public 版）

该 skill 用于政务问答场景，优先给出可执行的办理步骤、条件、材料、渠道和依据。ClawHub Public 版不内置深知可信统一接口 API Key；首次使用时由 Agent 通过 MaaS 注册接口完成手机号注册、验证码确认、API Key 获取和本地配置写入。

## 启动初始化

只要本 Skill 被调用，必须先检查本 Skill 根目录下是否已存在可用的 `config.ini`。如果 `config.ini` 不存在，或调用脚本提示 API Key 缺失，先暂停原任务并向用户说明：

```text
首次使用深知政务智查需要完成深知可信统一接口账号初始化。你只需要提供手机号和收到的验证码，注册、获取 Key 和本地配置由我处理。
```

然后按两步流程执行：

```bash
node scripts/register.mjs send --phone <手机号>
```

返回 `status=true` 后，暂停并向用户索取收到的 6 位验证码，不得自行编造验证码。

拿到验证码后执行：

```bash
node scripts/register.mjs register --phone <手机号> --vcode <验证码> --organ 个人 --name 用户
```

脚本默认固定 `type=11`（可信统一接口），并自动使用 ClawHub 渠道码 `2787E171-B0E5-4328-9946-47AC52434D1F`。注册成功后，脚本会自动将 API Key 写入本 Skill 根目录下的 `config.ini`，标准输出不返回完整 Key。不得向用户索要、展示或要求用户手动复制 API Key。配置写入成功后，继续处理用户原任务。

如接口失败、短信发送受限、验证码错误、手机号已注册或用户不希望自动注册，暂停原任务并给出 ClawHub 渠道注册链接作为降级方案：

```text
https://platform.dknowc.cn/auth/#/register?channel=2787E171-B0E5-4328-9946-47AC52434D1F&type=11
```

## 配置

`config.ini` 只存在于用户本地安装后的 Skill 目录中，不得上传、打包或公开分享。公开包只提供 `config.ini.example`。

本地配置写入后包含：

- `endpoint`: 可信统一接口调用地址，默认 `https://open.dknowc.cn/chat/trusted/unification`
- `api_key`: 由注册脚本自动获取并写入的深知可信统一接口 API Key
- `sz_user_id`: 用户标识。普通使用可留空；如平台分配了用户标识，可填入
- `area`: 默认 `中国`
- `safe_answer_scope`: 安全代答范围，`none` 不代答，`risk` 仅高风险代答，`all` 对非安全问题代答
- `safe_answer_type`: 安全代答模式，`active` 积极型，`conservative` 稳妥型
- `credible_chat_scope`: 默认 `onlyNorms`
- `search_mechanism`: 搜索机制，默认 `autoSearch`
- `interpretation_model`: 解读模型，默认 `autoModel`
- `stream`: 默认 `true`
- `material`: 默认 `true`，用于返回正文角标、参考材料、原文段落和源链接
- `item`: 默认 `false`，用于返回公共事项在线办理清单
- `policy`: 默认 `false`，用于返回规范性文件清单

`session_id` 默认留空。只有需要多轮对话上下文管理时，才通过配置或 `--session-id` 动态传入。

不要把任何真实 API Key 写入公开仓库或公开分发包。

不要把 `knowledgeServiceType` 改成 `credibleRecall`。政务智查固定使用：

```json
{
  "knowledgeServiceType": "credibleChat",
  "credibleChatScope": "onlyNorms"
}
```

`credibleChatScope` 可选值：

- `onlyNorms`: 仅政务领域，适合政策、法规、办事依据等政务问答。
- `needNorms`: 政务及公共服务领域，适合公共服务、便民服务、办事咨询覆盖面更宽的场景。
- `all`: 全领域，适合用户明确要求更宽范围政策材料、行业规范或综合研究时使用。

`searchMechanism` 可选值：

- `quickSearch`: 快速搜索。
- `autoSearch`: 自动判断。
- `deepSearch`: 深度搜索，适合复杂政策研究、跨地区或跨部门材料梳理。

`interpretationModel` 可选值：

- `autoModel`: 自动选择，默认使用。
- `fastModel`: 快捷回答。
- `deepModel`: 深度解读；只有用户明确需要深度分析、复杂对比、政策研判时使用。

## 调用方式

```bash
python3 {baseDir}/scripts/gov_chat.py "社保迁移怎么办理？"
```

常用调试：

```bash
python3 {baseDir}/scripts/gov_chat.py "社保迁移怎么办理？" --show-payload
python3 {baseDir}/scripts/gov_chat.py "社保迁移怎么办理？" --json-only
python3 {baseDir}/scripts/gov_chat.py "社保迁移怎么办理？" --auto-request-id
python3 {baseDir}/scripts/gov_chat.py "深圳公积金提取需要什么材料？" --material --item
python3 {baseDir}/scripts/gov_chat.py "整理新能源汽车补贴政策文件清单" --policy --credible-chat-scope all
```

输出默认是人类可读摘要；需要给其他程序消费时使用 `--json-only`，会输出聚合后的结构化 JSON。需要链路排查时使用 `--auto-request-id` 或显式传 `--request-id`。

## 地域规则

- 当用户明确说明地域时，以用户指定地域为准。
- 当用户没有明确说明地域时，默认按 `中国` 处理。
- 如果问题明显依赖地方政策但用户未说明地域，先按 `中国` 查询；最终回答中提示用户可补充省、市、区县以获得更精准结果。
- 示例：用户问“深圳公积金提取需要什么材料？”时，按深圳市处理；用户问“公积金提取需要什么材料？”时，按中国处理，并提示可补充所在地。

## 参数选择规则

- 默认使用 `credibleChatScope=onlyNorms` 回答政策、法规、办事依据类问题。
- 用户询问公共服务、便民服务、事项办理但不局限于政策条文时，可使用 `--credible-chat-scope needNorms`。
- 用户要求整理政策文件清单、跨领域政策材料、行业规范或研究型材料时，可使用 `--credible-chat-scope all`，并打开 `--policy`。
- 用户问“怎么办、去哪办、办理入口、线上办理”时，打开 `--item`。
- 用户问“有哪些政策文件、原文清单、法规列表、依据文件”时，打开 `--policy`。
- 用户要求快速结论时，可使用 `--interpretation-model fastModel`；用户要求深度分析、对比或研判时，可使用 `--interpretation-model deepModel`。

## 跨渠道稳定回复规则

政务智查的最终回复要优先保证用户能看懂、能核对、能复制链接。不要依赖特定渠道的 Markdown、表格、脚注或链接渲染能力。

- 面向用户回复时，正文保持自然表达，不插入 `[^1^]`、`[依据1]` 等标记。
- 接口返回的引用信息只用于筛选末尾“参考依据”，不要直接暴露给用户。
- 默认在回复末尾输出“参考依据”，只列出本次回复实际使用的来源，不要默认输出完整召回清单。
- “参考依据”是该 skill 的核心特色，必须逐条、逐字段输出，不得压缩成“《标题》- 发布单位，日期”这种单行摘要。
- 每条参考依据必须保留以下字段：标题、发文字号（如有）、发布单位、发布日期、链接、相关内容。
- 每条参考依据内部字段必须换行展示，字段前使用 `-` 短横线；不同依据条目之间必须空一行，避免在聊天窗口中挤成一整段。
- 不要使用 Markdown 表格、HTML、`[标题](链接)`、`查看`、`同上` 等依赖渲染或上下文补全的表达。
- 链接必须以完整纯文本 URL 输出，用户复制或点击都应能使用。
- 如果接口未返回源链接或材料信息，明确写“接口未返回源链接”或“接口未返回对应材料”，不得补写或猜测来源。
- 如果某个字段接口未返回，保留字段名并写“接口未返回”，不要直接省略该字段。
- 如果正文未返回引用角标但接口返回了参考材料，输出接口返回的前 5 条参考材料作为依据兜底。
- 如果用户追问“哪句话对应哪条依据”，再输出“观点与依据对应”清单；默认回答不做逐句标注。

推荐格式：

```text
回复内容：
深圳市保障性住房主要包括公共租赁住房、保障性租赁住房和人才住房三类。
符合条件的青年人才可关注租金补贴、过渡性住房或人才住房配租政策。

参考依据
1. 《深圳市保障性住房管理办法》
   - 发文字号：深府规〔2023〕...号
   - 发布单位：深圳市人民政府
   - 发布日期：2023-...
   - 链接：https://...
   - 相关内容：...

2. 《...》
   - 发文字号：接口未返回
   - 发布单位：接口未返回
   - 发布日期：接口未返回
   - 链接：接口未返回源链接
   - 相关内容：...
```

如果用户追问“来源在哪”“依据怎么看”，优先重新列出本轮已使用的“参考依据”纯文本来源清单；只有用户明确要求“完整来源清单”时，才输出完整材料列表，并仍然使用纯文本列表，不使用表格。

## 回答原则

- 优先给用户可执行的办理步骤、条件、材料、渠道。
- 涉及政策依据时，打开 `--material` 或在配置中启用 `material=true`。
- 涉及线上办理入口时，打开 `--item` 或在配置中启用 `item=true`。
- 涉及政策文件清单、法规列表或原文目录时，打开 `--policy`。
- 不要把“原文清单/召回结果”作为默认体验。
