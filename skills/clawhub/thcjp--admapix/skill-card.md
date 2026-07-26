## Description: <br>
Admapix is a thin client that helps agents query AdMapix advertising, app, ranking, download, revenue, distribution, and market endpoints and return the raw structured JSON responses. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers, marketers, and research agents use this skill to retrieve raw AdMapix data for ad creative monitoring, app market research, competitor SDK review, store ranking checks, and cross-region download or revenue comparisons. The calling agent is responsible for choosing endpoints, combining requests, and performing any analysis after data retrieval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Queries send AdMapix search terms, app IDs, developer IDs, countries, date ranges, and similar research targets to the AdMapix service. <br>
Mitigation: Use the skill only when third-party disclosure to AdMapix is approved, and avoid confidential or regulated target lists unless organizational policy permits it. <br>
Risk: The skill requires an AdMapix API key for X-API-Key authentication. <br>
Mitigation: Keep ADMAPIX_API_KEY in the environment, do not paste it into chat, and do not print, store, or place the key in URLs or logs. <br>
Risk: Download and revenue endpoints return third-party estimates rather than official reported figures. <br>
Mitigation: Label download and revenue results as estimates and avoid using them as financial source-of-truth data. <br>
Risk: Invalid parameters, rate limits, service errors, or endpoint permission limits can affect query results. <br>
Mitigation: Validate available codes with filter-options or endpoint-specific metadata, handle empty lists as valid results, and retry rate-limited or transient service errors conservatively. <br>


## Reference(s): <br>
- [ClawHub Admapix skill page](https://clawhub.ai/thcjp/skills/admapix) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>
- [SkillHub homepage](https://skillhub.cn) <br>
- [AdMapix service](https://www.admapix.com) <br>
- [AdMapix API host](https://api.admapix.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash/curl snippets and raw JSON API responses.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns unmodified AdMapix API JSON; creative search page_size is capped at 10; download and revenue values are third-party estimates.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata; artifact frontmatter reports 1.0.31) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
