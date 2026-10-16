## Description:

Helps parents access SchoolPass student and dismissal information and request confirmed arrival or dismissal changes through their own account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents use this skill to check their linked students, school information, pickup arrangements and arrival or dismissal schedules, and to request confirmed dismissal changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SchoolPass credentials and sensitive parent-account records may be exposed if configuration or responses are shared.

Mitigation: Only install if comfortable providing credentials to the MCP package; keep credentials and account records private, and never echo passwords or session tokens.

Risk: Submitting or canceling a dismissal change can alter a child's real school dismissal plan.

Mitigation: Check the preview and get explicit user approval before confirming; if submission status is uncertain, re-read the calendar rather than submitting again.

## Reference(s):

- [SchoolPass skill on ClawHub](https://clawhub.ai/chrischall/skills/schoolpass)
- [schoolpass-mcp package](https://www.npmjs.com/package/schoolpass-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance, Configuration, API calls]

**Output Format:** [Markdown guidance and structured tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read responses default to compact view; dismissal changes return previews and confirmation receipts.]

## Skill Version(s):

1.0.10 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
