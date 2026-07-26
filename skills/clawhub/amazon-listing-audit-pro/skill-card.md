## Description: <br>
Amazon Listing Audit Pro audits Amazon listings across eight dimensions, benchmarks them against category leaders, identifies keyword gaps, and generates data-backed optimization recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Amazon sellers, agencies, and ecommerce operators use this skill to assess listing quality, compare an ASIN against category leaders, find keyword gaps, and prioritize listing improvements. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends ASINs, keywords, competitor context, and review-derived analysis to ZooData using the user's API key. <br>
Mitigation: Use only with data you are authorized to share, review ZooData retention practices, and avoid confidential client portfolios unless sharing is permitted. <br>
Risk: The artifact includes a broader credential-backed research CLI than the listing-audit workflow alone. <br>
Mitigation: Review the available CLI commands before installing or running the skill, and limit execution to commands needed for the listing audit. <br>
Risk: The script can read legacy APICLAW credentials as a fallback. <br>
Mitigation: Set ZOODATA_API_KEY intentionally for this skill and remove or avoid unintended legacy APICLAW credentials. <br>
Risk: The bundled reference material is mismatched to a market-entry analyzer even though this release is a listing-audit skill. <br>
Mitigation: Treat the listing-audit README and SKILL.md as the primary behavior evidence, and verify reference-field usage before relying on generated reports. <br>


## Reference(s): <br>
- [API Field Reference](references/reference.md) <br>
- [ZooData API Documentation](https://api.zoodata.ai/api-docs) <br>
- [ZooData API Key Setup](https://zoodata.ai/en/api-keys) <br>
- [ZooData Skills Homepage](https://github.com/SerendipityOneInc/ZooData-Skills) <br>
- [ClawHub Skill Page](https://clawhub.ai/apiclaw/skills/amazon-listing-audit-pro) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown audit report with tables, confidence labels, API usage, data provenance, and suggested listing rewrites.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZOODATA_API_KEY. Reports should match the user's language and distinguish data-backed, inferred, and directional conclusions.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
