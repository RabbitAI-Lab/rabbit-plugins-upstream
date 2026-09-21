# API 密钥配置

本 Skill 使用产品专属环境变量 `EXPENSE_COMPLIANCE_API_KEY`。密钥只授权报销合规产品的 operation，不要写入命令参数、日志、报销材料或导出报告。

```sh
openclaw config set env.EXPENSE_COMPLIANCE_API_KEY "你的平台APIKey"
openclaw gateway restart
```

所有请求使用：

```http
Authorization: Bearer ais_...
```

密钥失效、撤销或产品未开通时停止请求并说明原因，不要改用其他产品密钥。
