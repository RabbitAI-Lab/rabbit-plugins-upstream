## Description:

Guides agents in accessing OurFamilyWizard messages, calendar, expenses, and journal using a signed-in browser session and shell commands instead of the MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

OurFamilyWizard users and developers use this skill to guide shell-based access to their messages, calendar, expenses, and journal when the MCP server is unavailable or unsuitable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Extracting a live browser session token can expose access to sensitive family records.

Mitigation: Keep the token out of logs and shell history; use a safer gated workflow when possible.

Risk: Shell commands can create, update, upload, or delete shared court-relevant records without enforced confirmation.

Mitigation: Confirm each target ID and payload, and require an explicit confirmation before every write or delete.

Risk: A message write may appear successful without saving the intended content.

Mitigation: Re-fetch the message after posting and verify its subject and body.

## Reference(s):

- [OurFamilyWizard request examples](references/requests.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may read or change shared OurFamilyWizard records.]

## Skill Version(s):

2.20.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
