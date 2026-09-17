## Description:

TabAPI enables agents to search Google and retrieve website, DNS, WHOIS/RDAP, backlink, traffic, screenshot, and page-content data through an OOMOL-connected TabAPI account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to inspect TabAPI action schemas, run read-oriented TabAPI requests, and troubleshoot authentication, connection, and billing setup for TabAPI access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that execute downloaded shell or PowerShell scripts.

Mitigation: Review the CLI installation path before use and prefer an official package manager, pinned release, or downloaded installer with checksum or signature verification.

Risk: Future TabAPI actions tagged as write or destructive could change, remove, or overwrite data.

Mitigation: Inspect the live action schema first, confirm the exact payload and target with the user, and require explicit approval before running tagged actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-tabapi)
- [TabAPI Homepage](https://tabapi.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON command responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [TabAPI command results include data and meta.executionId when run with --json.]

## Skill Version(s):

1.0.2 (source: server evidence release and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
