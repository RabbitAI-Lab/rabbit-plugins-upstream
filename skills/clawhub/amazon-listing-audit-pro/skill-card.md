## Description: <br>
Amazon Listing Audit Pro audits Amazon product listings for sellers by scoring eight listing dimensions, benchmarking category leaders, identifying keyword gaps, and producing data-backed optimization recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, agencies, and operators use this skill to evaluate Amazon listing health, compare against category leaders, find keyword gaps, and prioritize listing improvements for single-ASIN or bulk audits. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a ZooData API key and performs ZooData network calls. <br>
Mitigation: Install only when sharing a ZooData API key with this workflow is acceptable, keep API credentials scoped to ZooData use, and avoid unrelated CLI subcommands unless separately reviewed. <br>
Risk: Listing audits consume ZooData account credits, especially broad or bulk scans. <br>
Mitigation: Confirm estimated credit cost before multi-call scans and use granular commands when a lower credit cap is required. <br>
Risk: The review fallback can create temporary /tmp/review_<ASIN>_* working directories. <br>
Mitigation: Delete temporary review fallback directories after use, especially on shared systems. <br>
Risk: Recommendations depend on sampled ZooData API signals and may include inferred or directional conclusions. <br>
Mitigation: Preserve confidence labels, include data provenance and API usage in reports, and validate important business decisions with additional sources before acting. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/apiclaw/skills/amazon-listing-audit-pro) <br>
- [Skill metadata homepage](https://github.com/SerendipityOneInc/ZooData-Skills) <br>
- [ZooData](https://zoodata.ai) <br>
- [ZooData API documentation](https://api.zoodata.ai/api-docs) <br>
- [Listing Audit Pro API Field Reference](references/reference.md) <br>
- [ZooData CLI Contract](references/cli-contract.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports with scorecards, audit sections, provenance tables, API usage summaries, and optional shell command guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs match the user's language and label conclusions as data-backed, inferred, or directional.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
