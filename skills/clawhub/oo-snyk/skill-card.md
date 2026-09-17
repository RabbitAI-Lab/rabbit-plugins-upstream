## Description:

Snyk (snyk.io). Use this skill for ANY Snyk request - searching and reading data. Whenever a task involves Snyk, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security teams use this skill to read Snyk organizations, projects, issues, and authenticated principal information through an OOMOL-connected Snyk account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes remote installer commands executed directly in a shell.

Mitigation: Prefer verified, signed, or package-manager based oo CLI installation instructions before using the connector.

Risk: The skill accesses Snyk data through an OOMOL-mediated connected account.

Mitigation: Install only when OOMOL-mediated access is acceptable, and review connector outputs before sharing them.

## Reference(s):

- [ClawHub Snyk Skill](https://clawhub.ai/oomol/skills/oo-snyk)
- [Snyk Homepage](https://snyk.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include structured data and execution metadata.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
