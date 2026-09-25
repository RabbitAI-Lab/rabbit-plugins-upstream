## Description:

Analyzes fixed-camera images or video to estimate adolescent screen-looking posture, summarize screen-time behavior, and produce gentle family-facing reminders without making medical diagnoses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, guardians, and education or smart-home operators use this skill to review camera footage for head-down screen posture, daily screen-time patterns, and family-friendly intervention reminders. The skill is intended for behavior monitoring and reporting, not clinical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Minor-related home or school camera footage may be sent to a cloud service for analysis.

Mitigation: Use only with guardian and adolescent consent, limit recordings to appropriate spaces, and confirm the publisher's retention, deletion, and access-control practices before deployment.

Risk: The skill can create or reuse a local identity with stored tokens.

Mitigation: Run it in a controlled environment, review where credentials are stored, and establish an account revocation or cleanup process before operational use.

Risk: Screen-time labels can be mistaken for clinical conclusions or punitive judgments.

Mitigation: Present outputs as posture and duration observations only, avoid medical diagnosis language, and use the skill's gentle reminder posture for family-facing guidance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-teen-screen-addiction-detection-analysis)
- [API interface documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown text with JSON-style structured report content and optional report link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save report output to a file when requested; analysis and history lookup use a documented cloud service.]

## Skill Version(s):

1.0.5 (source: server release metadata; artifact frontmatter says 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
