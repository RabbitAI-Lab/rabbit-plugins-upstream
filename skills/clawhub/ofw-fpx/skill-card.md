## Description:

Access OurFamilyWizard messages, calendar, expenses, and journal data from a shell by capturing a signed-in browser Bearer token with fpx and using curl against the OFW API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical OurFamilyWizard users use this skill to inspect or update OFW records from shell scripts when they have an active signed-in browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill guides an agent or shell session to use a signed-in OFW session token for API calls that can read and change live OFW records.

Mitigation: Install and run it only in sessions where OFW data access is intended, and keep the captured Bearer token confined to the current trusted shell.

Risk: Send, upload, update, and delete examples can create permanent, visible changes to shared family-court records.

Mitigation: Review each write command, recipient, payload, and target ID before execution, and re-GET message writes to confirm the intended content landed.

## Reference(s):

- [OurFamilyWizard request examples](references/requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/ofw-fpx)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a signed-in OFW browser session, fpx CLI, jq, and curl; commands may read or mutate live OFW records.]

## Skill Version(s):

2.14.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
