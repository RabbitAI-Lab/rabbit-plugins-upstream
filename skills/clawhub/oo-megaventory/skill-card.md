## Description:

Megaventory (megaventory.com). Use this skill for Megaventory requests that read, create, or update data through the OOMOL-connected oo CLI instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Megaventory action schemas, list products, orders, document types, locations, suppliers, and clients, and create or update products and orders through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands for the oo CLI, which can execute code from OOMOL's distribution endpoint.

Mitigation: Inspect or verify the installer and install only when the OOMOL CLI distribution path is trusted.

Risk: The skill can create or update Megaventory products, purchase orders, and sales orders.

Mitigation: Confirm the exact write payload and expected account changes with the user before running write actions.

## Reference(s):

- [Megaventory homepage](https://www.megaventory.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-megaventory)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, API Calls]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo CLI schema-inspection commands and JSON action payloads; write actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
