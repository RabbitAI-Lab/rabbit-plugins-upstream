## Description:

Analyzes child facial video from a classroom or home desk to estimate drowsiness using eye closure and head movement, and produces a fatigue score and rest reminders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers and parents can use the skill to review visual fatigue estimates from a child's study video, receive rest prompts, and request past reports. Results support observation rather than medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Children's facial video is processed through a cloud service.

Mitigation: Review the provider and retention terms and obtain appropriate consent for minors before use.

Risk: Persistent identities and tokens may be silently created or reused, potentially mixing reports in shared workspaces.

Mitigation: Avoid shared workspaces until identity fallback and token storage are fixed; require explicit user-controlled account linkage and history retrieval.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-child-drowsiness-fatigue-detection-analysis)
- [Fatigue detection API reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured analysis results and Markdown history tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fatigue score and level, event summaries, rest prompts, and optional report links or JSON output]

## Skill Version(s):

1.0.12 (source: ClawHub release metadata; bundled SKILL.md states 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
