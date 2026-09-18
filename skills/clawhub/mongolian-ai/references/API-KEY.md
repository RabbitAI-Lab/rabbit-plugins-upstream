# API 密钥配置

在 [产品管理](https://ai-skills.open-idea.net/dashboard/products) 开通蒙语 AI，在 [API 密钥管理](https://ai-skills.open-idea.net/dashboard/keys) 创建产品专属密钥。密钥只存入 MENGGUYU_API_KEY，不能放入 URL、日志、截图或最终回复。

当前 Skill 使用 `MENGGUYU_API_KEY`。ClawHub 旧版 v1.0.14 使用的是 `MONGOL_AI_SKILL_API_KEY`，升级后必须把已确认可用于 AI Skills 平台的密钥复制到新变量名；不要删除旧配置，直到新接口验证成功。旧站点密钥若未被平台迁移或兼容，不能仅凭复制变量用于新接口，也不得把旧密钥自动上传到其它服务换取新密钥。完整步骤见 [UPGRADE](https://ai-skills.open-idea.net/skill-docs/mongolian-ai/UPGRADE.md)。

请求使用 Authorization: Bearer 平台密钥。缺少配置时停止请求，提示用户完成配置；不得猜测凭证或寻找其它服务密钥。配置后重启 Gateway。
