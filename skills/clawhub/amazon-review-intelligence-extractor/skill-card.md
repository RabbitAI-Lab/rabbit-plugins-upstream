## Description: <br>
Extracts Amazon review intelligence from ZooData across pain points, buying factors, user profiles, usage patterns, competitor sentiment, and listing-copy opportunities. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to analyze Amazon product reviews or categories, compare competing ASINs, identify customer pain points and buying factors, and draft review-informed listing recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a ZooData API key and sends product-analysis inputs to ZooData. <br>
Mitigation: Use the skill only when sharing ASINs, keywords, category paths, marketplace/date values, and numeric filters with ZooData is acceptable; avoid sending unrelated user-profile text. <br>
Risk: Broad or composite analyses can consume paid API credits. <br>
Mitigation: Ask for a credit estimate and user confirmation before broad scans or multi-call review-deepdive workflows. <br>
Risk: Small review samples can overstate pain-point frequency or sentiment conclusions. <br>
Mitigation: Apply the skill's sample-size advisory, report counts with percentages, and avoid strong conclusions when review coverage is below the documented threshold. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/apiclaw/skills/amazon-review-intelligence-extractor) <br>
- [Publisher profile](https://clawhub.ai/user/apiclaw) <br>
- [ZooData-Skills repository](https://github.com/SerendipityOneInc/ZooData-Skills) <br>
- [ZooData](https://zoodata.ai) <br>
- [ZooData API key setup](https://zoodata.ai/en/api-keys) <br>
- [ZooData API field reference](references/reference.md) <br>
- [ZooData CLI contract](references/cli-contract.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports with structured review findings, provenance tables, API-usage summaries, and inline shell commands when needed] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs match the user's language, label conclusions by confidence, and should report only data returned by ZooData or the local fallback workflow.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata; artifact metadata reports 1.0.9) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
