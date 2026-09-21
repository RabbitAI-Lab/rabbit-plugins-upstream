## Description:

Qdrant Cloud helps agents read, create, update, and delete Qdrant Cloud data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Qdrant Cloud collections and points through an OOMOL-connected account, including listing, inspecting, searching, creating collections, and upserting vectors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create collections and upsert points, including replacing existing vector point data.

Mitigation: Confirm write and destructive action payloads with the user before execution, especially collection names, point IDs, vectors, and payload filters.

Risk: Qdrant Cloud operations run through OOMOL as an intermediary with server-side credential handling.

Mitigation: Use the skill only when that intermediary model is acceptable for the deployment and connected account.

Risk: First-time setup may require running a remote oo CLI installer.

Mitigation: Verify the installer against official OOMOL documentation before running remote install commands.

## Reference(s):

- [Qdrant Cloud homepage](https://qdrant.tech/cloud/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-qdrant)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration guidance, Markdown]

**Output Format:** [Markdown with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the live connector schema before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
