## Description: <br>
谷歌搜索工具 helps agents run Google Custom Search API queries and return structured titles, links, and summaries for research, documentation lookup, and current-information retrieval. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, students, researchers, and developers use this skill to search the web through Google Custom Search and collect structured results for research, technical documentation lookup, and current information checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries and Google API credentials are sent to Google as part of normal use. <br>
Mitigation: Use the skill only when Google Custom Search API use is acceptable, keep API keys in environment variables or a local .env file, and avoid including secrets or private data in search queries. <br>
Risk: The skill text contains broad SEO trigger wording that could overstate the tool's scope. <br>
Mitigation: Treat the skill as a Google Custom Search helper for information retrieval, not as SEO automation or paid advertising management. <br>
Risk: The free edition is limited to single-query search and up to 10 results. <br>
Mitigation: Use it for focused searches and choose another workflow when batch search, export, custom site-restricted search, or search history is required. <br>


## Reference(s): <br>
- [Google APIs endpoint](https://www.googleapis.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and structured JSON-style search result descriptions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search results include titles, links, snippets, status metadata, logs, and errors when available; the free edition describes single-query use with up to 10 results.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
