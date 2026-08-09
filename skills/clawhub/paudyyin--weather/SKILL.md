---
name: weather-moji
description: "Get current weather and forecasts using Moji Weather for China-focused detailed forecasts"
tags: [domain-specific, general, api-integration, cli]
version: 1.0.0
homepage: https://tianqi.moji.com
metadata: {"clawdbot":{"emoji":"🌤�?,"requires":{"bins":["curl"]}}}
---

# Weather - 墨迹天气�?
中国天气查询服务，使用墨迹天气作为主要数据源�?
## 墨迹天气（主要数据源�?
### 查询格式

```bash
# 实时天气 + 三天预报
curl -s "https://tianqi.moji.com/weather/省份/城市/区县"
```

### 示例

```bash
# 上海浦东
curl -s "https://tianqi.moji.com/weather/上海/上海/浦东"

# 山东日照
curl -s "https://tianqi.moji.com/weather/山东/日照/东港"

# 广东佛山顺德
curl -s "https://tianqi.moji.com/weather/广东/佛山/顺德"
```

### 返回内容

- 实时温度、湿度、风力、AQI
- 三天天气预报（日�?天气/温度/风力/AQI�?- 生活提示（穿衣、运动、紫外线等）

### 备用数据�?
如果墨迹天气不可用，使用 MSN 天气�?```bash
curl -s "https://www.msn.cn/zh-cn/weather/"
```

---

## 以下为原�?wttr.in 文档（已弃用�?
Two free services, no API keys needed.

## wttr.in (primary, deprecated)

Quick one-liner:
```bash
curl -s "wttr.in/London?format=3"
# Output: London: ⛅️ +8°C
```

Compact format:
```bash
curl -s "wttr.in/London?format=%l:+%c+%t+%h+%w"
# Output: London: ⛅️ +8°C 71% �?km/h
```

Full forecast:
```bash
curl -s "wttr.in/London?T"
```

Format codes: `%c` condition · `%t` temp · `%h` humidity · `%w` wind · `%l` location · `%m` moon

Tips:
- URL-encode spaces: `wttr.in/New+York`
- Airport codes: `wttr.in/JFK`
- Units: `?m` (metric) `?u` (USCS)
- Today only: `?1` · Current only: `?0`
- PNG: `curl -s "wttr.in/Berlin.png" -o /tmp/weather.png`

## Open-Meteo (fallback, JSON)

Free, no key, good for programmatic use:
```bash
curl -s "https://api.open-meteo.com/v1/forecast?latitude=51.5&longitude=-0.12&current_weather=true"
```

Find coordinates for a city, then query. Returns JSON with temp, windspeed, weathercode.

Docs: https://open-meteo.com/en/docs
