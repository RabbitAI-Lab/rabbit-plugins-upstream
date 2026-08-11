## Description:

Assists government and enterprise administrative users with Chinese-language official documents, meeting minutes, periodic reports, meeting preparation, cross-department communication, compliance reminders, and workflow follow-up without making professional decisions or fabricating unsupported details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chesaram](https://clawhub.ai/user/chesaram)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and administrative staff in government agencies and enterprises use this skill to draft, organize, track, and remind on routine administrative documents and processes. It is intended for structured drafting support and coordination, not for legal, financial, personnel, procurement, or other professional determinations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated official-looking administrative documents may contain unsupported dates, locations, deadlines, document numbers, attendees, or example-derived details.

Mitigation: Review those fields before use and replace unsupported or missing information with 待补 or 待定.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chesaram/skills/gov-entity-admin-1-0-0)
- [ClawHub Publisher Profile](https://clawhub.ai/user/chesaram)
- [README](artifact/README.md)
- [Skill Source](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Chinese-language Markdown and structured XML-like document blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses 待补, 待签, or 待定 for missing fields and HEARTBEAT_OK when no actionable schedule or to-do data is available.]

## Skill Version(s):

1.0.0 (source: evidence release, SKILL.md frontmatter, manifest.yaml, _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
