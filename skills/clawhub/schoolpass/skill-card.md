## Description:

schoolpass connects an agent to a SchoolPass parent account to read student, dismissal, pickup, driver, dismissal-location, and school information, with confirmation-gated dismissal changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to let an agent answer questions and perform confirmed actions for a SchoolPass parent account, including checking students, calendars, pickup changes, authorized drivers, dismissal locations, and school information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SchoolPass credentials are stored in MCP configuration.

Mitigation: Use a private, uncommitted MCP config location and restrict file permissions where possible.

Risk: Confirmed write tools can change a child's real dismissal plan.

Mitigation: Review the preview carefully and get explicit user approval before approving any confirm:true action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/schoolpass)
- [npm package: schoolpass-mcp](https://www.npmjs.com/package/schoolpass-mcp)
- [Source link from artifact](https://github.com/chrischall/schoolpass-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance, API calls]

**Output Format:** [Markdown and structured tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read tools default to compact responses; dismissal-change tools require explicit confirmation before changing SchoolPass data.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
