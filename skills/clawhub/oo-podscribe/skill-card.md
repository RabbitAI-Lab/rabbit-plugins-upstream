## Description:

Operates Podscribe through an OOMOL-connected account to retrieve integration health, show information, and episode search results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to search and read Podscribe data through the OOMOL connector without handling raw Podscribe API tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup directs users to run remote installer scripts directly in a shell.

Mitigation: Install the oo CLI from a verified, version-pinned source with checksum or signature verification, and avoid curl or PowerShell pipe execution from elevated shells.

## Reference(s):

- [ClawHub Podscribe Skill](https://clawhub.ai/oomol/skills/oo-podscribe)
- [Podscribe Homepage](https://podscribe.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are JSON objects containing data and meta.executionId when actions run successfully.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
