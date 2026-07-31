## Description: <br>
Code-Right helps an agent create software copyright application materials by submitting a system name and recipient email to a remote document-generation service that produces Word documents, screenshots, a ZIP package, and an emailed download link. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ziyiyu](https://clawhub.ai/user/ziyiyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agent operators use this skill when they need to generate software copyright filing materials from a software system name, optional description, and recipient email. The skill creates an asynchronous remote task and returns task status while the service prepares the document package and sends the download link by email. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends the system name, optional system description, recipient email address, and any supplied access token to softcraft.cloud for remote processing and email delivery. <br>
Mitigation: Use the skill only when that transfer is acceptable, avoid confidential project details unless approved for the external service, and verify the recipient email address before creating the task. <br>
Risk: The generated materials are prepared by a remote workflow and may be unsuitable if the input system details are incomplete or inaccurate. <br>
Mitigation: Review the generated package before filing and provide a concise system description when the system name alone is not enough context. <br>


## Reference(s): <br>
- [Code-Right ClawHub Skill](https://clawhub.ai/ziyiyu/skills/code-right-skill) <br>
- [Code-Right Service Homepage](https://softcraft.cloud) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates a remote asynchronous task; generated files are delivered by email as a download link.] <br>

## Skill Version(s): <br>
0.2.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
