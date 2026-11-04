## Description:

Access OurFamilyWizard messages, calendar, expenses, and journal from the shell by capturing a signed-in browser token and making requests with curl.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

OurFamilyWizard users and developers use the skill to read and manage family messages, calendar events, expenses, and journal entries from shell scripts when they want access without an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The commands can send messages, alter shared family records, or delete data without a per-action approval step.

Mitigation: Require explicit approval of recipients, content, affected records, and visibility before each send, deletion, shared upload, or expense change. Prefer read-only or draft-only access when writes are unnecessary.

Risk: The captured bearer token and the browser extension or CLI used to obtain it can expose account access.

Mitigation: Protect the captured token and review the CLI and extension before pairing.

## Reference(s):

- [OurFamilyWizard request examples](references/requests.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [Fetchproxy extension details](https://github.com/chrischall/fetchproxy#extension)
- [ClawHub release page](https://clawhub.ai/chrischall/skills/ofw-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON/API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples can read account data or make consequential changes to shared family records.]

## Skill Version(s):

2.25.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
