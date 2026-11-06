## Description:

This skill should be used when the user asks about OurFamilyWizard (OFW) co-parenting data. Triggers on phrases like "check OFW", "OurFamilyWizard inbox", "OFW messages", "OFW calendar", "OFW expenses", "what did my co-parent say", "log an expense in OFW", "OFW journal", or any request involving co-parenting messages, calendar events, shared expenses, or journal entries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People managing co-parenting arrangements use this skill to retrieve and organize OurFamilyWizard messages, calendar events, expenses, and journal entries, and to prepare or make changes with appropriate confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OFW requests may be ambiguous, causing access to the wrong service or account context.

Mitigation: Confirm that ambiguous requests refer to OurFamilyWizard before acting.

Risk: Credentials and cached co-parenting records contain sensitive family information.

Mitigation: Protect credential files and cached family data.

Risk: Reading an unread message can change its viewed status, and consequential writes can alter a legal co-parenting record.

Mitigation: Enable OFW_CONFIRM_MARK_READ when unread-message approval is needed, and review consequential changes before confirming them.

Risk: The release review did not verify the external server package payload or all runtime safeguards.

Mitigation: Pin and review the external server version.

## Reference(s):

- [OFW skill release on ClawHub](https://clawhub.ai/chrischall/skills/ofw)
- [ofw-mcp package on npm](https://www.npmjs.com/package/ofw-mcp)

## Skill Output:

**Output Type(s):** [Text, JSON, Files]

**Output Format:** [Structured tool results, natural-language responses, and inline or downloadable attachments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Message and expense results may be paginated; message and draft data can come from a local cache.]

## Skill Version(s):

2.26.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
