# Jimeng AI Skill for OpenClaw

即梦AI图像生成技能封装 - 基于 jimeng-free-api

## 服务状态

| 项目 | 状态 |
|------|------|
| 服务地址 | http://127.0.0.1:8000 |
| API 兼容 | OpenAI Images API |
| 运行状态 | ✅ 运行中 (PID: 8022) |
| 测试状态 | ✅ 生图成功 |

## 快速开始

### 启动服务
```bash
bash ~/.openclaw/workspace/skills/jimeng-ai/start.sh
```

### 生图调用
```bash
curl -X POST http://127.0.0.1:8000/v1/images/generations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <sessionid>" \
  -d '{
    "model": "jimeng-3.0",
    "prompt": "一只可爱的猫咪在花园里玩耍",
    "n": 1
  }'
```

## 支持的模型

- `jimeng-3.0`（默认，推荐）
- `jimeng-2.1`
- `jimeng-2.0-pro`
- `jimeng-2.0`
- `jimeng-1.4`
- `jimeng-xl-pro`

## 参数说明

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| model | string | jimeng-3.0 | 模型版本 |
| prompt | string | 必填 | 生成描述 |
| n | number | 1 | 生成数量(1-4) |
| width | number | 1024 | 图片宽度 |
| height | number | 1024 | 图片高度 |

## 配置

sessionid 已配置在 `start.sh` 中，如需更新：
```bash
export AUTHORIZATION=你的新sessionid
```

## 日志

服务日志：`server.log`
