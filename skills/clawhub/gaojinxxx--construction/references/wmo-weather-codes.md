# WMO Weather Code Reference (Open-Meteo)

Used for fetching weather in Ningbo Zhenhai (lat=29.87, lon=121.55).

## API Endpoint
```
https://api.open-meteo.com/v1/forecast?latitude=29.87&longitude=121.55&daily=temperature_2m_max,temperature_2m_min,weathercode&start_date=YYYY-MM-DD&end_date=YYYY-MM-DD&timezone=Asia/Shanghai
```

## WMO Code to Chinese Description

| Code | Description (EN) | Chinese Description |
|------|-------------------|---------------------|
| 0 | Clear sky | 晴 |
| 1 | Mainly clear | 晴间多云 |
| 2 | Partly cloudy | 多云间晴 |
| 3 | Overcast | 多云/阴 |
| 45 | Foggy | 雾 |
| 48 | Depositing rime fog | 雾凇 |
| 51 | Light drizzle | 小毛毛雨 |
| 53 | Moderate drizzle | 毛毛雨 |
| 55 | Dense drizzle | 大毛毛雨 |
| 56 | Freezing light drizzle | 冻毛毛雨 |
| 57 | Freezing dense drizzle | 冻雨 |
| 61 | Slight rain | 小雨 |
| 63 | Moderate rain | 中雨 |
| 65 | Heavy rain | 大雨 |
| 66 | Light freezing rain | 小冻雨 |
| 67 | Heavy freezing rain | 大冻雨 |
| 71 | Slight snow fall | 小雪 |
| 73 | Moderate snow fall | 中雪 |
| 75 | Heavy snow fall | 大雪 |
| 77 | Snow grains | 雪粒 |
| 80 | Slight rain showers | 小阵雨 |
| 81 | Moderate rain showers | 阵雨 |
| 82 | Violent rain showers | 大阵雨 |
| 85 | Slight snow showers | 小阵雪 |
| 86 | Heavy snow showers | 大阵雪 |
| 95 | Thunderstorm | 雷阵雨 |
| 96 | Thunderstorm with slight hail | 雷阵雨伴小冰雹 |
| 99 | Thunderstorm with heavy hail | 雷阵雨伴大冰雹 |

## June Ningbo Weather Patterns
- Typical max: 28-31 C, min: 18-24 C
- Common codes: 2, 3, 61, 63, 80-81, 95
- Weather phrase format: `Highest XX C Lowest XX C <description>`
