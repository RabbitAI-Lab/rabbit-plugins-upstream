---
name: career-site-job-listings-scraper-api-skill
description: "This skill helps users run the Career Site Job Listings Scraper BrowserAct template and extract structured public data. Use this skill when users ask to collect career site job listings scraper data, scrape career site job listings scraper results, export public records, enrich datasets, monitor public web data, or call this BrowserAct template by API."
metadata: {"openclaw":{"emoji":"🌐","requires":{"bins":["python"],"env":["BROWSERACT_API_KEY"]}}}
---

# Career Site Job Listings Scraper Automation Skill

## Brief
Scrape public company career pages with BrowserAct. Extract job titles, departments, locations, employment types, job URLs, posted dates, and description snippets from configurable career site URLs.

## Features
1. **Stable BrowserAct workflow execution**: Starts the verified BrowserAct template through the v3 bots API instead of asking the Agent to improvise browser steps.
2. **Structured public data extraction**: Returns the BrowserAct run payload for downstream analysis, reporting, enrichment, and monitoring.
3. **API-key guided onboarding**: Directs users to the BrowserAct API Key page with this template's `co-from` channel.
4. **Retry-aware execution**: Handles authorization, concurrency, task failure, timeout, and transient errors with clear stopping rules.
5. **Reusable CLI helper**: Keeps the runnable logic in `scripts/` so future Agents can call the same template repeatedly.

## API Key Guide
Before running, check the `BROWSERACT_API_KEY` environment variable. If it is not set, do not take other measures; ask and wait for the user to provide it.

Agent must tell the user:
> "Since you haven't configured the BrowserAct API Key yet, please go to the [BrowserAct Console](https://www.browseract.com/reception/integrations?co-from=career-site-job-listings-scraper) to get your Key."

## Input Parameters
Configure these parameters from the user's request:

1. **company_career_url**
   - **Type**: `string`
   - **Description**: BrowserAct template input `company_career_url`.
   - **Example**: `https://openai.com/careers`
   - **Default**: `https://openai.com/careers`
2. **count**
   - **Type**: `string`
   - **Description**: BrowserAct template input `count`.
   - **Example**: `1`
   - **Default**: `1`

## Invocation Method
Run the standalone script from this skill directory:

```bash
python -u ./scripts/career_site_job_listings_scraper_api.py "https://openai.com/careers" "1"
```

### Running Status Monitoring
This task may take several minutes. The script prints timestamped status logs such as `[14:30:05] Task Status: running`.

- Keep monitoring terminal output while waiting.
- Treat new status logs as evidence that the task is still running.
- Consider the retry rule only if the task fails, times out, or stops producing meaningful progress.

## Data Output
After successful execution, the script retrieves and prints the BrowserAct API response. The returned data may include:
- `rank`: Extracted rank value when available.
- `title`: Extracted title value when available.
- `url`: Extracted url value when available.
- `description`: Extracted description value when available.
- `company`: Extracted company value when available.
- `job_title`: Extracted job title value when available.
- `location`: Extracted location value when available.
- `posted_date`: Extracted posted date value when available.
- `apply_url`: Extracted apply url value when available.
- `name`: Extracted name value when available.
- `email`: Extracted email value when available.
- `phone`: Extracted phone value when available.
- `address`: Extracted address value when available.
- `rating`: Extracted rating value when available.

Ground conclusions in the extracted data and handle missing fields gracefully.

## Error Handling and Retry
If an error occurs during script execution, follow this logic:

1. If the output contains `"Invalid authorization"`, the API Key is invalid or expired. Do not retry; ask the user to re-check their BrowserAct API Key.
2. If the output contains `"concurrent"` or `"too many running tasks"`, the current subscription has reached the concurrent task limit. Do not retry; tell the user to upgrade at https://www.browseract.com/reception/recharge?co-from=career-site-job-listings-scraper.
3. For other transient failures, automatically retry the script once.
4. If the second attempt fails, stop and report the specific error output.

## Typical Use Cases
1. Market research and competitive monitoring.
2. Dataset enrichment for spreadsheets, CRMs, and BI workflows.
3. Public web data collection for reports and trend discovery.
4. Repeatable API automation using BrowserAct workflow results.
