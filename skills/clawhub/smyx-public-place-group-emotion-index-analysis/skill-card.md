## Description:

Analyzes public-place camera footage to estimate aggregated facial-expression distributions and a 0–100 group-emotion index, with area-level reports and operational suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Venue operators and developers use this skill to review aggregate emotion trends in mall, exhibition, and other public-space footage and receive area-level service suggestions or safety alerts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public-camera footage is sent to an external service and may expose sensitive media.

Mitigation: Confirm consent and prominent signage, review the external service and its retention practices, and submit only footage authorized for analysis.

Risk: The skill creates or reuses a persistent service identity and stores associated tokens in a workspace database.

Mitigation: Review identity creation before installation, restrict access to stored tokens, and define credential retention and removal procedures.

## Reference(s):

- [Public-place group emotion analysis API documentation](references/api_doc.md)
- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-public-place-group-emotion-index-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Text or JSON analysis report; Markdown links for historical reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Aggregate emotion scores, area-level findings, suggested actions, and report links when available]

## Skill Version(s):

1.0.14 (source: server-resolved ClawHub release; artifact frontmatter lists 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
