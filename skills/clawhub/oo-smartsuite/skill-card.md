## Description:

SmartSuite lets an agent read, create, update, and delete data in a connected SmartSuite workspace through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill when they want an agent to work with SmartSuite Solutions, Tables, and Records from a connected SmartSuite workspace. It supports both read workflows and user-approved record creation, updates, and deletion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can create or modify SmartSuite records in the connected workspace.

Mitigation: Inspect the live action schema, show the exact payload and expected effect, and get user confirmation before running create or update actions.

Risk: The delete action can remove a SmartSuite record.

Mitigation: Confirm the target record and obtain explicit approval before running the destructive delete action.

Risk: Connector authentication or workspace connection issues can block SmartSuite actions.

Mitigation: Run first-time setup or reconnection steps only after an auth, scope, credential, app, or billing error indicates they are needed.

## Reference(s):

- [SmartSuite skill release page](https://clawhub.ai/oomol/skills/oo-smartsuite)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [SmartSuite homepage](https://www.smartsuite.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill inspects live connector schemas before constructing SmartSuite action payloads.]

## Skill Version(s):

1.0.1 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
