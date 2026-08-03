## Description: <br>
Automated product opportunity scanner for Amazon sellers that scans categories with preset selection strategies, validates candidates with ZooData signals, and ranks opportunities by composite score. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Amazon sellers and ecommerce operators use this skill to discover product niches, compare category opportunities, and prioritize product candidates using ZooData market, product, review, brand, price, and trend signals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a ZooData API key and can spend ZooData credits during scans. <br>
Mitigation: Prefer ZOODATA_API_KEY over a persistent config file, check estimated credit cost, and confirm before broad or multi-call scans. <br>
Risk: Amazon opportunity reports may be misleading if sampled data, lower-bound sales estimates, or strategy suggestions are treated as final business advice. <br>
Mitigation: Include the required disclaimer, confidence labels, data provenance, and API usage details, and validate promising opportunities with additional sources before acting. <br>
Risk: Review fallback workflows can create temporary /tmp/review_* working folders. <br>
Mitigation: Delete temporary review folders after review fallback work is complete if they are no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/apiclaw/skills/amazon-opportunity-discoverer) <br>
- [ZooData API Field Reference](references/reference.md) <br>
- [ZooData API documentation](https://api.zoodata.ai/api-docs) <br>
- [ZooData API key setup](https://zoodata.ai/en/api-keys) <br>
- [Project homepage](https://github.com/SerendipityOneInc/ZooData-Skills) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown report with ranked opportunity tables, detailed candidate analysis, data provenance, API usage, and inline shell commands when needed.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZOODATA_API_KEY. Broad scans consume ZooData credits and should be confirmed with the user before multi-call execution.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
