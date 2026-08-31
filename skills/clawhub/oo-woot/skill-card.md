## Description:

Provides agent access to Woot offer and category feed data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect live Woot category feeds and retrieve details for one or more Woot offers through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on OOMOL as the intermediary for the user's Woot connection.

Mitigation: Install and use it only when the user is comfortable with OOMOL-mediated access to Woot.

Risk: One-time CLI or login setup can introduce risk if run from untrusted sources.

Mitigation: Run setup only from trusted OOMOL sources and only when an auth, connection, or missing-CLI error requires it.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-woot)
- [Woot Homepage](https://www.woot.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include Woot data and an execution identifier when actions run successfully.]

## Skill Version(s):

1.0.0 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
