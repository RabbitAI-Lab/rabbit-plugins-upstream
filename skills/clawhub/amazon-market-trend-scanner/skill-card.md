## Description: <br>
Scans Amazon category landscapes to discover trending subcategories, emerging niches, and market shifts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, ecommerce operators, and market analysts use this skill to scan Amazon parent categories for growing subcategories, emerging products, concentration risks, price shifts, and market-entry timing signals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends Amazon research inputs, such as categories, keywords, ASINs, dates, and filters, to ZooData and consumes ZooData API credits. <br>
Mitigation: Use the skill only when this data sharing is acceptable, estimate credit cost before broad scans, and confirm with the user before running multi-call workflows. <br>
Risk: The skill requires a ZooData API key and can read a user-home credential file. <br>
Mitigation: Prefer a scoped ZOODATA_API_KEY environment secret and avoid plaintext home configuration where possible. <br>
Risk: Scheduled monitoring keeps scan state such as watchlists, baselines, alerts, and history under the skill's scan-data directory. <br>
Mitigation: Enable monitoring only after explicit user consent and review stored scan-state files for sensitive category or marketplace choices. <br>
Risk: The bundled shared ZooData CLI exposes commands beyond this skill's trend-scanner workflow. <br>
Mitigation: Use only the documented trend-scanner commands for this skill: categories, market, products, and check. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/apiclaw/skills/amazon-market-trend-scanner) <br>
- [ZooData Skills repository](https://github.com/SerendipityOneInc/ZooData-Skills) <br>
- [Market Trend Scanner API Field Reference](references/reference.md) <br>
- [ZooData API documentation](https://api.zoodata.ai/api-docs) <br>
- [ZooData API key setup](https://zoodata.ai/en/api-keys) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown trend reports with data provenance and API usage tables, plus optional shell commands or scheduling configuration.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports should match the user's language and label conclusions as data-backed, inferred, or directional.] <br>

## Skill Version(s): <br>
1.0.6 (source: release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
