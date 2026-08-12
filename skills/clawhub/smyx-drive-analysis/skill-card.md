## Description:

Analyzes videos of vehicle drivers to identify unsafe driving behaviors and generates professional analysis reports to help enhance road safety awareness.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze driver videos or video URLs for unsafe driving behaviors such as fatigue, distraction, seatbelt non-use, posture issues, and risky behavior, then receive a structured safety report and report link.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Driver videos or video URLs, report metadata, and generated identity information may be sent to the publisher's cloud service.

Mitigation: Use only footage you are authorized to share, avoid sensitive footage until privacy and retention terms are confirmed, and obtain the publisher's permissions, retention, and deletion details before production use.

Risk: The skill can silently create or reuse an identity and stores account tokens locally in the workspace.

Mitigation: Run it in a controlled workspace, restrict workspace access, remove local token and data files after use when appropriate, and do not share the workspace with unauthorized users.

Risk: Cloud report history is queried with limited direct user control.

Mitigation: Confirm the active user identity before querying history and review publisher account controls for report access, deletion, and account closure.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-drive-analysis)
- [API interface documentation](artifact/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Files]

**Output Format:** [Markdown text with structured JSON content and optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces driver-safety analysis summaries, history listings, and report export links; local video inputs are limited to mp4, avi, and mov files up to 10 MB.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter lists 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
