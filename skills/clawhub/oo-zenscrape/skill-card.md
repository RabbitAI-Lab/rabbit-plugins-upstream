## Description:

Fetch public web pages through Zenscrape using the OOMOL oo connector, with live schema inspection before each action.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to fetch public URLs through a connected Zenscrape account without handling raw API tokens directly. It is suited for web page retrieval tasks that need optional rendering, proxy, header, or wait controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded scripts.

Mitigation: Prefer an official, version-pinned, or otherwise verifiable installer and review the installation path before executing it.

Risk: The skill can fetch arbitrary public URLs through a third-party Zenscrape account.

Mitigation: Confirm the target URL and intended retrieval behavior before execution, and avoid sending private or sensitive URLs through the connector.

Risk: Authentication, account connection, credential, scope, and billing recovery steps may require user account action.

Mitigation: Only start login, connection, or billing recovery after a matching command failure and with user confirmation.

## Reference(s):

- [Zenscrape homepage](https://zenscrape.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-zenscrape)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Zenscrape connector responses include data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
