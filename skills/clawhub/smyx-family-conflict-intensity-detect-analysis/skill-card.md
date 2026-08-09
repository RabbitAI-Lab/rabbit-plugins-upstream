## Description:

Analyzes living-room audio and video from a fixed camera with microphone to estimate family or couple conflict intensity and produce structured low, medium, or high reports with gentle reminder guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, family counselors, mediation centers, and smart-home integrators use this skill to analyze consented living-room audio/video for acoustic and visual indicators of conflict intensity. The skill produces structured reports and non-diagnostic reminder guidance for low, medium, or high conflict intensity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive household audio/video or video URLs may be sent to cloud analysis services.

Mitigation: Require informed consent from affected household members before use, avoid bystander or minor recordings unless clearly authorized, and store exported reports carefully.

Risk: Cloud report history may be queried automatically and a local identity/token database may be created.

Mitigation: Review this behavior before installation and deploy only where the identity, token, and cloud history handling are acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-family-conflict-intensity-detect-analysis)
- [API documentation](references/api_doc.md)
- [Skill usage demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON structured analysis reports with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links, acoustic metrics, visual metrics, conflict intensity levels, reminder text, and history query results.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
