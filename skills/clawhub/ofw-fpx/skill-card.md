## Description:

Guides agents in accessing OurFamilyWizard messages, calendars, expenses, and journal entries through a signed-in browser session and shell commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

OurFamilyWizard account holders and their agents use this skill to retrieve family-account information and manage messages, events, expenses, and journal entries from a shell without the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses the active account token to access private family information.

Mitigation: Install only if you trust the agent with your signed-in OurFamilyWizard session and account token.

Risk: Write, delete, upload, and message commands can change court-visible records without an enforced confirmation step.

Mitigation: Review exact record IDs, recipients, payloads, and files before running a mutation; verify sent messages afterward.

## Reference(s):

- [OurFamilyWizard request examples](artifact/references/requests.md)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/ofw-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands operate on the user's active OurFamilyWizard account.]

## Skill Version(s):

2.19.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
