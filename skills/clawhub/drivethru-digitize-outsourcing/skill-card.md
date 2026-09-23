## Description:

Outsource embroidery digitizing for BaconCo by coordinating Odoo digitize.demand records, vendor submissions, returned stitch files, worksheet parsing, and Odoo workflow updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zmtucker](https://clawhub.ai/user/zmtucker)

### License/Terms of Use:

MIT-0

## Use Case:

Operations employees use this skill to send ready, non-custom embroidery digitizing demands from Odoo to an outside digitizer and to receive completed DST files, production worksheet data, and thread color updates back into the workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can mutate Odoo workflow data and submit jobs to an external digitizing vendor.

Mitigation: Use a narrow tool allowlist and require explicit confirmation before live submissions or Odoo writes.

Risk: The skill needs an Odoo MCP bearer token.

Mitigation: Store ODOO_MCP_TOKEN as a secret, avoid sharing it in chat, and scope the token to the minimum required permissions.

Risk: Returned customer and vendor job files may persist on the agent host.

Mitigation: Define retention, access, and cleanup rules for the local job archive before production use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zmtucker/skills/drivethru-digitize-outsourcing)
- [Publisher profile](https://clawhub.ai/user/zmtucker)
- [Routine details](references/routine.md)
- [Odoo](https://www.odoo.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Files, Configuration]

**Output Format:** [Markdown guidance with JSON command payloads and generated local files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ODOO_MCP_URL and ODOO_MCP_TOKEN; may create a persistent per-job vendor file archive.]

## Skill Version(s):

0.5.0 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
