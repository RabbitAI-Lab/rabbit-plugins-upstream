## Description: <br>
Extracts Airbnb accommodation search results from a destination query via SSR-embedded data, returning listing ID, URL, name, coordinates, rating, price, photos, badge info, and pagination cursors for multi-page retrieval. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[browseract-cli](https://clawhub.ai/user/browseract-cli) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to navigate public Airbnb search results pages and extract structured accommodation listing data for a destination query. It is intended for browser-based workflows that read information already available on the loaded page without login or access-control bypass. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill navigates Airbnb pages and executes bundled Python-generated browser JavaScript in the active browser context. <br>
Mitigation: Run it only on intended public Airbnb search pages and review the generated script behavior before use in sensitive browser sessions. <br>
Risk: Airbnb page structure or anti-scraping behavior may change, causing extraction failures or incomplete results. <br>
Mitigation: Follow the documented wait-and-retry flow, test one or two pages before batch pagination, and save results page by page for resumption. <br>
Risk: The skill may keep brief local troubleshooting notes when extraction behavior changes. <br>
Mitigation: Keep notes limited to operational observations and avoid recording user queries, listing result contents, or other task outputs. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, JSON] <br>
**Output Format:** [Markdown instructions with inline shell commands and generated browser JavaScript; extracted listing results are returned as JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns listing fields such as id, URL, name, coordinates, rating, price, photos, badges, count, total_pages, and pagination cursors; per-page output defaults to up to 18 listings.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
