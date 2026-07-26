## Description: <br>
Query Google Trends for interest-over-time, by-region, and related queries for a keyword, and pull real-time trending searches for a country as structured JSON using Scavio's v2 Google Trends API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[scavio-ai](https://clawhub.ai/user/scavio-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, SEO practitioners, and market researchers use this skill to query Google Trends interest over time, interest by region, related queries, related topics, and real-time trending searches through Scavio's API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Trend queries, locations, date ranges, and filters are sent to Scavio using SCAVIO_API_KEY. <br>
Mitigation: Avoid sending secrets, private customer names, sensitive business plans, or other confidential material in trend queries. <br>
Risk: Google Trends values are relative interest indexes rather than absolute search counts. <br>
Mitigation: Describe trend values as relative 0-100 interest and return only data received from the API. <br>
Risk: The skill depends on a valid Scavio API key and paid or free usage credits. <br>
Mitigation: Confirm SCAVIO_API_KEY is configured and handle 401, 429, 502, and 503 responses before retrying or reporting results. <br>


## Reference(s): <br>
- [Scavio Google Trends documentation](https://scavio.dev/docs/google-trends) <br>
- [Scavio rate limits documentation](https://scavio.dev/docs/rate-limits) <br>
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/scavio-google-trends) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/scavio-ai) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Guidance, Shell commands, Code] <br>
**Output Format:** [Markdown guidance with JSON responses, API request details, shell setup commands, and example code] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; each documented Scavio Google Trends endpoint call costs 1 credit.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
