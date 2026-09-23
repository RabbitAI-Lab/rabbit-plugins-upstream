# Happy Horse · 提交任务

> a7w 插件 `happy_horse` 的接口 `submit` · 官方文档

---

## 提交任务

`POST /api/v1/apps/happy_horse/submit`

创建一条视频生成任务，返回平台 `task_id`。
计费为 **定价矩阵（点数/秒）× 目标时长**：矩阵按输出分辨率 × 是否含视频输入分档（与 Seedance 矩阵 JSON 同形；Happy Horse 通常两档填相同点数/秒）。

平台需在应用管理中配置可用的服务地址与密钥；未配置时提交将提示服务未就绪。

### 主要参数

- `resolution`：`720P` 或 `1080P`
- `duration`：目标时长(秒)，文生 / 图生 / 多参考支持 3～15 秒；视频编辑时长由输入视频决定
- `prompt`：文本描述，必填
- `model`：能力代号，决定文生、图生、多参考或视频编辑
- `media`：统一参考素材数组；视频编辑传 1 个 video，可附参考图

### 请求示例
```json
{
  "resolution": "720P",
  "duration": 5,
  "prompt": "都市夜景，车流水灯，中景推进镜头"
}
```