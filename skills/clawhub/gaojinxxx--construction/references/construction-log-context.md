# 施工日志项目详情

## Project: 镇海区综合体育中心建设工程
## Template: 甬筑表C01-8 (construction log format)

### Template Structure (docx internal table)

The docx contains a single 4-column × 6-row table:

| Row | Cell Content |
|-----|-------------|
| 0 | 表格编号 \| 甬筑表C01-8 \| 页号 \| [page number] |
| 1 | 工程名称 \| 镇海区综合体育中心建设工程 (span 3 cols) |
| 2 | 日期 \| [YY年MM月DD日 星期X] \| 天气 \| [最高XX°C 最低XX°C 天气] |
| 3 | 施工内容及情况（施工部位、内容、机械、人员等）(span 4 cols) |
| 4 | 一、现场情况：... (span 4 cols) — contains all site content |
| 5 | 技术质量安全工作记录存在问题及处理情况：... (span 4 cols) |

### Formatting Rules

- Page size: A4 (210×297mm)
- Table cell text: 宋体 (SimSun)
- Page number (页号): sz=21 (42 half-points)
- Content text: sz=18 (36 half-points)
- 1.5x line spacing, 3pt before/after paragraph spacing
- Paragraphs separated by `<w:br/>`

### Page Number Calculation

基准页号 = 43 (2026-05-20)
目标日期页号 = 43 + (目标日期 - 2026-05-20).days

### Content Continuity Rules

1. User-provided construction content MUST be used verbatim — never rephrase.
2. Only generate/fill content when user hasn't specified it.
3. Previous day's ongoing work → "养护中"/"验收中" for next day.
4. New items start from foundation excavation.
5. Personnel: 6 management + 1 documentation + 15-25 workers (varies by phase).
6. Weather defaults: early June ~28-31°C / 22-24°C, cloudy with light rain.

### File Locations (from user's setup)

- Template: `C:\Users\hi\Desktop\桌面文件\自动日志\施工日志_20260520.docx`
- Output: `C:\Users\hi\Desktop\桌面文件\自动日志\501-531\施工日志_YYYYMMDD.docx`
- June logs should go to `6月份/` directory (not yet created)

### Weather Lookup

Use Open-Meteo API for Ningbo/Zhenhai area:
```
https://api.open-meteo.com/v1/forecast?latitude=29.87&longitude=121.55&daily=temperature_2m_max,temperature_2m_min,weathercode,precipitation_sum&start_date=YYYY-MM-DD&end_date=YYYY-MM-DD&timezone=Asia/Shanghai
```

Ningbo coordinates: 29.87°N, 121.55°E
Weather code 0 = clear, 1 = main clear, 61 = light rain, etc.
