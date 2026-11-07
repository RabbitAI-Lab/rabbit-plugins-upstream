## Description:

Access OurFamilyWizard (OFW) — messages, calendar, expenses, journal — from a shell with the fpx CLI (@fetchproxy/cli) instead of running the ofw-mcp server: capture the signed-in web app's Bearer token once via the browser bridge, then curl the REST API directly. Use when you want OFW data without the MCP, in a script, or on a machine where the MCP isn't installed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technically confident OFW users can use this skill to read messages, calendar, expenses, journal entries, and profile data from shell scripts or machines without the ofw-mcp server. It also provides examples for writing to the shared OFW record, so users can review the request and target before making changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Commands can send or delete messages and change calendar or expense data in the shared OFW record, where changes are visible to the co-parent.

Mitigation: Review each write request and its target before running it; after sending or saving a message, fetch the created record and verify its contents as the skill instructs.

Risk: The recorded security scan was partial, so some local references were not checked.

Mitigation: Review the referenced request examples and any linked material before relying on commands from them.

## Reference(s):

- [OFW request examples](references/requests.md)
- [OurFamilyWizard](https://ofw.ourfamilywizard.com)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [Fetchproxy extension information](https://github.com/chrischall/fetchproxy#extension)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/ofw-fpx)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Configuration instructions]

**Output Format:** [Markdown with inline shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands and request examples for reading and writing OFW data.]

## Skill Version(s):

2.27.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
