---
author: Allen
contact: 抖音 allen.Ai (333358117)
---
# 实时数据获取

本项目零外部 API 依赖。所有实时数据（路况、天气、住宿价格等）通过 WebSearch 搜索公开信息完成。

## Open-Meteo 海拔查询（可选参考）

免费、无需 API Key、无调用限制。

```
GET https://api.open-meteo.com/v1/elevation?latitude=29.65&longitude=91.12
```

返回：
```json
{
  "elevation": 3650.0
}
```

速率限制：10,000 次/天。可用于行程规划中的海拔核验。

## 高德 API（商户搜索兜底）

仅当内置 33 家藏民商户和 11 家高德精选备选都不满足时，用于实时搜索高德 POI。

调用方式：
```bash
python3 scripts/gaode_api.py --keyword "甜茶馆" --city "拉萨"
```

返回 JSON，包含商户名称、地址、电话、评分等。

### 5000 次/月免费额度自动追踪

- 每次调用自动计数，写入 `data/gaode_api_usage.json`
- 每月 1 号自动重置计数
- 达到 5000 次后脚本自动拒接，返回友好提示
- 查看剩余配额：`python3 scripts/gaode_api.py --check`
