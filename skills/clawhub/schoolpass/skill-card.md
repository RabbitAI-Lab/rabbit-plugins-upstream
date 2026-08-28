## Description:

This skill helps an agent answer questions about a child's SchoolPass arrival and dismissal information through a parent account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to read parent-scoped SchoolPass data such as linked students, arrival and dismissal calendars, pickup changes, authorized drivers, dismissal locations, and school information. It can also prepare confirm-gated dismissal changes that require explicit user confirmation before submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive child, family, password, calendar, driver, and dismissal-change data.

Mitigation: Install only when the user accepts this data access, keep credentials out of conversation output, and restrict use to the intended parent account.

Risk: Dismissal-change tools can affect a child's real-world arrival or dismissal plan.

Mitigation: Show the preview and require explicit confirmation before submitting or canceling a dismissal change.

Risk: Local session persistence may be unacceptable in some environments.

Mitigation: Disable or relocate the session cache when local token persistence does not meet the deployment's security requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/schoolpass)
- [npm package](https://www.npmjs.com/package/schoolpass-mcp)
- [Source repository](https://github.com/chrischall/schoolpass-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON configuration examples, tool guidance, and concise user-facing text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce previews for dismissal changes and should avoid exposing passwords or session tokens.]

## Skill Version(s):

0.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
