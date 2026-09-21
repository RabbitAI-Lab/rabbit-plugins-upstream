# API 密钥配置

在 AI Skills 平台登录后，先在“产品管理”开通“产品运营助手”，再进入“API 密钥”创建并复制 API 密钥。

```sh
openclaw config set env.PRODUCT_OPERATIONS_API_KEY "你的平台APIKey"
openclaw gateway restart
```

默认 API 根地址为 `https://ai-skills.open-idea.net`。自托管时可设置 `AI_SKILLS_API_URL`。不要在回复、日志、导出文件或版本库中显示完整 Key。
