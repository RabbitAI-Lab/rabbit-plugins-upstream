# Format Example — Row 4 & Row 5 Paragraph Structure

Each numbered item must be in its **own paragraph** (`add_paragraph()`), not all concatenated.

## Row 4 (现场情况) — Paragraph layout

```
P0: 一、现场情况：
P1: 1、东侧一级坡混凝土浇筑至东南位置，按设计坡度及标高进行混凝土浇筑，振捣密实后整平收面。
P2: 2、南侧排水沟砌体施工，基槽清理后按设计尺寸砌筑，砂浆饱满度及沟底高程同步检查。
P3: 3、6号、5号塔吊钢丝绳安装完成，安装后对钢丝绳连接、卡扣紧固及限位装置逐项检查。
P4: 4、西南角、东南角二级坡修坡施工，按设计放坡比例修整坡面，平整度及坡度检查合格。
P5: 
P6: 二、材料：
P7: 混凝土、水泥、砂石料、砌块等材料按需进场，满足当日施工需求。
P8: 
P9: 三、机械：
P10: 小型挖机1台、大型挖机（260）6台、混凝土运输车2辆、振捣设备2套、汽车吊1台、塔吊2台。
P11: 
P12: 四、人员：
P13: 管理人员6人，资料员1人，工人28人。
```

**Style rules for each item's sentence:**
- One flowing sentence per item — concise, no repetition
- Pattern: `[工序]施工，[准备/清理]，[作业内容]，[质量检查]`
- End with "完成" or implied completion
- Do NOT repeat the item number description in subsequent paragraphs

## Row 5 (技术质量安全记录 + 签名) — Paragraph layout

**CRITICAL:** Row 5 must include "项目技术负责人" and "施工记录" as its final paragraphs. These are NOT external paragraphs — they belong inside the table.

```
P0: 技术质量安全工作记录存在问题及处理情况：
P1: 1、东侧一级坡混凝土浇筑前检查基层处理及模板安装情况，浇筑过程控制坍落度及振捣密实度，浇筑后及时覆盖养护。
P2: 2、南侧排水沟砌体砌筑过程中检查砂浆配合比及砌体垂直度、平整度，确保排水坡度符合要求。
P3: 3、6号、5号塔吊钢丝绳安装过程中设专人指挥，吊装区域设置警戒线，安装完成后检查连接螺栓及限位装置，钢丝绳卡扣紧固到位。
P4: 4、西南角、东南角二级坡修坡过程中检查坡面平整度及坡度，修坡完成后进行边坡检查验收。
P5: 5、今日上午有中雨，混凝土浇筑及砌体施工注意防雨措施，雨后及时排除积水。
P6: 项目技术负责人：________________________
P7: 施工记录：2026年06月14日
```

## Row 3 — TITLE ONLY

Row 3 must contain exactly ONE paragraph:
```
P0: 施工内容及情况：（施工部位、内容、机械、人员等）
```

No additional paragraphs or detailed content in Row 3.

## External paragraphs — remove signature lines only

After generating the docx, the following external paragraphs MUST be deleted from the document body:
1. ❌ The "项目技术负责人" paragraph (after the table) — now inside Row 5, remove external copy
2. ❌ The "施工记录" paragraph (after the table) — now inside Row 5, remove external copy

✅ **KEEP the "施工日志" title paragraph** before the table (22pt centered) — do NOT remove it. The user explicitly corrected this on June 14: the header title must be preserved.

After removal, `<p>施工日志</p>`, `<tbl>`, and `<sectPr>` should remain as top-level elements (in that order).
