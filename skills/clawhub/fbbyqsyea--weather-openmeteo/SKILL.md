---
name: weather
description: Query current, hourly, 15-minutely, 16-day weather, history/archive, air quality + pollen, marine waves, river flood, weather alerts, elevation for any city or coordinates via free Open-Meteo APIs (no key). Units switching, model choice, batch/compare, geocoding filters. Use for temperature/rain/snow/wind/UV/AQI/pollen/waves/flood/packing advice.
---

# Weather (Open-Meteo 全家桶)

纯标准库脚本，无 API key，带本地缓存（默认 TTL 600s）。所有"现在/当前小时"按**目标城市时区**
（API 返回的 utc_offset_seconds）计算，与本机时钟无关。

```bash
python3 scripts/weather.py <command> <city> [options]
```

## 命令一览

| Command | 数据源端点 | 给出 |
|---|---|---|
| `now <city>` | api…/v1/forecast current | 温度/体感/湿度/露点/天气码/风+阵风/降水分解雨雪/云量/气压/能见度/CAPE/雪深/昼夜 |
| `hourly <city> --hours N` | forecast hourly | 未来逐小时（≤168），含 UV、能见度 |
| `minutely <city> --count N` | forecast minutely_15 | 未来 15 分钟级（最多 96 条 = 24 小时），短期带伞判断用 |
| `daily <city> --days N` | forecast daily | 最多 16 天：高低温/降水概率与量/雨雪分列/降水时长/日照/可照时数/UV/最大风/阵风/风向/日出日落 |
| `past <city> --days N` | forecast past_days | 过去 N 天实况（同 daily 字段） |
| `history <city> --days N` | historical-forecast-api | 近期历史（约 1 个月保存储；超范围自动回落 archive） |
| `archive <city> --start --end` | archive-api | 1940 年起任意历史区间（需 YYYY-MM-DD） |
| `climate <city> --start --end` | climate-api | CMIP6 气候情景未来预估（-50~100年，模式平均；`--models` 传 climate_models） |
| `ensemble <city> --models gfs_seamless` | ensemble-api | 集合预报成员逐时温度 + 成员间扩散度（best_match 会被拒，必须指定单一模型） |
| `air <city>` | air-quality-api | US AQI+欧洲AQI+PM2.5/PM10/O₃/NO₂/SO₂/CO/沙尘/AOD/UV + 花粉6种（分地区，取不到自动跳过）；`--trend N` 未来N小时AQI序列 |
| `marine <city>` 或 `--lat --lon` | marine-api | 浪高/浪周期/浪向（current+2天daily）；用海岸坐标 |
| `flood <city>` 或 `--lat --lon` | flood-api | 最近 92 天 + 未来 7 天 河流流量 m³/s（网格站点） |
| `nowcast <city>` | nowcast-api | ECAD 降水临近预报（过去+未来各30分钟，15分钟粒度）。该域名与 alerts 同样存在 DNS 不可达地区，自动降级 |
| `alerts <city>` | alerts-api | 官方 CAP 天气预警；域名解析失败时自动降级返回 error 字段不崩 |
| `elevation <city>` | api…/v1/elevation | 海拔（host 是 api.open-meteo.com，不是 elevation-api.*） |
| `batch "城市1,城市2,..."` | forecast | 多点当前天气+空气（一次循环，别反复单查） |
| `compare A..B` 或 `compare A B` | forecast | 两（多）地对比 |
| `full <city>` | 上面多个 | now+daily+hourly+minutely+air+alerts+可执行建议，一次调用 |

## 通用选项

- `--json` 机器可读输出（给模型用，优先）
- `--lat <lat> --lon <lon>` 跳过地名解析；歧义/精确坐标场景必用
- `--country CN` 地名的国家码过滤，消歧（两位码）
- `--units metric|imperial|ms` 公制/华氏英里英寸/风速 m/s
- `--models ecmwf_ifs025,gfs_seamless` 指定预报模型（默认 best_match 自动混合；ensemble 命令下为必选单一模型，climate 下映射 climate_models）
- `--trend N` 仅 air：未来 N 小时逐时 AQI（≤48）
- `--no-cache` 强制刷新；`--no-air` / `--no-alerts` 在 full 里跳过可选源
- `--days`（daily/past/history/full，≤16）`--hours`（hourly/full，≤168）`--count`（minutely，≤96）
- `--start/--end` 仅 archive
- 环境变量：`WEATHER_CACHE_TTL`、`WEATHER_CACHE_DIR`

退出码：`0` 成功 / `1` 网络失败（重试3次后；HTTP 4xx 不重试）/ `2` 地名未找到。

## 推荐流程

1. "天气如何" → `full <city> --json` 一次拿全，引用其中数字，不要凭气候常识补数。
2. 特指某天 → 从 `daily` 里取那天；特指"今晚/明早" → `hourly`；一两小时内 → `minutely`。
3. 带伞/穿衣/跑步建议 → 直接用 `advice` 数组（阈值集中在 ADVICE_THRESHOLDS，表驱动可审计）。
4. 花粉季过敏 → `air --json` 看 `pollen`；历史对比/复盘 → `history`/`archive`；
   海边 → `marine`；汛期河汛 → `flood`；灾害预警 → `alerts`。

## 实测坑（都会咬人）

- **时区**：所有时间是目标城市当地时区；脚本绝不读本机时钟。别拿输出里的 17:45 跟你手腕上的时间比。
- **US AQI**：美国标尺，不是中国 AQI 指数；中国无公开 API 支持（cn_aqi 参数不被服务接受）。
- **alerts-api.open-meteo.com 在部分网络 DNS 无法解析**（本工作站实测 NO_DNS）。已内置降级：
  `alerts` 返回 error 字段、`full` 里 alerts 为 null，**不会**拖垮其余数据。
- **`--start/--end` 只配 archive/climate**；其他命令带上会直接报错（不再 400 后一头雾水）。
- **batch/compare 走真批量**：一次 HTTP 逗号多坐标（forecast/air 均支持数组返回），不要循环单查。
- **geocoding 精度**：语言 zh 返回中文名（london→倫敦）；区/街道级细地址（"北京市东城"）常搜不到
  → 用 `--lat --lon` 或加 `--country`；POI 名（万寿公园）可直接命中。地名歧义时输出里的
  `resolved`/`place` 先核对。
- **archive 端点不认 forecast_days**（会 400）；archive/history 的 daily 没有降水概率字段（历史模式无此量）。
- **花粉变量按地区支持不一**（实测北京 alder/birch/grass/mugwort/olive/ragweed 可用，
  部分欧洲种返回 400）→ 脚本用第二次请求，取不到置 null，不报错。
- **flood**：返回的是 0.1° 网格上最近的水文站点，place 只是坐标标注，不是真城市。
- **marine** 要海岸坐标，内陆城市返回 wave=0 属正常。
- **minutely_15 共 96 条**（未来 24 小时），再往后用 hourly/daily。
- **models**：非默认模型只回该模型分辨率（ecmwf_ifs025 会把坐标吸附 0.05° 网格），经纬度小数位变化是预期。
- **额度**：免费档宽松但非无限。缓存按完整 URL 命中；多城市请用 `batch`/`compare`，别在循环里刷单查。
- 坏缓存文件会被当作未命中自动重抓；HTTP 4xx 视为参数错误直接失败不重试。

## 数据源（全部免 key）

- `https://geocoding-api.open-meteo.com/v1/search`
- `https://api.open-meteo.com/v1/forecast`
- `https://api.open-meteo.com/v1/elevation`
- `https://archive-api.open-meteo.com/v1/archive`
- `https://historical-forecast-api.open-meteo.com/v1/forecast`
- `https://air-quality-api.open-meteo.com/v1/air-quality`
- `https://marine-api.open-meteo.com/v1/marine`
- `https://flood-api.open-meteo.com/v1/flood`
- `https://alerts-api.open-meteo.com/v1/alerts`
- `https://nowcast-api.open-meteo.com/v1/nowcast`
- `https://climate-api.open-meteo.com/v1/climate`
- `https://ensemble-api.open-meteo.com/v1/ensemble`

发布输出需注明数据来自 Open-Meteo。明确不支持（实测）：等压面变量（wind_speed_850hpa 等）不在
免费 forecast API；CN 指数 AQI 参数不被服务接受；卫星/雷达图无公开免费 API。
historical-forecast 保存储约 1 个月（history 命令自动算昨天往前的区间）。
