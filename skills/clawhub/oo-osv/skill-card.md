## Description:

OSV helps agents query OSV vulnerability data through OOMOL's oo CLI instead of calling the OSV API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, security engineers, and agents use this skill to fetch complete OSV vulnerability records and query vulnerabilities for packages or package versions through the OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on OOMOL's oo CLI and a signed-in OOMOL session, so OSV lookups fail when the CLI is missing or unauthenticated.

Mitigation: Run setup only after a matching command failure, use OOMOL's install guide, and sign in once with oo auth login when authentication errors occur.

Risk: First-time setup includes remote installer commands that should not be run casually.

Mitigation: Review OOMOL's installer guidance and verify the installer source before running pipe-to-shell installation commands.

Risk: Stale assumptions about connector inputs can lead to failed or inaccurate OSV queries.

Mitigation: Fetch the live connector schema with oo connector schema before constructing each action payload.

## Reference(s):

- [ClawHub OSV Skill](https://clawhub.ai/oomol/skills/oo-osv)
- [OSV Homepage](https://osv.dev)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON]

**Output Format:** [Markdown guidance with oo CLI commands and JSON payload or response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses read-only OSV connector actions and instructs agents to fetch live action schemas before execution.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
