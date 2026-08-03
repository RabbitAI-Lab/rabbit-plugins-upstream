## Description: <br>
Deep consumer insights from 1B+ pre-analyzed Amazon reviews, extracting pain points, buying factors, user profiles, usage patterns, differentiation opportunities, competitor sentiment comparisons, and listing-copy suggestions across 11 analysis dimensions using ZooData. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and product or research teams use this skill to analyze Amazon reviews for a single ASIN, compare competitors, or study category-wide sentiment with ZooData-backed review and product data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: ZooData receives the configured API key and Amazon product or category parameters needed for review and product research. <br>
Mitigation: Install and run the skill only when ZooData use is intended, configure ZOODATA_API_KEY deliberately, and keep requests scoped to the ASINs, keywords, categories, marketplace/date values, and filters required for the task. <br>
Risk: Broad or composite scans can consume ZooData API credits. <br>
Mitigation: Review credit estimates before multi-call workflows and use granular commands when operating under a credit cap. <br>
Risk: Small review samples or fallback aggregation can make percentage-based conclusions look stronger than the evidence supports. <br>
Mitigation: Show sample-size advisories, report counts alongside percentages, and demote single-mention findings before presenting conclusions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/apiclaw/skills/amazon-review-intelligence-extractor) <br>
- [Publisher profile](https://clawhub.ai/user/apiclaw) <br>
- [ZooData API field reference](references/reference.md) <br>
- [ZooData API key setup](https://zoodata.ai/en/api-keys) <br>
- [ZooData API base endpoint](https://api.zoodata.ai/openapi/v2) <br>
- [Metadata homepage](https://github.com/SerendipityOneInc/ZooData-Skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports with inline shell commands and structured ZooData API outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZOODATA_API_KEY; can produce review snapshots, ranked pain points, positives, buying factors, improvement suggestions, consumer profiles, competitor comparisons, listing copy suggestions, differentiation roadmaps, data provenance, and API usage notes.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
