## Description: <br>
Analyzes seedling tray images or videos with AI object detection to count emerged seedlings and estimate germination rate for incubators, greenhouse trays, home pots, and seed-company tests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to analyze seed tray images or videos, estimate germinated seed counts and rates, and retrieve cloud-hosted history reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Seed tray media may be uploaded to or processed by a cloud-backed service. <br>
Mitigation: Use the skill only with media approved for external cloud processing and avoid private or sensitive media unless that processing is acceptable. <br>
Risk: The skill can use or create an internal identity and store authentication tokens locally. <br>
Mitigation: Review identity and token storage behavior before installation, and avoid shared workspaces unless local credential persistence is acceptable. <br>
Risk: The skill can fetch account-associated history reports. <br>
Mitigation: Confirm the account context and report-retention expectations before using history-report features. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-seed-germination-rate-prediction-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](artifact/references/api_doc.md) <br>
- [Analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands] <br>
**Output Format:** [Markdown text with JSON payloads and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can save analysis output to a file when an output path is provided.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata; SKILL.md frontmatter says 1.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
