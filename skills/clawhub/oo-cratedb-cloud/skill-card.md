## Description:

This skill helps agents search and read CrateDB Cloud data through an OOMOL-connected account instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect CrateDB Cloud users, organizations, projects, clusters, products, and regions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can lead agents to execute unverified remote installer scripts.

Mitigation: Install the oo CLI through a verified, pinned, or manually inspected method before use.

Risk: CrateDB Cloud metadata is routed through OOMOL as an intermediary connector.

Mitigation: Use a least-privilege read-only CrateDB Cloud API key limited to the organizations and projects intended for querying.

## Reference(s):

- [CrateDB Cloud homepage](https://cratedb.com/database/cloud)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-cratedb-cloud)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: server evidence release.version and skill metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
