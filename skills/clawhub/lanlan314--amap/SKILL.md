---
name: amap
description: 高德地图 API 技能，支持路径规划、距离计算、地理位置搜索等。用于查询两地之间的骑行/驾车/步行路线、距离、时间等实时信息。需要配置高德地图 API Key（AMAP_API_KEY）。
---

# 高德地图技能 (amap)

## ⚠️ 环境变量配置

| 环境变量 | 说明 | 获取方式 |
|----------|------|---------|
| `AMAP_API_KEY` | 高德地图 Web 服务 API 密钥 | [高德开放平台控制台](https://console.amap.com/dev/key/app) |

### 配置步骤

1. 注册/登录高德开放平台：https://console.amap.com
2. 创建应用，获取 Web 服务 API Key
3. 在 `~/.openclaw/credentials/` 下创建 `amap.json`，格式如下：

```json
{
  "amap": {
    "api_key": "你的API Key"
  }
}
```

## API 端点

- **路径规划**：`https://restapi.amap.com/v3/direction/:type`
- **地理编码**：`https://restapi.amap.com/v3/geocode/geo`
- **距离测量**：`https://restapi.amap.com/v3/distance`

### 支持的出行方式（type）

| type | 说明 |
|------|------|
| `bicycling` | 骑行（自行车） |
| `driving` | 驾车 |
| `walking` | 步行 |

## 使用示例

### 骑行路线查询

```bash
AMAP_KEY="你的Key"
FROM="南京"
TO="景德镇"

# 地理编码
FROM_LOC=$(curl -s "https://restapi.amap.com/v3/geocode/geo?address=${FROM}&key=${AMAP_KEY}" | python3 -c "import sys,json; print(json.load(sys.stdin)['geocodes'][0]['location'])")
TO_LOC=$(curl -s "https://restapi.amap.com/v3/geocode/geo?address=${TO}&key=${AMAP_KEY}" | python3 -c "import sys,json; print(json.load(sys.stdin)['geocodes'][0]['location'])")

# 路径规划
curl -s "https://restapi.amap.com/v3/direction/bicycling?origin=${FROM_LOC}&destination=${TO_LOC}&key=${AMAP_KEY}"
```

### 输出格式

返回 JSON，包含：
- `距离`（米）
- `时间`（秒）
- `路线`（途经节点）

## 依赖

- `python3` + `requests`
- `ffmpeg`（如需音频处理）
- `jq`（JSON 处理，可选）

## 注意事项

- 高德地图 API 有每日调用配额限制（个人开发者 sufficient）
- 骑行路线数据可能不包含详细海拔信息
- 部分偏远地区路径数据可能不完整
