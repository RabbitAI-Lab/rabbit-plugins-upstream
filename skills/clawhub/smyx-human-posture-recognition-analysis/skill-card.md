## Description:

Recognizes human postures such as standing, sitting, lying down, bending, raised hands, running, falling, and abnormal posture events from video inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Safety monitoring, elder-care, and operations teams use this skill to analyze local or URL-based videos for posture classifications, fall warnings, abnormal posture counts, structured results, and report links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media inputs and report queries may be sent to remote cloud or LAN services for posture analysis and history lookup.

Mitigation: Use the skill only where that data flow is acceptable, especially for videos involving private homes, patients, seniors, employees, or surveillance footage.

Risk: The skill can create or reuse local account identity and persisted tokens.

Mitigation: Run it in an environment with appropriate access controls, and clear local identity or token state when the workflow no longer requires it.

Risk: Fall warnings and posture reports are safety-monitoring aids and may be incomplete or incorrect.

Mitigation: Treat results as operational guidance, verify urgent events through independent channels, and do not rely on the report as the sole emergency response signal.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-human-posture-recognition-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands]

**Output Format:** [Markdown or JSON analysis reports with optional report links and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save report output to a user-specified local file path.]

## Skill Version(s):

1.0.12 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
