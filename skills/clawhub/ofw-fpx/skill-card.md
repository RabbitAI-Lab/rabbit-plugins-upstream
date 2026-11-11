## Description:

Access OurFamilyWizard messages, calendar, expenses, and journal from shell scripts using fpx to capture a signed-in browser token and curl for API requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OurFamilyWizard users use this skill to read and update messages, events, expenses, and journal entries from shell scripts when they need direct API access without the OFW MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write commands can permanently change shared family-court records, and the security scan has partial coverage.

Mitigation: Review the missing references and confirm you need the described write capabilities before use; the benign verdict does not establish that the skill is risk-free.

## Reference(s):

- [OurFamilyWizard request examples](references/requests.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [Fetchproxy extension information](https://github.com/chrischall/fetchproxy#extension)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/ofw-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples include commands that read and write OurFamilyWizard data.]

## Skill Version(s):

2.28.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
