## Description: <br>
Automated product opportunity scanner for Amazon sellers that uses ZooData APIs to scan categories, validate candidates with product and market data, and rank opportunities by composite score. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Amazon sellers and ecommerce researchers use this skill to discover candidate products or niches when they do not yet have a specific target. It turns budget, experience, risk tolerance, category, keyword, and filter inputs into ranked opportunity reports with market, competition, pricing, trend, review, provenance, and API-usage sections. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends product research queries, category paths, ASINs, marketplace/date values, and numeric filters to ZooData as an external API provider. <br>
Mitigation: Install only if ZooData is acceptable for the use case, and avoid entering sensitive business profile text beyond the inputs needed for the scan. <br>
Risk: Broad opportunity scans can consume ZooData API credits. <br>
Mitigation: Estimate and confirm credit cost before multi-call scans, and use quick scans or granular commands when the user has a credit cap. <br>
Risk: The skill requires a ZooData API credential. <br>
Mitigation: Prefer ZOODATA_API_KEY in the environment, avoid plaintext credential storage, and do not continue when the key is missing, invalid, or exhausted. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/apiclaw/skills/amazon-opportunity-discoverer) <br>
- [ZooData](https://zoodata.ai) <br>
- [ZooData API key setup](https://zoodata.ai/en/api-keys) <br>
- [ZooData API docs](https://api.zoodata.ai/api-docs) <br>
- [API field reference](references/reference.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports with tables, ranked opportunities, confidence labels, data provenance, API usage, and occasional shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZOODATA_API_KEY and may consume ZooData API credits.] <br>

## Skill Version(s): <br>
1.0.6 (source: server evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
