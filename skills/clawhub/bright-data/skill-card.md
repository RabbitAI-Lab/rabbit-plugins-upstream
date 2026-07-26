## Description: <br>
Bright Data provides web scraping and Google search through Bright Data APIs, returning scraped pages as markdown and search results as structured JSON. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[meirkad](https://clawhub.ai/user/meirkad) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to route Google searches and webpage scraping requests through Bright Data when they need structured SERP JSON or markdown page content. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Scraping or search requests can disclose sensitive, internal, credentialed, or confidential URLs and queries to Bright Data. <br>
Mitigation: Use only non-sensitive targets and queries, avoid credentialed or internal URLs, and review requests before execution. <br>
Risk: Bright Data API usage can create costs and may be subject to legal or target-site restrictions. <br>
Mitigation: Use scoped API keys and zones, monitor usage and costs, and confirm scraping complies with applicable law and target-site rules. <br>
Risk: The scripts require Bright Data credentials in environment variables. <br>
Mitigation: Use scoped credentials and keep API keys out of prompts, logs, and committed files. <br>


## Reference(s): <br>
- [Bright Data Dashboard](https://brightdata.com/cp) <br>
- [Bright Data request API endpoint](https://api.brightdata.com/request) <br>
- [ClawHub Bright Data skill page](https://clawhub.ai/meirkad/skills/bright-data) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, JSON, shell commands, configuration] <br>
**Output Format:** [Markdown for scrape output and JSON for search output, invoked through shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires BRIGHTDATA_API_KEY and BRIGHTDATA_UNLOCKER_ZONE; search accepts an optional pagination cursor.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
