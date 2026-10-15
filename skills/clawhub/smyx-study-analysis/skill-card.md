## Description:

Analyzes children's study videos to identify learning behaviors and provide structured reports with suggestions for families.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and educators use this skill to review children's study videos for attention, posture, and learning habits, then receive reports and practical home-learning suggestions. It can also retrieve previous reports from the cloud service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Children's videos are sent to an external cloud service for analysis.

Mitigation: Confirm consent and that cloud processing is acceptable before submitting a child's video.

Risk: The skill automatically creates or reuses an account identity and stores account tokens in the workspace data directory.

Mitigation: Review the identity and token storage behavior before installation; limit workspace access and remove stored tokens when no longer needed.

Risk: Sensitive child-video reports are linked to cloud history with limited user control.

Mitigation: Use history features only when identity-linked cloud reports are acceptable; restrict access to report links and avoid sharing them unnecessarily.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-study-analysis)
- [Study analysis API documentation](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis reports or Markdown report lists; JSON results when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include behavior findings, suggestions, and links to cloud-hosted reports.]

## Skill Version(s):

1.0.18 (source: ClawHub release metadata; bundled SKILL.md states 1.0.20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
