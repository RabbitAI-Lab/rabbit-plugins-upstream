# Seedance 2.0 · 创建任务

> a7w 插件 `seedance` 的接口 `create` · 官方文档

---

## Seedance 2.0 创建任务

`POST /api/v1/apps/seedance/create`

异步任务：提交后返回 `task_id`，可通过 `GET /api/v1/tasks/{task_id}` 或 `GET /api/v1/tasks/{task_id}` 查询进度与结果。

### 模型名称与使用场景

请求体中的 `model` 只能使用下表的公开模型名称。模型类型、名称和适用场景一一对应：

| 模型类型 | 模型名称 | 描述 |
|---|---|---|
| Seedance 2.0 标准版 | `seedance-2-text-2-video` | 输入内容不包含视频，适合文生视频、图生视频、首尾帧生成 |
| Seedance 2.0 标准版 | `seedance-2-video-2-video` | 输入内容包含视频，适合视频编辑、视频延长、视频参考 |
| Seedance 2.0 快速版 | `seedance-2-fast-text-2-video` | 输入内容不包含视频，优先生成速度 |
| Seedance 2.0 快速版 | `seedance-2-fast-video-2-video` | 输入内容包含视频，优先生成速度 |

除上述 4 个公开模型名称外，不需要填写其他模型名称。

### 计费

按输出 `total_tokens` 与定价矩阵结算。实际扣点 = 输出 `total_tokens` ÷ 1,000,000 × 当前档位点数单价（点数/百万 tokens）。
不同分辨率 × 是否含视频输入 单价不同；创建任务时预扣可为 0，完成后按矩阵扣点。