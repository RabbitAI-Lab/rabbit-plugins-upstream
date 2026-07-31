# 深知晓（ClawHub Public 版）

这是深知晓的 ClawHub 分发版本。功能逻辑与 full 版保持一致，但不内置深知可信统一接口 API Key；首次调用本 Skill 时，由 Agent 通过 MaaS 注册接口完成手机号注册、验证码确认、API Key 获取和本地配置写入，用户只需提供手机号和收到的验证码。

## 能力范围

- 咨询导办：调用深知可信统一接口 `credibleChat` 能力，回答税务社保、法规政策、行业标准、证照补贴资质申办、买房购车、养老育儿、上学就业等工作与公共服务问题。
- 可信搜索：用户明确要求查找原文、依据、材料、来源或召回结果时，调用 `scripts/trusted_search.py` 返回重点材料摘要和知识专库链接。
- 复杂任务：支持企业补贴测算、税务优惠判断、政策调研、跨地区对比、投标方案背景和合规义务分析等 ReAct 工作流。
- 分析写作：支持分析调研、拟稿写文等工作场景，输出内容可逐项索引于动态更新的权威知识网络。
- 本地化服务：支持结合用户问题智能识别或切换城市，提供本地化精准知识服务。
- 可信溯源：问答模式默认返回可信溯源报告链接，来源核验以报告页为准。
- 稳定输出：脚本只输出接口正文的必要清洗版，不在聊天窗口重组参考依据、事项清单或政策文件清单。
- 默认参数：问答模式使用 `credibleChatScope=all`、`material=true`、`item=true`、`policy=true`、`traceurl=true`、`stream=true`；搜索模式默认 `policy=true`、`item=true`、`know_base=true`、`segment_count=2`、`simplified=true`。

## 注册并配置深知可信统一接口 API Key

ClawHub 版默认使用：

- 接入点 `type=11`，即可信统一接口。
- 渠道码 `2787E171-B0E5-4328-9946-47AC52434D1F`。
- 本地 `config.ini` 保存可信统一接口 Key，由 Agent 自动创建，公开包不携带该文件。

如果当前深知晓没有配置 Key，Agent 会先询问用户是否允许复用当前运行环境已安装 Skills 目录下其他 `dknowc*` Skill 的本地 Key。用户同意后可执行：

```bash
node scripts/register.mjs scan-reuse
node scripts/register.mjs reuse-key --from <候选目录名或 slug>
```

扫描范围仅限当前 Skill 同级目录下一级 `dknowc*` Skill，只读取 `_meta.json` 和 `config.ini`，不会展示完整 Key。

如用户不复用、未找到候选或复用失败，再进入 MaaS 注册。注册第二步会携带平台固定 `grantToken`，手机号已注册时可通过验证码查回已有可用 API Key；默认不主动新建 Key。第 1 步，发送短信验证码：

```bash
node scripts/register.mjs send --phone 13812345678
```

返回 `status=true` 后，暂停并请用户提供收到的 6 位验证码。

第 2 步，注册并获取 API Key：

```bash
node scripts/register.mjs register --phone 13812345678 --vcode 123456 --organ 个人 --name 用户
```

成功后，脚本会把 API Key 自动写入本 Skill 根目录下的 `config.ini`，不会在标准输出中返回完整 Key。用户不需要手动复制 Key，也不需要手动编辑配置文件。

如自动注册链路失败，可降级使用 ClawHub 渠道注册链接手动注册：

```text
https://platform.dknowc.cn/auth/#/register?channel=2787E171-B0E5-4328-9946-47AC52434D1F&type=11
```

可信统一接口固定为：

```text
https://open.dknowc.cn/chat/trusted/unification
```

可信搜索接口固定为：

```text
https://open.dknowc.cn/dependable/search
```

`config.ini` 只存在于用户本地安装后的 Skill 目录中，不得上传、打包或公开分享。发布包检查会阻止该文件进入公开包。

## 常用测试

语法检查：

```bash
python3 -m py_compile scripts/gov_chat.py scripts/trusted_search.py scripts/check_release.py
node --check scripts/register.mjs
```

发布检查：

```bash
python3 scripts/check_release.py
```

请求参数检查：

```bash
python3 scripts/gov_chat.py "社保迁移怎么办理？" --show-payload --dry-run
python3 scripts/trusted_search.py "公积金租房提取政策原文" --show-payload --dry-run
```

## Public 版说明

- 本版本 slug 为 `dknowc-know`，展示名为“深知晓”。
- 本版本不内置 API Key。
- 用户可通过 Agent 调用 `scripts/register.mjs`，用手机号和验证码注册 MaaS 账号并获取深知可信统一接口 API Key。
- 注册成功后，Agent 自动把 API Key 写入本地 `config.ini`，用户不需要查看或手动配置 Key。
- 如调用失败或提示 API Key 未配置，请重新执行注册流程或检查本地 `config.ini` 是否存在且有效。
