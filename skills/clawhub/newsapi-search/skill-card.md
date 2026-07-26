## Description: <br>
Search news articles via NewsAPI with filtering by time windows, sources, domains, and languages. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hegghammer](https://clawhub.ai/user/hegghammer) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, researchers, and analysts use this skill to query NewsAPI for article search, breaking headlines, and source discovery with time, language, source, domain, pagination, and sorting filters. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search terms and filters are sent to newsapi.org. <br>
Mitigation: Do not submit confidential queries, personal data, or sensitive investigation terms unless that sharing is acceptable for the use case. <br>
Risk: The skill loads variables from ~/.openclaw/.env even though it only needs NEWSAPI_KEY. <br>
Mitigation: Use a dedicated NewsAPI key and keep unrelated secrets out of ~/.openclaw/.env. <br>


## Reference(s): <br>
- [NewsAPI](https://newsapi.org) <br>
- [Everything Endpoint](https://newsapi.org/v2/everything) <br>
- [Top Headlines Endpoint](https://newsapi.org/v2/top-headlines) <br>
- [Sources Endpoint](https://newsapi.org/v2/top-headlines/sources) <br>
- [NewsAPI Parameter Reference](references/api-reference.md) <br>
- [NewsAPI Search Examples](references/examples.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands; CLI commands return structured JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires NEWSAPI_KEY in ~/.openclaw/.env and sends requests to NewsAPI.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
