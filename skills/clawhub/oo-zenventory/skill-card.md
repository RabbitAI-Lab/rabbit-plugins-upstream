## Description:

Zenventory helps an agent read, create, and update Zenventory inventory data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operations teams use this skill to let an agent search inventory records, retrieve item details, and prepare create or update actions for Zenventory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Create and update actions can change Zenventory inventory data.

Mitigation: Review the exact item, payload, and expected effect with the user before running write actions.

Risk: Connector access depends on the user's OOMOL account connection and available billing credits.

Mitigation: Resolve authentication, connection, scope, expiration, or billing errors through the documented OOMOL setup and account pages before retrying.

## Reference(s):

- [Zenventory skill page](https://clawhub.ai/oomol/skills/oo-zenventory)
- [Publisher profile](https://clawhub.ai/user/oomol)
- [Zenventory homepage](https://www.zenventory.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
