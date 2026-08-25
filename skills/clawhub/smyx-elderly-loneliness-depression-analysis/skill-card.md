## Description:

Analyzes fixed-camera home videos of elderly people living alone to report behavior-based loneliness or depression-tendency risk signals such as dazing, sighing, and self-talking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External family members, community care workers, elder-care operators, and developers use this skill to analyze authorized home, nursing-home, or daycare video and produce behavior statistics, an emotional-risk level, friendly reminders, and report links. It is intended to surface risk signals for care follow-up, not to diagnose depression or replace clinical screening.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive home video and identity-linked reports are sent to remote services.

Mitigation: Use only with explicit informed consent and authorized footage; confirm the backend endpoint, retention policy, report access controls, and deletion process before processing real home footage.

Risk: The skill silently creates and persists user identity tokens.

Mitigation: Review local storage behavior before deployment and document how operators can inspect, rotate, and delete stored database entries or tokens.

Risk: Behavior-based risk output could be mistaken for a medical diagnosis.

Mitigation: Present outputs as non-diagnostic care prompts and require professional clinical evaluation for diagnosis, treatment decisions, or urgent self-harm concerns.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-elderly-loneliness-depression-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Elderly loneliness/depression analysis API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports and JSON-style structured analysis returned through API-backed scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include behavior metrics, baseline comparison, risk level, alert text, recommended actions, and report links.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter says 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
