---
name: build-airport-va-dashboard
description: Generate, rebuild, or update a single-file Smart Airport video-analytics HTML dashboard from face-record Excel workbooks, with camera/date/hour filters, traffic and demographic charts, comparison metrics, data-quality reporting, and in-browser Excel upload for future refreshes without editing source code.
version: 1.0.0
metadata:
  openclaw:
    requires:
      bins:
        - python3
    emoji: "🛫"
---

# Build Airport VA Dashboard

Create a production-ready single-page HTML dashboard from face-record Excel data. Preserve an existing HTML's visual language when supplied, but correct its aggregation defects rather than copying them.

## Required workflow

1. Read `references/dashboard-contract.md` completely.
2. Inspect every relevant workbook sheet, headers, row count, timestamp range, nulls, distinct cameras, and representative values using available spreadsheet or Python tooling.
3. If a reference HTML is supplied, inspect its visible sections, filters, chart types, grouping configuration, embedded data, responsive behavior, and event handlers. Treat it as a design and feature reference, not as authoritative calculation logic.
4. Build one `.html` file that:
   - opens directly in a modern browser without a backend;
   - initially shows the supplied workbook data;
   - accepts a replacement `.xlsx` or `.xls` through file selection and drag-and-drop;
   - validates, parses, aggregates, and rerenders all views in-browser;
   - never requires the user to edit JavaScript to refresh data.
5. Put business rules and camera groups in clearly labeled configuration objects near the top of the application code.
6. Run `python3 scripts/validate_dashboard.py OUTPUT.html`. Fix every error before delivery and assess every warning.
7. When browser tooling is available, open the HTML and verify initial load, filters, reset, empty states, responsive layout, tooltips, comparison logic, and at least one Excel re-upload. Check the browser console for errors. If browser tooling is unavailable, disclose the unperformed visual checks.

## Implementation rules

- Derive every KPI and chart from one shared filtered aggregate. Never maintain independent chart-specific totals.
- Aggregate uploaded rows into camera × date × hour buckets with nested gender, age, and eyewear counts. Discard unnecessary image-path fields after parsing to keep 300k–500k row workbooks usable.
- Compute demographics exactly from matching timestamped rows. Do not scale full-day demographics by a time-range fraction.
- Compute weekday traffic from each record's actual date. Do not distribute an overall average across weekdays.
- Make the comparison selector visibly affect at least Total Detections and the trend chart. Return `N/A` when a valid comparison period is unavailable or its denominator is zero.
- Treat hours after the latest timestamp on a partial final day as unavailable, not observed zero traffic.
- Keep labels and displayed metadata dynamic. Do not hardcode record totals, date ranges, camera counts, or latest-update text.
- Preserve camera identifiers as strings.
- Prefer embedded spreadsheet and chart libraries for fully offline output. If only CDN dependencies are feasible, keep the artifact as one HTML file and disclose that first load requires internet access.
- Process Excel locally in the browser. Do not send workbooks or face-record data to a remote service unless the user explicitly requests a backend.
- Do not add portrait/panoramic image browsing unless requested; those columns are not needed for this dashboard.

## Output and handoff

Deliver the final HTML with a concise note covering:

- source workbook and detected sheet;
- record, camera, and date coverage;
- whether third-party libraries are embedded or CDN-loaded;
- which browser checks were completed;
- how to refresh data: open the HTML, select or drop a same-schema Excel file, wait for validation, and confirm the new filename/date range in Data Status.

If the user requests a reusable update workflow, retain the same HTML and replace data only through its upload control. Regenerate the HTML only when schema, calculations, camera groups, or design requirements change.
