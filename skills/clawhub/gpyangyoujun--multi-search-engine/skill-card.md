## Description: <br>
Multi search engine integration with 16 engines (7 CN + 9 Global). Supports advanced search operators, time filters, site search, privacy engines, and WolframAlpha knowledge queries. No API keys required. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gpyangyoujun](https://clawhub.ai/user/gpyangyoujun) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to route web search queries across Chinese and international search engines, apply advanced search operators and time filters, and aggregate results without API keys. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search terms and request metadata are sent to selected third-party search engines. <br>
Mitigation: Avoid secrets, credentials, internal hostnames, confidential business topics, regulated data, and sensitive personal queries. <br>
Risk: Search-engine requests may be subject to provider rate limits, access controls, robots policies, and terms of service. <br>
Mitigation: Use the documented rate limiting, query only relevant engines, and confirm that the intended use complies with each provider's terms. <br>
Risk: The skill's privacy notice understates third-party query exposure. <br>
Mitigation: Treat searches as external disclosures and review provider routing before using the skill for non-public topics. <br>


## Reference(s): <br>
- [ClawHub listing](https://clawhub.ai/gpyangyoujun/skills/multi-search-engine) <br>
- [Domestic search guide](references/advanced-search.md) <br>
- [International search guide](references/international-search.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls, Markdown] <br>
**Output Format:** [Markdown search report with web_fetch JSON call examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses selected search-engine URLs and does not require API keys.] <br>

## Skill Version(s): <br>
2.1.3 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
