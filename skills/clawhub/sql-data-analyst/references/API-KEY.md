# API 密钥配置

推荐在平台创建通用 Key，并执行 `openclaw config set env.AI_SKILLS_API_KEY "你的平台APIKey"` 和 `openclaw gateway restart`，全平台 Skill 只需配置一次。仍需开通目标产品。下列 `SQL_DATA_ANALYST_API_KEY` 配置是兼容的产品专用覆盖项；调用优先使用该变量，为空时回退到 `AI_SKILLS_API_KEY`。两个变量均缺失时停止调用，不发送空 Bearer 请求。不要把旧请求换 Key 自动重试；幂等记录按 Key 隔离。


## 获取密钥

1. 登录 AI Skills 平台。
2. 在“产品管理”中开通 SQL 数据分析。
3. 进入“API 密钥”，创建通用 Key；已有通用 Key 时直接复制复用。

## 配置 OpenClaw

```sh
openclaw config set env.SQL_DATA_ANALYST_API_KEY "你的平台APIKey"
openclaw gateway restart
```

`AI_SKILLS_API_KEY` 与兼容的 `SQL_DATA_ANALYST_API_KEY` 任选其一即可；已配置全局通用 Key 时无需再次配置。不配置服务提供方、平台地址、公钥、模型或 Worker。

不要把完整密钥发送到对话中，也不要写入 SQL、数据文件、日志、报告或代码仓库。
