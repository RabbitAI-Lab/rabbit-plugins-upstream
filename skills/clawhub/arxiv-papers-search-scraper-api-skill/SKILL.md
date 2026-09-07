---
name: arxiv-papers-search-scraper-api-skill
description: "This skill helps users run the arXiv Papers Search Scraper BrowserAct template and extract structured public data. Use this skill when users ask to collect arxiv papers search scraper data, scrape arxiv papers search scraper results, monitor public records from this source, export structured records for analysis, compare listings or products, enrich a dataset with public web fields, gather market research evidence, collect pricing or availability signals, retrieve review or rating data, automate repeatable public data extraction, build a lead or research list, or call the BrowserAct template by API."
metadata: {"openclaw":{"emoji":"🌐","requires":{"bins":["python"],"env":["BROWSERACT_API_KEY"]}}}
---

# arXiv Papers Search Scraper Automation Skill

## 📖 Brief
This skill uses BrowserAct's arXiv Papers Search Scraper API template to extract structured public data. It starts the official workflow template, waits for completion, and prints the returned result so the Agent can use the data for research, monitoring, reporting, or downstream automation.

## ✨ Features
1. **No hallucinations, ensuring stable and accurate data extraction**: Pre-set workflows avoid AI generative hallucinations, ensuring stable and precise data extraction.
2. **No CAPTCHA issues**: No need to handle reCAPTCHA or other verification challenges.
3. **No IP restrictions or geo-blocking**: No need to handle regional IP restrictions or geofencing.
4. **Faster execution**: Tasks execute faster compared to pure AI-driven browser automation solutions.
5. **Extremely high cost-efficiency**: Significantly lowers data acquisition costs compared to high-token-consuming AI solutions.

## 🔑 API Key Guide
Before running, check the `BROWSERACT_API_KEY` environment variable. If not set, do not take other measures; ask and wait for the user to provide it.
**Agent must inform the user**:
> "Since you haven't configured the BrowserAct API Key yet, please go to the [BrowserAct Console](https://www.browseract.com/reception/integrations?co-from=arxiv-papers-search-scraper) to get your Key."

## 🛠️ Input Parameters
Agent should configure the following parameters based on user requirements:

1. **base_url**
   - **Type**: `string`
   - **Description**: arXiv base URL without a trailing slash.
   - **Example**: `https://arxiv.org`
   - **Default**: `https://arxiv.org`
2. **keyword**
   - **Type**: `string`
   - **Description**: Search query text.
   - **Example**: `large language model`
   - **Default**: `large language model`
3. **search_type**
   - **Type**: `string`
   - **Description**: arXiv search field, such as all, title, author, abstract, comments, journal_ref, paper_id, doi, or full_text.
   - **Example**: `all`
   - **Default**: `all`
4. **count**
   - **Type**: `number`
   - **Description**: Maximum number of paper records to return.
   - **Example**: `20`
   - **Default**: `20`

## 🚀 Invocation Method
Agent should run the standalone script from this skill directory:

```bash
python -u ./scripts/arxiv_papers_search_scraper_api.py "https://arxiv.org" "large language model" "all" "20"
```

### ⏳ Running Status Monitoring
Since this task involves automated browser operations, it may take several minutes. The script continuously outputs timestamped status logs such as `[14:30:05] Task Status: running`.
**Agent guidelines**:
- Keep monitoring terminal output while waiting for the script result.
- As long as new status logs appear, the task is running normally; do not mistake it for a deadlock or unresponsiveness.
- Only if the status remains unchanged for a long time or the script stops outputting without returning a result should you consider the retry mechanism.

## 📊 Data Output
After successful execution, the script retrieves and prints the BrowserAct API response. The returned data may include these fields:
- `rank`: Extracted rank value when available.
- `title`: Extracted title value when available.
- `arxiv_url`: Extracted arxiv url value when available.
- `arxiv_id`: Extracted arxiv id value when available.
- `authors`: Extracted authors value when available.
- `abstract`: Extracted abstract value when available.
- `categories`: Extracted categories value when available.
- `submitted`: Extracted submitted value when available.
- `comment`: Extracted comment value when available.
- `journal_ref`: Extracted journal ref value when available.
- `pdf_url`: Extracted pdf url value when available.
- `search_keyword`: Extracted search keyword value when available.

Ground conclusions in the extracted data and handle missing fields gracefully.

## ⚠️ Error Handling & Retry
If an error occurs during script execution such as network fluctuations or task failure, the Agent should follow this logic:

1. **Check Output Content**:
   - If the output **contains** `"Invalid authorization"`, it means the API Key is invalid or expired. **Do not retry**; guide the user to re-check and provide the correct API Key.
   - If the output **contains** `"concurrent"` or `"too many running tasks"` or similar concurrency limit messages, it means the current subscription plan's concurrent task limit has been reached. **Do not retry**; guide the user to upgrade their plan.
     **Agent must inform the user**:
     > "The current task cannot be executed because your BrowserAct account has reached the limit of concurrent tasks. Please go to the [BrowserAct Plan Upgrade Page](https://www.browseract.com/reception/recharge) to upgrade your subscription plan and enjoy more concurrent task benefits."
   - If the output **does not contain the above error keywords** but the task failed such as output starts with `Error:` or returns empty results, the Agent should **automatically try to re-execute the script once**.

2. **Retry Limit**:
   - Automatic retry is limited to **one time**. If the second attempt fails, stop retrying and report the specific error information to the user.

## 🌟 Typical Use Cases
1. **Market research**: Collect structured public records for quick analysis.
2. **Competitive monitoring**: Compare public products, listings, reviews, prices, or availability.
3. **Dataset enrichment**: Add clean fields to spreadsheets, CRMs, or BI workflows.
4. **Lead generation**: Identify relevant entities and URLs for downstream outreach.
5. **Review analysis**: Collect ratings and text signals where the template exposes review fields.
6. **Pricing checks**: Track current prices, total prices, or availability where supported.
7. **Content research**: Extract public text, metadata, or search results for editorial workflows.
8. **Trend discovery**: Find ranked or recent records around a destination, keyword, category, or source.
9. **Operational reporting**: Produce repeatable JSON output for scheduled reports.
10. **API automation**: Use BrowserAct workflow results as an input to other applications.
