## Description:

Access OurFamilyWizard messages, calendar, expenses, and journal from shell scripts using fpx to capture a signed-in session token and curl to call its REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People who use OurFamilyWizard and developers who need command-line access can use this skill to read and manage messages, calendar events, expenses, and journal entries without an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, change, and delete shared OurFamilyWizard records, and these actions may be permanent and visible to the co-parent.

Mitigation: Avoid installation unless these capabilities are clearly disclosed and needed; inspect the target, recipients, and payload before each write or deletion.

Risk: The workflow reads a signed-in account's bearer token from browser local storage and uses it in shell requests.

Mitigation: Keep the token out of shell history, logs, and shared terminals, and use the workflow only on a trusted machine.

## Reference(s):

- [OFW request examples](references/requests.md)
- [OurFamilyWizard](https://ofw.ourfamilywizard.com)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [fetchproxy extension documentation](https://github.com/chrischall/fetchproxy#extension)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/ofw-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API calls, Guidance]

**Output Format:** [Markdown with inline bash, curl, and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples include read and write operations against a signed-in OurFamilyWizard account.]

## Skill Version(s):

2.29.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
