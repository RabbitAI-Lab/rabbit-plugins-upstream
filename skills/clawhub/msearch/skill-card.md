## Description: <br>
Aggregates 16 Chinese and international search engines with advanced operators, time filters, site search, privacy-oriented search options, and WolframAlpha knowledge queries without requiring API keys. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sclawbot](https://clawhub.ai/user/sclawbot) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to route web-search queries across Chinese and international search engines, apply common advanced search operators, and summarize aggregated search results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search terms can be transmitted to third-party search engines, including privacy-sensitive or regulated queries. <br>
Mitigation: Avoid confidential, private, regulated, or account-related queries unless the selected search engine and jurisdiction are acceptable for that data. <br>
Risk: The artifact claims all operations remain local, but search requests necessarily disclose query text to external search providers. <br>
Mitigation: Treat external transmission as expected behavior and review the selected engines before deployment. <br>
Risk: Automated search across multiple engines may encounter rate limits, access blocks, or terms-of-service constraints. <br>
Mitigation: Use the documented rate limiting, retry only once after access failures, and ensure use complies with each search engine's terms. <br>


## Reference(s): <br>
- [Multi Search skill page](https://clawhub.ai/sclawbot/skills/msearch) <br>
- [OpenClaw homepage](https://clawhub.ai/sclawbot/msearch) <br>
- [Domestic search engine guide](references/advanced-search.md) <br>
- [International search engine guide](references/international-search.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown search reports with inline web_fetch examples and URL patterns] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search queries may be sent to third-party search engines selected by language, availability, and query intent.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter, metadata.json, server release) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
