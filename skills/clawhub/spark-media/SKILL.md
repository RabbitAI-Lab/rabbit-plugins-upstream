---
name: spark-media
description: Use when 用户要求生成图片、编辑参考图、文生视频、图生视频、制作短视频或查询媒体任务；需要 SPARK_MEDIA_API_KEY。
metadata: {"packageVersion":"2.0.0","openclaw":{"emoji":"✨","homepage":"https://ai-skills.open-idea.net","primaryEnv":"SPARK_MEDIA_API_KEY","requires":{"env":["SPARK_MEDIA_API_KEY"]}}}
---

# Spark Media

统一处理文生图、图生图、文生视频和图生视频。默认 API 根地址为
`https://ai-skills.open-idea.net/api/v1`，可用 `AI_SKILLS_API_URL` 覆盖站点根地址。

## 工作流程

1. 检查 [API Key 配置](references/API-KEY.md)，不要输出完整 Key。
2. 图片任务读取 [图片生成与编辑](references/IMAGE-GENERATION.md)。
3. 视频任务读取 [视频生成与轮询](references/VIDEO-GENERATION.md)。
4. 四个创建接口均必须携带唯一 `Idempotency-Key`。
5. 用户未指定但会显著影响结果的尺寸、画幅或时长应先确认；其余参数可采用安全默认值。

## 交付规则

- 保存并返回本次响应已有的媒体结果，不为“保存”“移动”“下载”再次生成。
- 不在对话中展开完整 base64 data URL。
- 视频创建返回 HTTP 202 和 `task_id` 后持续轮询，直到成功、失败或明确超时。
- 需要展示计费时读取 `X-AI-Skills-Billing-Currency`、
  `X-AI-Skills-Billing-Charged`、`X-AI-Skills-Billing-Balance`。

## 参考资料

- [API Key 配置](references/API-KEY.md)
- [图片生成与编辑](references/IMAGE-GENERATION.md)
- [视频生成与轮询](references/VIDEO-GENERATION.md)
- [HTTP 请求示例](references/HTTP-REQUESTS.md)
- [行为、错误与重试规则](references/BEHAVIOR-RULES.md)
