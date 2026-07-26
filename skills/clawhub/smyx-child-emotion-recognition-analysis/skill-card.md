## Description: <br>
Identifies negative emotions such as crying, anger, fear, and distress in children's surveillance footage and produces alerts, soothing reminders, and caregiver-facing reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External caregivers, daycare operators, and developers use this skill to analyze child-focused images or video for negative emotion signals and to retrieve cloud-hosted historical analysis reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Children's images, videos, remote media URLs, report history requests, and account-linked identifiers may be sent to configured Life Emergence cloud services. <br>
Mitigation: Install and operate only after confirming consent, legal basis, retention and deletion terms, and who can access historical reports. <br>
Risk: The skill silently creates or reuses identity for report association. <br>
Mitigation: Review identity handling before deployment and restrict report-history access to authorized operators. <br>
Risk: The authoritative security verdict is suspicious because consent and retention controls are unclear. <br>
Mitigation: Treat deployment as requiring security and privacy review before use with real children's media. <br>


## Reference(s): <br>
- [API interface documentation](artifact/references/api_doc.md) <br>
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-child-emotion-recognition-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-backed text output from Python CLI commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include report links and optional local output files when the CLI --output parameter is used.] <br>

## Skill Version(s): <br>
1.0.15 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
