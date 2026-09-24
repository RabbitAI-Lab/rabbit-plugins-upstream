# 提交任务 · submit

> a7w 插件 `image_human` 的接口 `submit` · 平台官方文档

---

`POST /api/v1/apps/image_human/submit`

## 提交任务

`POST /api/v1/apps/image_human/submit`

全驱动数字人任务，提供人物图片、驱动音频、可选用户提示词和生成模式。mode 支持 fast、standard、2k、4k；resolution 仅作为兼容别名；submit 按输入音频时长计费。

返回示例：`{ "task_id": 123, "status": "pending" }`

## 参数（平台 schema 原文）

```json
{
  "mode": {
    "enum": [
      "fast",
      "standard",
      "2k",
      "4k"
    ],
    "type": "string",
    "default": "standard",
    "required": false,
    "description": "生成模式/清晰度档位：fast 快速模式，standard 标准模式，2k 高清模式，4k 超清模式"
  },
  "prompt": {
    "type": "string",
    "default": "人物说话自然，面对镜头，肢体语言自然，人物清晰可鉴。",
    "example": "人物说话自然，面对镜头，肢体语言自然，人物清晰可鉴。",
    "required": false,
    "description": "用户提示词；未传时使用默认提示词"
  },
  "duration": {
    "type": "number",
    "required": false,
    "description": "输入音频时长，单位秒；未传时平台从 ref_file_url 探测"
  },
  "file_url": {
    "type": "string",
    "example": "https://example.com/person.png",
    "required": true,
    "description": "输入图片 URL"
  },
  "resolution": {
    "enum": [
      "2k",
      "4k"
    ],
    "type": "string",
    "required": false,
    "description": "兼容字段；传 2k 或 4k 时等同于 mode=2k 或 mode=4k。新接入建议直接使用 mode"
  },
  "ref_file_url": {
    "type": "string",
    "example": "https://example.com/audio.wav",
    "required": true,
    "description": "输入音频 URL，用于驱动数字人；平台按该音频时长计费"
  }
}
```

## 计费

- 结算口径：按用量 2 点（租户价）；按用量 2 点/单位
- 标准价：`fixed_price=0.0000` / `input_price=2.000000`
- 租户价：`tenant_fixed_points=0.00` / `tenant_points_per_1k_input=2.0000`
- 分档：`2k`=4，`4k`=8，`fast`=1.5，`standard`=2
