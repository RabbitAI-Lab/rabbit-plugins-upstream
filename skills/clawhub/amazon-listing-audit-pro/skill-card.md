## Description: <br>
Amazon Listing Audit Pro audits Amazon listings with ZooData data, scoring listings across eight dimensions, benchmarking against category leaders, identifying keyword gaps, and generating optimization recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Amazon sellers, agencies, and commerce operators use this skill to evaluate single ASINs or bulk listing sets, compare them with category leaders, and prioritize listing improvements before acting on business decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends ASINs, keywords, categories, marketplace/date values, and audit parameters to ZooData and consumes API credits. <br>
Mitigation: Use only when the user accepts sharing those audit inputs with ZooData, estimate credit cost before broad scans, and confirm before multi-call or bulk audits. <br>
Risk: An alternate ZOODATA_BASE_URL can redirect API calls to a different host. <br>
Mitigation: Keep ZOODATA_BASE_URL unset unless the alternate host is explicitly trusted. <br>
Risk: The bundled CLI can read a legacy local credential file and create temporary review-analysis files. <br>
Mitigation: Prefer ZOODATA_API_KEY in the environment, use legacy credential files only intentionally, and remove temporary review directories after fallback analysis. <br>
Risk: The shared ZooData CLI exposes endpoints beyond the listing-audit workflow. <br>
Mitigation: Invoke only the documented listing-audit, product, products, market, check, and review-fallback commands needed for this skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/apiclaw/skills/amazon-listing-audit-pro) <br>
- [ZooData API key setup](https://zoodata.ai/en/api-keys) <br>
- [ZooData API endpoint](https://api.zoodata.ai) <br>
- [Skill homepage metadata](https://github.com/SerendipityOneInc/ZooData-Skills) <br>
- [Local API field reference](references/reference.md) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, guidance] <br>
**Output Format:** [Markdown report with tables, confidence labels, API usage, data provenance, and optional shell commands for ZooData CLI execution] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports must match the user's language and include a decision-use disclaimer, confidence labels, endpoint provenance, and credit usage.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence and skill frontmatter metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
