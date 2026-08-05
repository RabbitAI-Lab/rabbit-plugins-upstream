## Description: <br>
Automated product opportunity scanner for Amazon sellers that scans categories with preset strategies, validates candidates with ZooData market signals, brand analysis, and price structure, then ranks opportunities by composite score. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Amazon sellers and commerce researchers use this skill to discover product opportunities when they have not chosen a target product yet. It translates seller profile and criteria into ZooData-backed category scans, product rankings, risk alerts, and next-step guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: ZooData calls send Amazon keywords, category paths, ASINs, marketplace/date values, and numeric filters to ZooData and consume account credits. <br>
Mitigation: Confirm broad multi-call scans before running them, set ZOODATA_API_KEY explicitly, and use granular commands when operating under a credit cap. <br>
Risk: Review fallback workflows can create /tmp/review_* working directories that may contain review data or intermediate analysis. <br>
Mitigation: Delete review fallback working directories after use when the data should not remain on disk. <br>
Risk: Legacy APICLAW credential configuration may exist on the machine and affect credential resolution. <br>
Mitigation: Check local credential configuration before deployment and prefer the explicit ZOODATA_API_KEY environment variable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/apiclaw/skills/amazon-opportunity-discoverer) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/apiclaw) <br>
- [Skill metadata homepage](https://github.com/SerendipityOneInc/ZooData-Skills) <br>
- [ZooData API documentation](https://api.zoodata.ai/api-docs) <br>
- [ZooData API keys](https://zoodata.ai/en/api-keys) <br>
- [ZooData field reference](artifact/references/reference.md) <br>
- [ZooData CLI contract](artifact/references/cli-contract.md) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, guidance, shell commands] <br>
**Output Format:** [Markdown report with tables, ranked findings, provenance notes, and API usage details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZOODATA_API_KEY and ZooData credits; reports should match the user's language and label confidence for conclusions.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release evidence; artifact metadata reports 1.0.9) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
