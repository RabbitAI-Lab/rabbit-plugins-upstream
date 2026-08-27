# API Key 配置

## 获取 Key

1. 登录 AI Skills 平台。
2. 在“产品管理”中开通 SQL 数据分析。
3. 进入“API Key”，选择 SQL 数据分析，创建并复制 API Key。

## 配置 OpenClaw

```sh
openclaw config set env.SQL_DATA_ANALYST_API_KEY "你的平台APIKey"
openclaw gateway restart
```

`SQL_DATA_ANALYST_API_KEY` 是用户唯一需要配置的环境变量。不配置 Provider、平台地址、公钥、模型或 Worker。

不要把完整 Key 发送到对话中，也不要写入 SQL、数据文件、日志、报告或代码仓库。
