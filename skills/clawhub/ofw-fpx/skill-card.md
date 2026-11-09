## Description:

Access OurFamilyWizard (OFW) messages, calendar, expenses, and journal from a shell with the fpx CLI and curl by capturing a signed-in web app Bearer token through the browser bridge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OurFamilyWizard users can use the skill to read account data and perform account actions from shell scripts or machines where the ofw-mcp server is not installed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Examples can send messages and change or delete OFW account records visible to a co-parent; file uploads may also be shared depending on their settings.

Mitigation: Review each write or delete request, its payload, sharing settings, and target before running it; use read-only requests when no account change is intended.

Risk: Scanner coverage is incomplete because some local references were missing, so not every referenced component was inspected.

Mitigation: Review the referenced materials and extension components before use; do not treat the benign verdict as proof that all components were scanned.

## Reference(s):

- [OurFamilyWizard request examples](references/requests.md)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [Fetchproxy extension reference](https://github.com/chrischall/fetchproxy#extension)
- [OurFamilyWizard service](https://ofw.ourfamilywizard.com)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and curl requests]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Endpoint paths, request examples, and jq projections for OFW account operations]

## Skill Version(s):

2.28.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
