## Description: <br>
Looks up Jungle Scout keyword data for up to 10 Amazon ASINs, including search volume, ranking, competition, PPC bid, and relevancy metrics across supported marketplaces. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, marketplace analysts, and agents use this skill to analyze competitor ASIN keyword coverage, discover traffic keywords, compare ASIN rankings, and prepare keyword or advertising research for Amazon marketplaces. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: ASINs, marketplace choices, query filters, API credentials, and workflow metadata are sent to LinkFox. <br>
Mitigation: Install and run only when this data sharing is acceptable; avoid including secrets or sensitive business context in queries or feedback. <br>
Risk: Queries can consume LinkFox credits, and the documented dynamic cost can be high for larger requests. <br>
Mitigation: Confirm marketplace, ASIN count, result count, and expected credit cost with the user before each chargeable query. <br>
Risk: Full and cached API responses are persisted locally under the LinkFox output directories. <br>
Mitigation: Check the configured output path before use in shared or regulated workspaces and remove cached or saved JSON files when they are no longer needed. <br>
Risk: Automatic feedback behavior may report user sentiment or workflow details to LinkFox. <br>
Mitigation: Keep feedback content minimal and do not include confidential product, credential, or account information. <br>


## Reference(s): <br>
- [Jungle Scout ASIN Keyword API Reference](artifact/references/api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-junglescout-keyword-by-asin) <br>
- [Publisher Profile](https://clawhub.ai/user/linkfox-ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown summaries and tables with saved JSON response files and optional inline JSON output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires LinkFox API credentials; accepts marketplace, ASIN list, count, sorting, variant, and keyword filter parameters.] <br>

## Skill Version(s): <br>
1.0.5 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
