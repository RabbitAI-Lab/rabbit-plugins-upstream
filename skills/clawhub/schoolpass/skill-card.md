## Description:

Helps parents check SchoolPass student arrival and dismissal information and manage pickup changes through their own account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents use this skill to review their children's school arrival and dismissal schedules, pickup arrangements, and school information, and to request confirmed dismissal changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Parent credentials and children's account details may be exposed if configuration or responses are shared.

Mitigation: Keep account configuration out of version control, restrict file permissions, avoid shared workspaces, and never disclose passwords or session tokens.

Risk: Submitting or canceling a dismissal change can alter a child's real pickup arrangements.

Mitigation: Review the preview with the parent and get explicit approval before confirming; if submission status is uncertain, check the calendar rather than resubmitting.

## Reference(s):

- [SchoolPass skill on ClawHub](https://clawhub.ai/chrischall/skills/schoolpass)
- [schoolpass-mcp package](https://www.npmjs.com/package/schoolpass-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Natural-language responses based on SchoolPass account records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include student schedules, pickup details, and previews or status of requested changes.]

## Skill Version(s):

1.0.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
