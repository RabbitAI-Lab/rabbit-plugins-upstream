## Description: <br>
Identifies fruit ripeness stages (green / turning / ripe / over-ripe) based on color, size and gloss features to output a standardized ripeness grade. | 通过颜色、大小、光泽度识别果实成熟度（青/转色/成熟/过熟），输出成熟度等级。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, growers, agronomists, and developers use this skill to submit crop fruit images, videos, or URLs for ripeness grading and harvest-window guidance. It can also return identity-linked historical analysis reports from the vendor service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Crop images or videos and report queries are sent to the vendor API for analysis and history lookup. <br>
Mitigation: Use only media that is appropriate to share with the vendor service, and review data retention and account-management expectations before deployment. <br>
Risk: Analysis history is tied to an internally managed identity, and service tokens or user records may be stored in the workspace data directory. <br>
Mitigation: Run the skill in an isolated workspace, avoid shared machines for sensitive media, and clear local identity or token storage according to operational policy. <br>
Risk: Ripeness grades and harvest-window guidance are advisory and may be incomplete for commodity grading decisions. <br>
Mitigation: Require human review and applicable enterprise grading standards before acting on harvest or commercial quality decisions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-crop-fruit-ripeness-grading-analysis) <br>
- [Crop Fruit Ripeness Grading API Reference](artifact/references/api_doc.md) <br>
- [Shared Analysis API Reference](artifact/skills/smyx_analysis/references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, API Calls, Markdown, JSON, Files, Shell commands, Guidance] <br>
**Output Format:** [Markdown or JSON analysis reports, with optional saved output files and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Processes image, video, or URL inputs and may query history from the vendor API.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter lists 1.0.4) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
