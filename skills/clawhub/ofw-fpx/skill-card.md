## Description:

Guides agents in accessing OurFamilyWizard messages, calendars, expenses, and journals through shell commands using a signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

OurFamilyWizard users and developers use this skill to retrieve account records or prepare account actions from a shell without running an MCP server. Commands that change records require careful human review before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shell access to a signed-in account can expose sensitive family records and credentials.

Mitigation: Use only in a trusted environment and limit access to the signed-in session and its credentials.

Risk: Writes, deletes, uploads, expenses, and journal entries affect live, potentially court-relevant records without a built-in confirmation step.

Mitigation: Prefer read-only use; manually review the action, recipients, visibility, record IDs, and payload before executing any change, or add a confirmation wrapper.

Risk: Message posts may appear successful without the intended content being saved.

Mitigation: Retrieve the message after posting and verify its subject and body before treating it as delivered.

## Reference(s):

- [ofw-fpx on ClawHub](https://clawhub.ai/chrischall/skills/ofw-fpx)
- [OurFamilyWizard request examples](references/requests.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell examples and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands access live OurFamilyWizard records; reading some records may update their viewed status.]

## Skill Version(s):

2.20.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
