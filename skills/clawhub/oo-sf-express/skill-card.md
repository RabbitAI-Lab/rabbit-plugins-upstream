## Description:

SF Express (open.sf-express.com). Use this skill for ANY SF Express request - reading, creating, updating, and deleting data through the OOMOL-connected SF Express connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect SF Express action schemas and operate shipment, freight, cold-chain, station, store, waybill, route, print, fee, and service-point workflows through their connected OOMOL account. It supports read actions as well as confirmed write and destructive logistics operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The required CLI setup path includes remote script installers.

Mitigation: Review setup before installing, prefer a verified or pinned oo CLI release or official guide, and do not let an agent run curl|bash or irm|iex automatically.

Risk: Write and destructive SF Express actions can create, update, cancel, intercept, or otherwise change real logistics records.

Mitigation: Allow only the specific SF Express action requested, inspect the live schema first, and require explicit user confirmation before write or destructive operations.

## Reference(s):

- [SF Express homepage](https://open.sf-express.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL SF Express connection](https://console.oomol.com/app-connections?provider=sf_express)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-sf-express)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are expected as JSON from the oo CLI; live action schemas should be inspected before constructing payloads.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
