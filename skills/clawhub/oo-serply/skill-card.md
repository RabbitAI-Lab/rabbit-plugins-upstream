## Description:

Serply lets agents run Serply-backed Google web, News, Scholar, and Video searches through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search Google web, News, Scholar, and Video through Serply while relying on OOMOL-managed credentials and live connector schemas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands that can execute changing internet-hosted code.

Mitigation: Use a verified, pinned installer or package-manager installation with checksum or signature validation before installing the OOMOL CLI.

Risk: Connector calls depend on a signed-in OOMOL account, an active Serply connection, and sufficient billing credit.

Mitigation: Only run setup, connection, or billing steps after a matching command failure, and keep those actions separate from normal search execution.

## Reference(s):

- [Serply Homepage](https://serply.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Serply Skill](https://clawhub.ai/oomol/skills/oo-serply)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON result descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are returned as JSON data with execution metadata.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
