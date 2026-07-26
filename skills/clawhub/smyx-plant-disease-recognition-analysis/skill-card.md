## Description: <br>
Identifies plant diseases from image or video input and returns structured diagnostic reports with disease type, likely cause, severity, prevention suggestions, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, growers, gardeners, and plant-care developers use this skill to analyze plant photos or videos for disease diagnosis and prevention guidance. It can also retrieve cloud-hosted historical analysis reports associated with the resolved user identity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends plant images or videos to configured Life Emergence cloud APIs for analysis. <br>
Mitigation: Use only when users are comfortable sharing those media inputs with the configured cloud service, and confirm the publisher's retention and deletion practices before deployment. <br>
Risk: The skill silently creates or reuses a cloud-linked identity and may keep local SQLite records that include authentication tokens. <br>
Mitigation: Review before installing, require clear disclosure or opt-in for account creation and token storage, and document how local and cloud report data can be deleted. <br>


## Reference(s): <br>
- [API documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-disease-recognition-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON diagnostic reports with optional shell command examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include disease labels, likely causes, severity, prevention suggestions, report links, and historical report listings.] <br>

## Skill Version(s): <br>
1.0.6 (source: release evidence; artifact frontmatter reports 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
