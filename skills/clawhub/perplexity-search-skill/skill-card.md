## Description: <br>
Search the web using Perplexity's Search API for ranked, real-time web results with advanced filtering. Use when you need to search for current information, market research, trending topics, or when Brave Search is unavailable. Supports recency filtering (day/week/month/year) and returns structured results with titles, URLs, and snippets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[m4vf14](https://clawhub.ai/user/m4vf14) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to retrieve current web search results from Perplexity for research, news lookup, market research, and competitive analysis. It supports result-count limits, recency filters, and formatted or raw JSON output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries are sent to Perplexity using the user's API key and may include sensitive user-provided content. <br>
Mitigation: Avoid submitting secrets, regulated personal data, or confidential business information in queries. <br>
Risk: Perplexity API requests may consume paid quota. <br>
Mitigation: Monitor Perplexity usage for the API key used with this skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/m4vf14/skills/perplexity-search-skill) <br>
- [Perplexity API documentation](https://docs.perplexity.ai) <br>
- [Perplexity API key and usage page](https://perplexity.ai/account/api) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration guidance] <br>
**Output Format:** [Formatted terminal text or raw JSON search results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires PERPLEXITY_API_KEY; supports result count from 1 to 10 and optional day, week, month, or year recency filtering.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact skill.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
