## Description: <br>
Extracts pain points, buying factors, user profiles, usage patterns, competitor review comparisons, and listing-copy suggestions from Amazon review and product data through ZooData. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and ecommerce teams use this skill to analyze Amazon reviews by ASIN, competitor set, or category and produce consumer-insight reports, comparison findings, and listing-copy suggestions grounded in ZooData API results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires access to a ZooData API key. <br>
Mitigation: Prefer ZOODATA_API_KEY in the environment, avoid plaintext config files when possible, and rotate the key if it is exposed. <br>
Risk: ZooData API calls can spend credits during review and product lookups. <br>
Mitigation: Confirm the analysis scope before running calls, use documented page and sample limits, and stop on credit-exhausted responses instead of fabricating missing data. <br>
Risk: Raw-review fallback can create local JSON exports containing review text and related metadata. <br>
Mitigation: Store fallback files in a temporary run directory and delete raw exports when they are no longer needed. <br>
Risk: Changing ZOODATA_BASE_URL can redirect requests away from the default ZooData endpoint. <br>
Mitigation: Set ZOODATA_BASE_URL only to a trusted ZooData-compatible endpoint and verify it before sending credentials. <br>
Risk: Small review samples can overstate percentage-based conclusions. <br>
Mitigation: Surface sample-size warnings, report counts alongside percentages, and treat single-mention findings as directional rather than data-backed. <br>


## Reference(s): <br>
- [Amazon Review Intelligence Extractor on ClawHub](https://clawhub.ai/apiclaw/skills/amazon-review-intelligence-extractor) <br>
- [Publisher homepage from metadata](https://github.com/SerendipityOneInc/ZooData-Skills) <br>
- [ZooData API key setup](https://zoodata.ai/en/api-keys) <br>
- [ZooData API documentation](https://api.zoodata.ai/api-docs) <br>
- [ZooData API field reference](references/reference.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports with structured sections, tables, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZOODATA_API_KEY and may consume ZooData credits; raw-review fallback can create temporary JSON files for review aggregation.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
