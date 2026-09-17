## Description:

Use this skill to read, create, update, and delete Rebrandly data through the OOMOL-connected Rebrandly connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Rebrandly branded short links through an OOMOL-connected Rebrandly account, including account lookup, domain and link listing, link creation, link updates, and soft deletion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup instructions include remote installer commands that can execute code on the user's machine.

Mitigation: Install the oo CLI through a verified, versioned, checksum- or signature-checked method instead of allowing an agent to run remote installer commands.

Risk: Create, update, and delete actions can change or remove Rebrandly data.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [Rebrandly homepage](https://www.rebrandly.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Rebrandly skill listing](https://clawhub.ai/oomol/skills/oo-rebrandly)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
