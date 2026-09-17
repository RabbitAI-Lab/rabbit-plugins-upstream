## Description:

Serpdog lets an agent run Serpdog-powered Google Search, News, Videos, Autocomplete, and account quota requests through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent query Serpdog through an OOMOL-connected account, inspect live action schemas, run read-only search actions, and retrieve account or quota details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance references unverified internet installer scripts that can execute local code.

Mitigation: Do not let an agent run curl|bash or irm|iex installer commands automatically; use a verified package manager, pinned release, or manually inspected installer for the oo CLI.

Risk: Connector actions run against a connected Serpdog account and can consume account quota.

Mitigation: Use trusted OOMOL and Serpdog accounts, inspect the live action schema before requests, and check account or quota details with get_account_info when needed.

## Reference(s):

- [ClawHub Serpdog Skill](https://clawhub.ai/oomol/skills/oo-serpdog)
- [Serpdog Homepage](https://serpdog.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text with shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and a meta.executionId value.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
