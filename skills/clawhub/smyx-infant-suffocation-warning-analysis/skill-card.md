## Description:

Helps caregivers analyze infant sleep videos for prone positioning and face-covering risks through a cloud service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers and developers use the skill to submit infant sleep videos or video URLs for risk analysis and review structured findings and historical reports. It is an aid to supervision, not a replacement for adult care or a verified real-time alarm.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive infant videos, video URLs, and identifiers are sent to external Life Emergence services.

Mitigation: Review service privacy practices and obtain appropriate consent before sharing media; submit only necessary content.

Risk: The skill creates or reuses a local default identity and stores service tokens in a workspace SQLite database.

Mitigation: Review the local identity and token storage before installation and restrict access to the workspace database.

Risk: Cloud polling and report retrieval are not a verified real-time local alarm and may miss urgent events.

Mitigation: Do not use the skill as the sole safety monitor; maintain direct adult supervision and promptly check the infant if risk is suspected.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-infant-suffocation-warning-analysis)
- [Shared API reference](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis reports, Markdown tables, or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include risk indicators, recommendations, report links, and historical report listings.]

## Skill Version(s):

1.0.16 (source: ClawHub release; bundled SKILL.md states 1.0.20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
