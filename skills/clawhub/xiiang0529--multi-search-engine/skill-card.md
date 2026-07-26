## Description: <br>
Multi search engine integration with 16 engines (7 CN + 9 Global), advanced search operators, time filters, site search, privacy engines, and WolframAlpha knowledge queries without API keys. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xiiang0529](https://clawhub.ai/user/xiiang0529) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to route search queries across Chinese and international search engines, apply advanced search operators, and summarize aggregated search results. It is intended for normal search and knowledge lookup workflows where users can choose providers and evaluate result quality. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search terms are sent to third-party search engines and may be logged or processed under those providers' privacy practices. <br>
Mitigation: Do not use secrets, credentials, internal project names, regulated data, or sensitive personal queries unless the provider is explicitly chosen and its privacy practices are acceptable. <br>
Risk: The artifact privacy notice says there is no external data transmission, but the skill's core behavior sends queries to external search engines. <br>
Mitigation: Treat searches as external network requests and correct user-facing privacy notices before relying on the skill in sensitive environments. <br>


## Reference(s): <br>
- [Domestic Search Guide](references/advanced-search.md) <br>
- [International Search Guide](references/international-search.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Text] <br>
**Output Format:** [Markdown with inline web_fetch examples and summarized search reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search requests may contact third-party search engines and use in-memory session cookies when access is denied.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
