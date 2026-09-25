## Description:

Multi search engine integration with 16 engines (7 CN + 9 Global). Supports advanced search operators, time filters, site search, privacy engines, and WolframAlpha knowledge queries. No API keys required.

This skill is ready for commercial/non-commercial use.

## Publisher:

[woai36d](https://clawhub.ai/user/woai36d)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to run multi-source web searches across Chinese and global search providers, apply advanced search operators, and summarize results without API keys.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search query text can be sent to Google, Baidu, Sogou, Startpage, DuckDuckGo, Brave, WolframAlpha, and other third-party providers.

Mitigation: Avoid secrets, personal data, account identifiers, confidential project names, and regulated or jurisdiction-sensitive terms; choose providers explicitly when needed.

Risk: The artifact privacy notice claims no external data transmission, but the skill behavior depends on external search requests.

Mitigation: Treat searches as external network activity and review the provider list and query content before use.

Risk: Automated multi-engine searching can trigger provider rate limits or access denial.

Mitigation: Use the documented batching and delay controls, respect provider terms, and reduce provider count for repeated or high-volume searches.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/woai36d/skills/multi-search-engine)
- [Advanced Search Reference](references/advanced-search.md)
- [International Search Reference](references/international-search.md)
- [Version History](CHANGELOG.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Guidance]

**Output Format:** [Markdown search report with inline web_fetch examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search queries may be sent to selected third-party search providers; no API keys are required.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
