## Description:

Helps an agent read and manage OurFamilyWizard co-parenting messages, calendar events, expenses, and journal entries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People managing co-parenting arrangements use this skill to review OFW communications and schedules, track expenses, and prepare or make updates with appropriate confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OFW credentials and locally cached co-parenting data are sensitive.

Mitigation: Use a protected secret manager or environment injection; keep credentials out of project files, repositories, and screenshots, and restrict local cache access.

Risk: Reading an unread message or checking notifications can change visible account status.

Mitigation: Explain these side effects first; avoid opening unread messages or checking notifications without the user's intent.

Risk: Sending, deleting, or changing shared records can be consequential or irreversible.

Mitigation: Require an explicit request and confirmation for sends, deletes, expenses, events, and journal writes; verify uncertain results before retrying.

Risk: Cached messages and drafts may be stale or incomplete.

Mitigation: Check live status, freshness, completeness, and pagination before asserting current state or totals.

## Reference(s):

- [ofw ClawHub release](https://clawhub.ai/chrischall/skills/ofw)
- [ofw-mcp npm package (linked in skill)](https://www.npmjs.com/package/ofw-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Tool calls]

**Output Format:** [Human-readable summaries and structured OFW tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cached results may be stale or incomplete; check freshness and pagination before reporting current state.]

## Skill Version(s):

2.20.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
