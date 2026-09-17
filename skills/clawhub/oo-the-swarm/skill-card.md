## Description:

The Swarm connector lets an agent search and fetch company and profile records and check authenticated team API credit usage through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query The Swarm data from an OOMOL-connected account, including company search, profile search, record retrieval, and team credit usage checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup can execute a remotely downloaded installer without version or integrity checks.

Mitigation: Use the official OOMOL CLI installation documentation, prefer a signed or versioned package where available, inspect and verify installers before running them, and do not let an agent execute curl | bash or irm | iex automatically.

Risk: The connector sends search payloads and account usage requests through OOMOL and The Swarm.

Mitigation: Only connect The Swarm when the user trusts OOMOL and The Swarm with the search payloads and account usage involved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-the-swarm)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [The Swarm homepage](https://www.theswarm.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON when actions are run with the documented --json flag.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
