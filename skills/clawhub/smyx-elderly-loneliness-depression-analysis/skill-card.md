## Description:

Analyzes home video of older adults living alone for behaviors such as prolonged inactivity, sighing, and self-talking, and returns emotional-risk reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Families and community care workers use the skill to review behavior patterns in an older adult's home video and identify when supportive follow-up may be appropriate. Its reports are not a clinical depression diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive home video, optional audio, and emotional-risk reports are sent to a cloud service.

Mitigation: Obtain the monitored elder's explicit consent and assess whether cloud processing is appropriate before use.

Risk: Automatic identity reuse and cached account tokens can expose reports across shared workspaces.

Mitigation: Use an isolated workspace per person and review identity isolation and token storage before installation.

Risk: Behavior signals can be misleading and are not a clinical depression assessment.

Mitigation: Review reports in context and do not use them in place of professional assessment.

## Reference(s):

- [Skill release on ClawHub](https://clawhub.ai/smyx-sunjinhui/skills/smyx-elderly-loneliness-depression-analysis)
- [Analysis API reference](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis report or historical report list with links; JSON detail available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include behavior observations, emotional-risk levels, suggestions, and report links]

## Skill Version(s):

1.0.10 (source: ClawHub release; bundled SKILL.md lists 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
