---
name: garmin-analysis-skill
slug: garmin-analysis-skill
displayName: 骑行&健康(Garmin/Intervals.icu/Strava/iGPSPORT/Xingzhe)
version: 0.2.2
summary: 基于 cycling-health CLI，同步 Garmin CN 健康数据到 Intervals.icu，分析 Garmin、Intervals.icu 和 iGPSPORT 骑行与恢复数据，并查询 Strava 骑行活动、路线、装备及行者路书。
license: MIT
description: Structured cycling-health workflows using the public cycling-health CLI. Use when an assistant needs to sync Garmin China Wellness data to Intervals.icu; analyze Garmin sleep, recovery, training ability, activities, events, courses, workouts, plans, trends, or FIT/GPX data; query and compare Intervals.icu Wellness, activities, power, fitness, statistics, settings, sport settings, or calendar events; analyze personal iGPSPORT rides and FIT streams; query personal Strava athlete, zones, cycling activities, laps, streams, routes, gear, or rate limits; query or download Xingzhe route books; sync Garmin China activities to Garmin Global; or report cycling-health issues.
---

# Garmin Analysis Skill

Use `cycling-health` as the source of truth for supported Garmin, Intervals.icu, iGPSPORT, Xingzhe, and Strava operations. The public CLI is available from `https://github.com/baijian/cycling-health`.

## Principles

- Be environment-neutral. Do not assume a home directory, repository checkout, shell profile, or operating system.
- Prefer `cycling-health` from `PATH`. If it is missing, guide installation from the public repository.
- When command execution is available, run `cycling-health upgrade --output json` once before status, synchronization, or analysis commands.
- Prefer `--output json` for collection and analysis.
- Treat Garmin credentials, Intervals.icu API keys, OAuth tokens, passwords, MFA codes, account descriptions, downloaded FIT/GPX files, and exported activity files as sensitive local data. Never ask the user to paste secrets into chat.
- Analyze only returned fields. Do not invent HRV, power, zones, fitness, fatigue, form, FTP, W/kg, or causal relationships.
- Collect in stages. Start with summary/list/statistics calls, then request intervals, streams, curves, raw payloads, or exported files only when the conclusion needs them.
- Separate current recovery from durable ability. A poor night or negative form can affect today's decision without proving fitness loss.
- Preserve genuine CLI warnings and unresolved gaps. Expected no-data responses are already normalized by the CLI and do not need to be restated as failures.
- Keep sources distinct. Garmin is the primary source for device-specific sleep, recovery, training effect, account data, and raw activity detail. Intervals.icu is the primary source for consolidated activity history, server-calculated fitness/fatigue/form, power curves/models, statistics, and cross-activity comparison. iGPSPORT supplies explicitly selected personal rides and FIT sensor streams. Xingzhe supplies route-book metadata and GPX files.
- Treat each global `--profile` as an isolated identity. Do not assume Garmin, Intervals.icu, iGPSPORT, Strava, and Xingzhe profiles belong to the same person or that activities from different sources are duplicates.
- Do not upload Garmin activities directly to Intervals.icu. Preserve the existing Garmin CN to Garmin Global activity sync and the user's Garmin Global to Intervals.icu automatic connection.
- Treat writes conservatively. Preview Garmin Wellness synchronization and Intervals.icu settings/events first; use `--confirm` only after the user has clearly authorized a live write. Never add `--overwrite`, delete credentials/events, or replace a GPX destination without explicit approval after reviewing the effect.

Garmin query-region rules:

- If neither Garmin region is logged in, prompt for login.
- If one region is logged in, use it for Garmin queries.
- If both are logged in and the user did not specify a region, default Garmin queries to `cn`.
- Pass the selected region with `--region cn|global`.
- Garmin CN to Global activity sync requires both regions.
- Garmin to Intervals.icu Wellness sync defaults to `--source garmin-cn`. Use `garmin-global` only when explicitly requested because Intervals.icu can already ingest Garmin Global data through its native connection.

Read the references as needed:

- Read `references/cli-workflows.md` for installation, Garmin authentication, CN-to-Global activity sync, sleep/recovery queries, Garmin ride analysis, file analysis, and Garmin failure handling.
- Read `references/intervals-workflows.md` for Intervals.icu authentication, Garmin CN Wellness sync, Wellness and training-health analysis, activities, power, statistics, settings, sport settings, calendar events, comparisons, and Intervals-specific failure handling.
- Read `references/igpsport-workflows.md` for profile-isolated iGPSPORT authentication, activity/FIT analysis, sensor streams, cache behavior, and unsupported-private-API warnings.
- Read `references/xingzhe-workflows.md` for official Xingzhe OAuth, route-book queries, navigation data, and guarded GPX download.
- Read `references/strava-workflows.md` for official OAuth, personal read-only athlete/activity/route/gear queries, staged stream collection, rate limits, and failure handling.

## Workflow

1. Verify and upgrade the CLI:
   - Run `cycling-health version`.
   - Run `cycling-health upgrade --output json` once per invocation.
   - If upgrade fails, preserve the error and ask before continuing with the installed version unless the user already authorized that fallback.
   - Verify the requested top-level source and subcommand with `--help` after upgrade. If missing, report that the installed public CLI is too old instead of improvising another client or raw API call.

2. Check only the authentication needed for the task:
   - Garmin query or CN-to-Global activity sync: run `cycling-health garmin status --output json` and apply the region rules above.
   - Intervals.icu query: run `cycling-health intervals athlete --output json`.
   - Garmin Wellness to Intervals.icu sync: verify Intervals.icu with `intervals athlete` and Garmin CN with `garmin status --region cn`.
   - iGPSPORT task: run `cycling-health --profile PROFILE igpsport auth status --output json`; preserve the requested profile and account description.
   - Xingzhe task: run `cycling-health --profile PROFILE xingzhe auth status --output json`.
   - Strava task: run `cycling-health --profile PROFILE strava auth status --output json`, then query only the athlete, activity, route, gear, or rate-limit data needed for the request.

3. Route the task:
   - Garmin CN activity sync: inspect sync status, then run incremental sync by default.
   - Garmin Wellness sync: preview Garmin CN changes, inspect conflicts/warnings, then confirm only when authorized.
   - Garmin sleep/recovery: use wake-date-aware sleep and summary queries, then add selected health metrics.
   - Garmin single ride or device-specific analysis: start with Garmin activity details and add extended/raw/file data only as needed.
   - Garmin account, trend, race, course, workout, training-plan, achievement, nutrition, or lifestyle query: use only the matching read-only command family and preserve region-specific warnings.
   - Intervals.icu riding health, long-term fitness, power, statistics, or comparison: start with Wellness, activity list, power model/curves, and aggregate statistics appropriate to the question.
   - Intervals.icu settings, sport settings, or calendar event task: read current state first and preview any mutation before requesting authorization.
   - iGPSPORT ride analysis: select the profile explicitly, identify the ride from a bounded list, then add FIT analysis or selected sensor streams only as needed.
   - Xingzhe route task: list or fetch route metadata first; download GPX only when requested and never overwrite an existing path without explicit approval.
   - Strava query: start with athlete or bounded list metadata, then fetch one activity/route, laps, streams, zones, or gear only when needed.

4. Report results:
   - Lead with the conclusion.
   - State date ranges and data source for each conclusion.
   - State the selected region/profile and account description when they affect identity or source ownership.
   - Separate observed values, interpretation, confidence/gaps, and next actions.
   - Use compact units such as km, h:min, bpm, W, W/kg, rpm, m, CTL, ATL, and percent.
   - For writes, report previewed changes, conflicts, uploaded records, verified records, and warnings.

## Task Guidance

### Sync Garmin China Activities To Garmin Global

Use when the user asks to mirror or backfill Garmin China activities into Garmin Global.

1. Confirm both regions are logged in.
2. Inspect `garmin syncstatus`.
3. Run `garmin sync --new-only` unless the user explicitly requests historical backfill.
4. Report retried, synced, failed, and last activity time.

Do not treat this as a direct Intervals.icu upload. The user's Garmin Global connection handles subsequent activity ingestion into Intervals.icu.

### Sync Garmin Health To Intervals.icu

Use when the user asks to sync Garmin health, sleep, recovery, or Wellness data to Intervals.icu.

1. Default to Garmin CN and a seven-day range unless the user provides dates.
2. Verify Garmin CN and Intervals.icu authentication.
3. Run `intervals wellness sync --source garmin-cn` without `--confirm` first.
4. Inspect field-level `changes`, `conflicts`, `warnings`, and record actions.
5. If there are no changes, stop; do not issue a confirmed no-op merely for appearance.
6. If the user already clearly requested a live sync, or confirms after seeing the preview, rerun the same range with `--confirm`.
7. Skip conflicting existing values by default. Use `--overwrite --confirm` only after the user explicitly approves replacing them.
8. Report `changedRecords`, `changedFields`, `conflictFields`, `uploadedRecords`, and `verifiedRecords`.

The automatic mapping currently covers sleep duration, sleep score, average sleeping heart rate, overnight HRV, resting heart rate, daily average SpO2, average sleeping respiration, and steps. Missing Garmin values are omitted. Do not reinterpret Garmin stress, Body Battery, training readiness, calories burned, or training load as Intervals.icu Wellness fields.

### Sleep Query And Analysis

Use when the user asks about sleep duration, stages, score, overnight HRV, resting heart rate, stress, Body Battery, readiness, or recent sleep trends.

1. Resolve a night by wake date and include the adjacent prior date in sleep lookup.
2. Start with sleep list plus wake-date daily summary.
3. Default recent trends to seven days; use 14-30 days for an explicit baseline/trend question.
4. Add only the health metrics needed for the question.
5. Check adjacent-date and summary fallbacks before declaring sleep details unavailable.
6. Compare with the user's available baseline and avoid medical diagnosis.

### Garmin Cycling Query And Analysis

Use Garmin when the question depends on Garmin training effect/status/readiness, device zones, detailed laps/splits, gear/weather, or local FIT/GPX records.

1. Classify the request as single ride, durable ability/progression, or today's training decision.
2. Start a single ride with `garmin activity get`; use extended/raw/file analysis only for missing detail.
3. For ability, default to 90 days and add direct cycling FTP, max metrics, endurance score, hill score, and body weight only when relevant.
4. Use activity progress only for requested axes.
5. Keep recovery/readiness separate from durable ability.
6. Account for terrain, weather, equipment, and sensor coverage; speed alone is not fitness.

### Garmin Extended Queries

Use the dedicated read-only Garmin command families for health trends, races/events, saved courses, workouts, training plans, achievements, activity extensions, gear, account settings, nutrition, and lifestyle records. Query only fields relevant to the user's question, keep CN and Global results labeled, and preserve endpoint warnings because some private Garmin responses can differ by region or account.

### Intervals.icu Cycling Query And Analysis

Use Intervals.icu when the user asks about riding health/fitness, consolidated training history, eFTP, CTL/ATL/form, power curves/models, aggregate statistics, or comparisons.

1. Choose the smallest useful date range and identify `Ride` records when activity lists include multiple sports.
2. For daily health/recovery, query Wellness. For training health, combine aggregate fitness, fatigue, form, ramp rate, load, and eFTP from statistics; do not conflate these with subjective Wellness values.
3. For one ride, identify it with list/search, fetch detail, then add intervals, streams, best efforts, or activity-analysis endpoints only as needed.
4. For power ability, start with the current MMP model and `42d,1y,all` curves; add per-activity duration values or power-versus-heart-rate data for progression or efficiency questions.
5. For statistics, use a recent range and, when comparison is requested, a preceding non-overlapping range of equal length.
6. Compare like with like: same duration, sport, units, and comparable terrain/workout type. Show absolute and percentage change only when both values are valid.
7. Use Intervals.icu server-calculated values as returned. Do not silently recompute or combine duplicate Garmin/Intervals activity records.
8. Correlate Wellness and performance cautiously; date alignment supports context, not causation.

For Intervals.icu settings, sport settings, and calendar events, query the current object first. Preview settings updates with `--dry-run`; preview event uploads and reconcile with a stable `external_id`; delete only with `--confirm`. Garmin events require explicit mapping and review because there is no automatic Garmin-to-Intervals event-sync command.

### iGPSPORT Cycling Query And Analysis

Use iGPSPORT only for the selected personal account profile. Start with a bounded activity list and metadata detail, then use FIT analysis or selected streams for speed, heart rate, cadence, elevation, power, GPS, temperature, laps, or sessions. Report missing channels as sensor coverage, not API failure, when the FIT file lacks them. Label the source as an unsupported private iGPSPORT CN integration and do not merge it with Garmin or Intervals records unless identity and duplication have been established.

### Xingzhe Route Query And Download

Use Xingzhe for route books, route navigation/elevation/climb data, and explicitly requested GPX downloads. Query `mine` or `collects` with pages of at most 20 records. Download to a user-approved destination; do not use `--overwrite` without explicit authorization. The CLI does not upload the GPX to Garmin, so report the local path and leave Garmin Connect/device import as a separate step.

### Strava Read-Only Queries

Use Strava for the authenticated user's athlete profile/zones, cycling activity lists and details, laps, selected streams, routes, route streams, gear, and API rate limits. Start with bounded list or summary data and request detailed streams only when the question needs them. Preserve the selected profile, date range, activity/route IDs, granted scopes, sensor gaps, and returned rate-limit metadata. The CLI is read-only and does not upload, update, delete, synchronize, or cache Strava API data; authorization revocation is a separate destructive action that requires `--confirm`.

## Usage Examples

These examples assume `cycling-health version`, the once-per-invocation
upgrade check, and the required authentication checks have already succeeded.
Replace dates, IDs, profiles, and paths with values from the user's request.

### Example 1: Sync Garmin CN Health To Intervals.icu

User request: "把 7 月 20 日到 7 月 26 日的 Garmin CN 健康数据同步到
Intervals.icu。"

Preview first:

```bash
cycling-health garmin status --region cn --output json
cycling-health intervals athlete --output json
cycling-health intervals wellness sync \
  --source garmin-cn --start 2026-07-20 --end 2026-07-26 \
  --output json
```

If the preview contains intended changes and the user authorized this live
sync, rerun the exact range with `--confirm`:

```bash
cycling-health intervals wellness sync \
  --source garmin-cn --start 2026-07-20 --end 2026-07-26 \
  --confirm --output json
```

Report changed/conflicting fields, uploaded and verified dates, and warnings.
Do not add `--overwrite` unless differing existing values were reviewed and
the user explicitly approved replacing them.

### Example 2: Explain Last Night's Recovery

User request: "分析一下我 7 月 26 日早上醒来的睡眠和恢复情况。"

```bash
cycling-health garmin sleep list \
  --region cn --start 2026-07-25 --end 2026-07-26 --output json
cycling-health garmin summary get \
  --region cn --date 2026-07-26 --output json
cycling-health garmin health get \
  --region cn --start 2026-07-25 --end 2026-07-26 \
  --metrics hrv,rhr,stress,bb,respiration,spo2 --output json
```

Lead with sleep duration/score and recovery direction. Then cite available
sleep stages, overnight HRV versus baseline, resting HR, stress, Body Battery,
respiration, and SpO2. Keep today's readiness separate from durable fitness and
preserve any missing-day or endpoint warnings.

### Example 3: Compare Two Intervals.icu Training Blocks

User request: "比较最近四周和之前四周的骑行状态与功率变化。"

```bash
cycling-health intervals stats summary \
  --start 2026-06-29 --end 2026-07-26 --output json
cycling-health intervals stats summary \
  --start 2026-06-01 --end 2026-06-28 --output json
cycling-health intervals power curves \
  --curves 42d,1y,all --sport Ride --output json
cycling-health intervals power activities \
  --days 90 --durations 5,60,300,1200,3600 \
  --sport Ride --output json
```

Compare equal, non-overlapping ranges. Report volume, elevation, load, fitness,
fatigue, form, ramp rate, eFTP/eFTP/kg, and aligned power durations when
present. Distinguish repeated recent ability from one peak effort and state
terrain, sensor, and weight limitations.

### Example 4: Inspect A Strava Cycling Activity

User request: "查一下 Strava 最近的骑行，并看看其中一次的圈段、功率和装备。"

```bash
cycling-health strava activity list \
  --start 2026-07-01 --end 2026-07-26 \
  --page 1 --per-page 30 --output json
cycling-health strava activity get \
  --activity-id ACTIVITY_ID --output json
cycling-health strava activity laps \
  --activity-id ACTIVITY_ID --output json
cycling-health strava activity streams \
  --activity-id ACTIVITY_ID \
  --keys time,distance,heartrate,cadence,watts --output json
cycling-health strava gear get \
  --gear-id GEAR_ID --output json
```

Select a cycling record from the bounded list before requesting detail. Resolve
gear only when the activity returns a gear ID, and request only available
streams needed for the question. Include observed rate-limit metadata and
distinguish missing sensor streams from API errors.

### Example 5: Analyze An iGPSPORT Ride From Another Profile

User request: "分析 child 账号 7 月份最近一次骑行的心率、踏频和功率。"

```bash
cycling-health --profile child igpsport account get --output json
cycling-health --profile child igpsport activity list \
  --start 2026-07-01 --end 2026-07-31 \
  --page 1 --per-page 20 --output json
cycling-health --profile child igpsport activity analyze \
  --activity-id RIDE_ID --output json
cycling-health --profile child igpsport activity streams \
  --activity-id RIDE_ID \
  --channels speed,heart_rate,cadence,elevation,power \
  --resolution 10s --max-points 5000 --output json
```

Keep the `child` profile on every command and report its account description.
Use FIT-derived channels only when recorded by the device/sensors, and do not
merge this ride with another profile's Garmin or Intervals.icu history.

### Example 6: Find And Download A Xingzhe Route Book

User request: "从我收藏的行者路书里找到目标路线，下载 GPX 给 Garmin 用。"

```bash
cycling-health xingzhe route list \
  --collection collects --offset 0 --limit 20 --output json
cycling-health xingzhe route get \
  --route-id ROUTE_ID --output json
cycling-health xingzhe route download \
  --route-id ROUTE_ID --path /absolute/path/route.gpx --output json
```

Choose the route from title, distance, sport, elevation, and climb/navigation
data before downloading. Never add `--overwrite` without explicit approval.
Report the saved absolute path and clarify that Garmin Connect or device import
is a separate step.

## Feedback And Issues

For installation problems, supported-source data gaps, synchronization failures, or analysis issues, direct users to the Discord feedback channel:

```text
https://discord.gg/R6xPZc5Dg
```
