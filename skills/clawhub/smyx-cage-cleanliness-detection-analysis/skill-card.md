## Description: <br>
Analyzes cage images or videos to estimate feces and urine coverage, score cleanliness, trigger threshold-based cleaning alerts, and return reports for pet boarding, shop, hospital, or breeding settings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External pet-care facility operators and developers use this skill to analyze cage floor media, estimate waste coverage, and retrieve cloud-backed reports for hygiene monitoring. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cage images or videos and report activity are sent to the publisher's cloud service. <br>
Mitigation: Use the skill only for footage that is approved for cloud processing by the publisher, and review retention expectations before deployment. <br>
Risk: The skill may create or reuse a local identity and persist account tokens in a workspace SQLite database. <br>
Mitigation: Run it in an isolated workspace and review or remove stored local identity and token data when access is no longer needed. <br>
Risk: Cloud report history can be retrieved automatically when report-list intents are triggered. <br>
Mitigation: Limit use to operators authorized to view the associated reports and avoid using shared workspaces for sensitive facility footage. <br>


## Reference(s): <br>
- [API 接口文档](references/api_doc.md) <br>
- [API接口文档](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-cage-cleanliness-detection-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, files] <br>
**Output Format:** [Markdown or JSON structured analysis report, with optional saved output file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include cleanliness scores, threshold alerts, report links, and history tables.] <br>

## Skill Version(s): <br>
1.0.4 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
