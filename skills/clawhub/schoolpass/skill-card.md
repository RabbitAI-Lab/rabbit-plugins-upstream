## Description:

This skill helps a parent use a SchoolPass parent account to check student arrival and dismissal details, pickup drivers, dismissal locations, pickup changes, and confirmed dismissal-change actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users with SchoolPass parent accounts use this skill to let an agent read family, student, driver, calendar, school, and dismissal-location information. It can also prepare and submit or cancel real dismissal changes only after an explicit confirmation step.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles SchoolPass parent credentials and sensitive family, student, driver, calendar, and dismissal information.

Mitigation: Install only when that access is acceptable, avoid exposing passwords or session tokens in conversation, and consider pinning the npm package version in the MCP configuration.

Risk: Confirmed dismissal-change tools can make real changes to a child's dismissal plan.

Mitigation: Require the dry-run preview and explicit user confirmation before submitting or canceling a dismissal change.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chrischall/skills/schoolpass)
- [npm Package](https://www.npmjs.com/package/schoolpass-mcp)
- [Source Repository](https://github.com/chrischall/schoolpass-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, shell commands, guidance]

**Output Format:** [Markdown with inline JSON configuration and tool-result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dry-run previews for dismissal changes before confirmed submission.]

## Skill Version(s):

0.2.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
