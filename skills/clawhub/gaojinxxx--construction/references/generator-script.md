# 生成每日施工日志.py — Reference

Located at: `/mnt/c/Users/hi/Desktop/自动日志/生成每日施工日志.py`

## How it works

The script reads the template docx, fills in:
- **Paragraph 2** → `施工记录：YYYY年MM月DD日`
- **Row 0, Cell 3** → page number
- **Row 1, Cell 1** → project name (`镇海区综合体育中心建设工程`)
- **Row 2, Cell 1** → Chinese date format
- **Row 2, Cell 3** → weather string
- **Row 4, Cell 0** → scene content (from `--scene-file`)
- **Row 5, Cell 0** → safety content (from `--safety-file`)

Does NOT modify Row 3 (keeps template default: `施工内容及情况：（施工部位、内容、机械、人员等）`)

## ⚠️ Known bug — external paragraph duplication

Lines 51-53 of the script also write external paragraphs OUTSIDE the table:
```python
doc.paragraphs[1].text = "项目技术负责人：________________________"
doc.paragraphs[2].text = plain_record_date(dt)
```

Since the safety file (`--safety-file`) already contains these lines inside Row 5, the generated docx has **duplicated content** — both inside Row 5 and as standalone paragraphs after the table.

**Post-generation fix**: run the cleanup script (see SKILL.md §Post-generation cleanup) to remove the 2 external paragraphs, keeping only the "施工日志" title.

## Scene file content pattern

Each work item = ONE sentence. Structure:
```
一、现场情况：
1、[工序]施工，[作业内容描述]，[质量控制/验收]。

二、材料：
混凝土、钢筋、模板等材料按需进场，满足当日施工需求。

三、机械：
混凝土运输车N辆、振捣设备N套、小型挖机N台、大型挖机（260）N台。

四、人员：
管理人员6人，资料员1人，工人N人。
```

## Safety file content pattern

```
技术质量安全工作记录存在问题及处理情况：
1、[质量安全控制措施]。
2、[安全巡查/整改情况]。
...
N、[天气相关的安全注意事项]。
项目技术负责人：________________________
施工记录：YYYY年MM月DD日
```

## Key defaults

- **Base page**: 43 (2026-05-20)
- **Page formula**: `43 + (target_date - 2026-05-20).days`
- **Output dir (June)**: `/mnt/c/Users/hi/Desktop/自动日志/6月份/`
- **Output dir (May)**: `/mnt/c/Users/hi/Desktop/自动日志/501-531/`
- **Template**: `/mnt/c/Users/hi/Desktop/自动日志/501-531/施工日志_20260520.docx`
- **Project name**: 镇海区综合体育中心建设工程

## Weather data sources

- **wttr.in** (quick lookup): `curl -s "wttr.in/Ningbo?m&lang=zh&1"` — gives 4-part daily forecast in Chinese
- **Open-Meteo API** (structured data): `https://api.open-meteo.com/v1/forecast?latitude=29.87&longitude=121.55&daily=temperature_2m_max,temperature_2m_min,weathercode&start_date=YYYY-MM-DD&end_date=YYYY-MM-DD&timezone=Asia/Shanghai`

## Typical weather format (June, Ningbo/Zhenhai)

`最高27°C 最低23°C 零星小雨转多云` or `最高29°C 最低24°C 阴转多云`
