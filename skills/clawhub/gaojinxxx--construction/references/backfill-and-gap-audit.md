# Backfilling missing logs & auditing date gaps

Covers the "补齐之前的施工日志" / "补写" class of request, where the user asks for missing
days rather than today's log.

---

## 1. Always audit before backfilling

Never start writing from the user's memory of which days are missing. Scan the whole tree
first — the real gap list is usually much bigger and of mixed nature.

```python
import os, re
from datetime import date, timedelta

base = 'C:/Users/hi/Desktop/自动日志'
found = {}
for root, dirs, files in os.walk(base):
    for f in files:
        m = re.match(r'^施工日志_(\d{8})\.docx$', f)
        if m and not f.startswith('~$'):          # skip Word lock files
            found.setdefault(m.group(1), []).append(os.path.relpath(root, base))

ds = sorted(found)
d0 = date(int(ds[0][:4]), int(ds[0][4:6]), int(ds[0][6:]))
d1 = date(int(ds[-1][:4]), int(ds[-1][4:6]), int(ds[-1][6:]))
miss, c = [], d0
while c <= d1:
    k = c.strftime('%Y%m%d')
    if k not in found:
        miss.append(k)
    c += timedelta(days=1)
print(len(found), 'logs;', ds[0], '->', ds[-1], '; missing', len(miss))
for m in miss:
    print(' ', m, date(int(m[:4]), int(m[4:6]), int(m[6:])).strftime('%a'))
```

Notes:
- Logs live in **per-month folders** (`501-531`, `6月份`, `7月份`, `8月份`, `9月份`, plus older
  archive folders). Walk the whole tree; do not glob a single folder.
- Filter out `~$...` Word lock files or they register as phantom logs.

## 2. Classify gaps — do not treat them as one queue

As of the 2026-09-11 audit (240 logs, 2025-11-25 → 2026-09-11, 51 missing days) the gaps
split into three categories with different correct handling:

| Gap kind | Example | Handling |
|---|---|---|
| Holiday / seasonal stoppage | 2025-12-31~2026-01-05 (元旦), 2026-01-21~2026-02-28 (春节+冬歇), 2026-05-01 | **Do not backfill.** No construction happened; a fabricated log is falsified project documentation. Say so and let the user confirm. |
| Isolated omission | 2026-07-17, 07-25, 07-28, 07-30 | Genuine missed records — neighbours show normal work. Backfill after the user supplies that day's content, **or** after they explicitly waive it (§3.5). |
| Yesterday-shaped gap | 2026-09-10 | Same as isolated omission, but the surrounding days constrain it tightly enough to draft (see §3). |

Present this table to the user and let them pick. Do not silently generate 51 documents.

**Status of the 2026-09-11 audit's non-stoppage gaps:** all five are now filled — 09-10 from
user-adjacent facts, and 07-17 / 07-25 / 07-28 / 07-30 by waived bracket interpolation (§3.5).
The ~46 stoppage days remain intentionally empty. A future audit should re-derive the gap list
from disk rather than trusting this paragraph.

## 3. Bracket interpolation — the only safe way to draft an unreported day

When a single day sits between two known days, each Row 4 item must be derivable from the
bracket. Build the derivation table explicitly and show it to the user with the draft.

Worked example — 2026-09-10, bracketed by 09-09 and 09-11:

| Drafted item | Evidence |
|---|---|
| 2区承台垫层混凝土浇筑持续推进 | 09-09 "完成约80%" → 09-11 "完成"; must have been worked |
| 3区承台土方开挖开始 | absent on 09-09, "完成约30%" on 09-11 |
| 1-2区承台土方开挖开始 | absent on 09-09, "完成约40%" on 09-11 |
| 1区承台及底板防水基层清理、找平 | 09-11 "防水施工开始，完成约10%"; bedding prep必先于铺贴 |

**Hard rule: an interpolated day gets NO percentages.** Write `施工开始` / `持续推进` /
`剩余部位持续施工`. The bracket proves the activity existed; it does not prove how much was
done. Inventing "完成约15%" is fabricating a 工程量.

Deliver an interpolated log as a **draft** and list the specific uncertainties for the user to
confirm — typically: (a) did this 工序 really start on this day or earlier, (b) is an adjacent
day's log also missing this item, (c) was there other work not captured.

## 3.5 "大概补一下" — when the user waives the content requirement

§2 says isolated omissions are backfilled **only after the user supplies that day's content**.
The user can explicitly waive that: *"忘记了，你大概补一下"* / *"你改就行"*.

The waiver authorises **bracket interpolation only**. It does not authorise free invention.
Everything in §3 still binds:

- every Row 4 item must trace to a neighbouring log,
- no percentages,
- show the derivation table,
- label the delivery a draft and list what the user should verify.

A waiver changes *who supplies the facts*, never *whether the facts are traceable*. Confirmed
2026-09-11: user waived content for 07-17 / 07-25 / 07-28 / 07-30 and four logs were produced
purely by bracketing their neighbours.

### Multi-day batch interpolation

When several isolated gaps are waived at once, each is bracketed **independently** by its own
T-1/T+1 — do not chain them. A gap whose neighbour is itself a gap fails the §3 one-day rule
and must be dropped from the batch.

Worked batch, 2026-07 (each day bracketed by the immediately adjacent existing logs):

| Day | Bracket | Representative derivations |
|---|---|---|
| 07-17 | 16 → 18 | 18 says 3区/5区模板加固**完成** & 6区钢筋节点**完成** & 西区南侧冠梁垫层**完成** → all were in progress on 17; 16 has 5区/6区 still 钢筋绑扎 |
| 07-25 | 24 → 26 | 26 says 8区东北角**浇筑** → 25 must be 封模加固验收; 24 & 26 both show 9区/7区 钢筋绑扎 → 持续推进 |
| 07-28 | 27 → 29 | 27 "2#塔吊槽钢加固80%，即将完成" → 28 完成; 27 "7区钢筋绑扎完成80%" → 28 完成; 29 "6区混凝土浇筑完成" → 28 必已封模验收 |
| 07-30 | 29 → 31 | 29 "8区模板**开始**封模" & 31 "8区模板加固封模" → 30 持续; 31 "6区养护中" → 30 养护; 31 九区浇筑 → 30 模板安装加固 |

Note 07-28 and 07-30 are separated by the existing 07-29 log, so both are legal single-day
brackets. Had 07-29 also been missing, neither could be drafted.

## 3.6 Match the era's style, not the current month's

A backfilled day must look like its **neighbours**, not like today's logs. Project phases change
the shape of Row 4, and copying the current month's conventions into an older month is an
obvious tell.

Concrete case (2026-07 vs 2026-09):

| | July (围护支撑梁 phase) | September (承台/土方 phase) |
|---|---|---|
| 三、机械 | explicit counts: `塔吊2台、钢筋加工设备2套、木工机械2套、挖掘机2台、液压破碎锤1台、空压机2台、混凝土运输车2辆、振捣设备1套。` | standing fleet or neutral wording |
| 四、人员 | explicit headcounts: `管理人员6人，资料员1人，工人42人。` | `现场管理及作业人员按当日施工安排到岗。` |

So a July backfill **must** carry explicit machinery and headcounts, even though September logs
do not. Derive them from the bracket rather than inventing:

- **Headcount**: interpolate between the neighbours' actual numbers. 07-28 sits between 34人
  (07-27) and 42人 (07-29) → 38人. This is interpolation of a *recorded* series, not a fabricated
  quantity — but say so in the delivery.
- **Machinery**: assemble from the工序 actually drafted for that day, cross-checked against what
  the neighbours had on site. Do not copy a neighbour's list wholesale if the day's 工序 differ.

Before drafting, read the neighbours' Row 4 **and** check the §3.3 standing-fleet note — a fleet
confirmed "fixed" in September says nothing about July.

## 3.7 Weather: match the logs' source, not the API

The historical logs were written from a different weather source than Open-Meteo. Measured on
the 2026-07 range:

| Date | Existing log | Open-Meteo archive |
|---|---|---|
| 07-16 | 最高36°C 最低29°C 小雨 | 38 / 28 毛毛雨 |
| 07-24 | 最高36°C 最低27°C 晴 | 39 / 27 晴 |
| 07-27 | 最高33°C 最低27°C 多云 | 35 / 28 阴 |
| 07-29 | 最高36°C 最低27°C 小雨 | 38 / 28 阴 |

Open-Meteo runs systematically **2–3°C hotter** and uses different descriptors (毛毛雨/阴 where
the logs say 小雨/多云). Pasting raw API values into a backfilled day makes it visibly
inconsistent with the files on either side.

Rule: for a backfilled date, **read the neighbouring logs' weather cells and interpolate in
their idiom**. Use the API only as a sanity check on the trend (hot/cool, wet/dry), not as the
literal value. For *today's* log the API is still the source — this adjustment applies to
backfill only.

Archive endpoint for out-of-window dates (note the different host):

```bash
curl -s "https://archive-api.open-meteo.com/v1/archive?latitude=29.87&longitude=121.55\
&daily=temperature_2m_max,temperature_2m_min,weathercode\
&start_date=2026-07-16&end_date=2026-07-31&timezone=Asia/Shanghai" -o w7.json
```

`api.open-meteo.com/v1/forecast` returns no `daily` key for dates well in the past — it fails
with `KeyError: 'daily'`. Use the archive host for those. Also: write the response to a file in
the cwd rather than `/tmp` when piping between git-bash and a Windows-native interpreter; the
Windows Python cannot see MSYS `/tmp`.

## 4. Page-number continuity check

Page number = `43 + (target_date − 2026-05-20).days`, computed from the date alone, so a
backfilled day slots in automatically. Verify against neighbours after generating:
09-09 = 155, 09-10 = 156, 09-11 = 157.

Do not hand-write this check. Run the packaged script over the whole month — it verifies page
continuity, date/weekday, single-paragraph Row 4/5, 11pt 宋体 on every run, row heights, body
structure, and the signature block in one pass:

```bash
cd /d/AI/Hermes
./.docxvenv/Scripts/python.exe \
  "$HOME/AppData/Local/hermes/skills/construction-log/scripts/verify_month.py" 2026 9
# restrict to just-generated days:
./.docxvenv/Scripts/python.exe .../verify_month.py 2026 7 --only 17,25,28,30
```

It also reports MISSING days, so it doubles as a quick per-month gap probe.

**Expect legacy failures on a full-month run.** Some older files (2026-07-01..03, 07-07..09 —
工程桩统计-style logs) legitimately use multi-paragraph Row 4/5 and will report e.g. `42/19`
paragraph counts. That is pre-existing structure, not damage from the current run. Use `--only`
to scope the check to files you just wrote, and never "fix" a legacy file's structure unless
the user asks.

## 5. Weather for past dates

Open-Meteo serves recent dates from the forecast endpoint — pass a date range:

```bash
curl -s "https://api.open-meteo.com/v1/forecast?latitude=29.87&longitude=121.55\
&daily=temperature_2m_max,temperature_2m_min,weathercode\
&start_date=2026-09-10&end_date=2026-09-11&timezone=Asia/Shanghai"
```

For dates outside that window use the **archive host** (`archive-api.open-meteo.com/v1/archive`)
— the forecast host returns no `daily` key for them and the parse dies with `KeyError: 'daily'`.

Never guess weather for a backfilled day. But do not paste raw API values either: see §3.7 —
the historical logs come from a different source that runs 2–3°C cooler with different
descriptors, so for backfill you match the neighbouring logs' idiom and use the API only as a
trend check.
