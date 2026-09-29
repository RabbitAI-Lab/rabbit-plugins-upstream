## Description:

Helps people find live events and experiences in New York City with dates, prices, images, and booking links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liangstl](https://clawhub.ai/user/liangstl)

### License/Terms of Use:

MIT-0

## Use Case:

People planning outings in New York City can use the skill to discover relevant live music, theater, comedy, art, sports, classes, and other experiences and receive event details and booking links.

### Deployment Geography for Use:

New York City, United States (current experience coverage)

## Known Risks and Mitigations:

Risk: Personal plans, preferences, location, or calendar-derived context may be sent to a third-party event service.

Mitigation: Explain what will be shared and obtain explicit confirmation before personalized searches or calendar use; share only the context needed.

Risk: The skill asks the assistant to retain a long-lived account code and use the person's search allowance.

Mitigation: Request the code only with informed consent, store it securely if retention is necessary, and confirm before using the account for searches or standing daily checks.

## Reference(s):

- [SyncSo on ClawHub](https://clawhub.ai/liangstl/skills/syncso)
- [SyncSo account connection](https://syncso.com/connect)
- [SyncSo MCP endpoint](https://rtdb.syncso.com/partner/mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown event recommendations with images, dates, prices, and booking links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Searches use the person's SyncSo account allowance; event coverage is currently focused on New York City.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
