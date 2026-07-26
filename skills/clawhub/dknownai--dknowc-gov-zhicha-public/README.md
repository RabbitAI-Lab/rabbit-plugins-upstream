# 深知政务智查（ClawHub Public 版）

这是深知政务智查的 ClawHub 分发版本。功能逻辑与 public 版保持一致，但不内置深知可信统一接口 API Key；首次调用本 Skill 时，由 Agent 通过 MaaS 注册接口完成手机号注册、验证码确认、API Key 获取和本地配置写入，用户只需提供手机号和收到的验证码。

## 能力范围

- 政务问答：调用深知可信统一接口 `credibleChat` 能力，回答政务办事、公共服务、政策适用、办理流程、材料清单和官方依据等问题。
- 参考依据：默认返回参考材料，并以纯文本字段化方式展示标题、文号、发布单位、发布日期、链接和相关内容。
- 办理事项：可通过 `--item` 返回公共事项在线办理清单。
- 政策文件：可通过 `--policy` 返回规范性文件清单。

## 注册并配置深知可信统一接口 API Key

ClawHub 版默认使用：

- 接入点 `type=11`，即可信统一接口。
- 渠道码 `2787E171-B0E5-4328-9946-47AC52434D1F`。
- 本地 `config.ini` 保存可信统一接口 Key，由 Agent 自动创建，公开包不携带该文件。

第 1 步，发送短信验证码：

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

`config.ini` 只存在于用户本地安装后的 Skill 目录中，不得上传、打包或公开分享。发布包检查会阻止该文件进入公开包。

## 常用测试

语法检查：

```bash
python3 -m py_compile scripts/gov_chat.py scripts/check_release.py
node --check scripts/register.mjs
```

发布检查：

```bash
python3 scripts/check_release.py
```

请求参数检查：

```bash
python3 scripts/gov_chat.py "社保迁移怎么办理？" --show-payload --dry-run
```

## Public 版说明

- 本版本不内置 API Key。
- 用户可通过 Agent 调用 `scripts/register.mjs`，用手机号和验证码注册 MaaS 账号并获取深知可信统一接口 API Key。
- 注册成功后，Agent 自动把 API Key 写入本地 `config.ini`，用户不需要查看或手动配置 Key。
- 如调用失败或提示 API Key 未配置，请重新执行注册流程或检查本地 `config.ini` 是否存在且有效。
