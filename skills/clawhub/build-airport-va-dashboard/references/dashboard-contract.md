# Airport VA dashboard contract

## Input schema

Default sheet: `Face Records`. If absent, use the first non-empty sheet only after reporting the fallback.

Required columns:

| Column | Use |
|---|---|
| `Camera_Name` | Camera identifier; coerce to string without scientific notation |
| `Timestamp` | Detection time; accept Excel dates, serials, and parseable datetime strings |
| `Gender` | `MALE`, `FEMALE`, `GENDER_TYPE_NONE` |
| `Age_Lower_Limit` | Lower age estimate |
| `Age_Up_Limit` | Upper age estimate |
| `Glass_style` | Eyewear classification |

Optional passthrough fields such as `Camera_ID`, `Internal_ID`, image paths, respirator, cap, and mustache must not block loading.

Reject a workbook when it is empty or lacks `Camera_Name` or `Timestamp`. If a demographic column is absent, load traffic views and disable the affected demographic chart with a precise message. Report invalid rows and continue when safe.

## Normalization

- One valid row equals one detection; do not deduplicate.
- Derive local `Date` (`YYYY-MM-DD`), `Hour` (`0`–`23`), and Monday-first weekday from `Timestamp` without UTC date shifting.
- Set `Estimated_Age = (Age_Lower_Limit + Age_Up_Limit) / 2` when both bounds are numeric.
- Age groups: `<18`, `18–25`, `26–35`, `36–45`, `46–55`, `56–65`, `65+`. Missing/invalid age is `Unknown` and is reported separately.
- Gender labels: `MALE → Male`, `FEMALE → Female`, `GENDER_TYPE_NONE → Unclassified`; preserve unexpected values under `Other`.
- Eyewear labels:
  - `GLASSES_STYLE_TYPE_WITHOUT → No Glasses`
  - `TRANSPARENT_GLASSES → Clear Glasses`
  - `SUNGLASSES → Sunglasses`
  - `GLASSES_STYLE_TYPE_NONE → Undetected`
  - unexpected values → `Other`

## Default camera groups

Keep this configuration editable. Ignore configured cameras absent from the current workbook and place unconfigured cameras in `Other Cameras`.

```js
const CAMERA_GROUPS = {
  "All Cameras": ["113034","113042","113043","113044","113046","113051","113054","113059","113066","113067","113068","113322","113323"],
  "Cluster A – Left Gate": ["113066","113067","113068"],
  "Cluster B – Center": ["113042","113043","113044","113059","113322"],
  "Cluster C – Right Gate": ["113034","113323"],
  "Cluster D – Apron South": ["113046","113051","113054"]
};
```

## Filter and comparison state

Filters:

- camera group tabs;
- one optional single-camera selection;
- inclusive date from/to;
- inclusive hour from/to;
- comparison mode: previous day, previous hour slot, same day last week;
- reset to all available cameras, full detected date range, and `00:00–23:00`.

Comparison definitions:

- Previous day: shift every selected date back one calendar day, keeping cameras and hours.
- Same day last week: shift every selected date back seven calendar days.
- Previous hour slot: use the immediately preceding equal-length hour interval. If it crosses outside available data, return `N/A` rather than inventing zeros.
- Show absolute change and percentage change. If comparison total is zero or unavailable, percentage is `N/A`.

## KPI contract

1. Total Detections: filtered valid row count.
2. Male: filtered male count and share of `Male + Female` only.
3. Female: filtered female count and the same denominator.
4. Peak Hour: highest filtered hourly count; show count and use earliest hour for ties.
5. Cameras: number of cameras with at least one filtered detection.
6. Comparison delta: current total versus selected comparison total.

Use full thousands separators. Compact `K` values may supplement but never replace accessible full values or tooltips.

## Visualization contract

- Daily Footfall Trend: line chart; total plus camera series for multi-camera views; dashed comparison series when available.
- Hourly Traffic Pattern: 24-hour bar chart; highlight selected hours; represent unavailable future hours on a partial final day as null.
- Traffic by Day of Week: Monday-to-Sunday bars using actual filtered dates.
- Gender Distribution: doughnut for Male, Female, Unclassified, and Other when present.
- Age Group Distribution: ordered bars; optionally expose Unknown in status rather than distorting defined bins.
- Eyewear Detection: doughnut using normalized labels.
- Camera Comparison: descending horizontal bars with identifier, full count, and share.
- Daily Footfall by Camera: stacked bars by date and camera.

Destroy or update prior chart instances before rendering after upload. Provide accessible chart titles and a tabular or textual fallback for key totals.

## Excel refresh UX

Include both `<input type="file" accept=".xlsx,.xls">` and a keyboard-accessible drag-and-drop zone.

Refresh sequence:

1. Display filename and loading/progress state.
2. Parse workbook client-side with SheetJS or an equivalent browser library.
3. Validate headers before replacing current data.
4. Normalize and build the aggregate cube asynchronously enough for the loading state to paint.
5. Atomically replace the current dataset only after successful parsing.
6. Rebuild date/camera controls and reset invalid filter selections.
7. Rerender KPIs, charts, data status, and comparison results.
8. On failure, keep the previous valid dashboard and show an actionable error.

Do not upload the workbook to a remote service unless the user explicitly requests a backend.

## Data Status

Display:

- current filename and sheet;
- valid/total row counts;
- earliest and latest timestamps;
- camera count;
- invalid timestamp and missing camera counts;
- missing/unknown demographic counts;
- whether the latest date is partial;
- last successful browser-load time.

Show a deliberate empty state for filters with no records.

## Visual baseline

- Dark airport operations aesthetic with restrained blue, green, violet, amber, and pink accents.
- Header, filter bars, five KPI cards, responsive two-column chart grid, and footer/status.
- At widths below roughly 768px, use one chart column and a compact KPI grid.
- Ensure text contrast, keyboard focus, responsive canvases, non-clipped labels, and readable tooltips.
- Preserve a supplied reference HTML's typography and spacing when doing so does not conflict with accessibility or correctness.

## Required code boundaries

Use clearly named functions or equivalent modules:

```text
parseExcel
normalizeRows
applyFilters
aggregateData
calculateComparison
renderDashboard
showDataQuality
```

Keep `REQUIRED_COLUMNS`, mappings, age bins, and `CAMERA_GROUPS` near the top of application code.

## Browser QA

- Initial workbook renders without console errors.
- Uploading the same workbook reproduces totals.
- Uploading an invalid workbook preserves the previous valid view and reports missing headers.
- Camera group, single camera, date, hour, comparison, and reset controls all change the intended results.
- Gender + age + eyewear totals reconcile with valid filtered rows, accounting for unknown categories.
- Daily totals reconcile to Total Detections.
- Camera totals reconcile to Total Detections.
- Partial-day future hours are not presented as observed zeros.
- Desktop and narrow layouts have no clipped controls, legends, or chart titles.
