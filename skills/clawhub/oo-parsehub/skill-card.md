## Description:

Operate ParseHub through an OOMOL-connected account to search and read project data with the oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect live ParseHub connector schemas and run read-only ParseHub project actions through an authenticated OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path recommends executing a mutable remote installer directly in a shell.

Mitigation: Prefer a pinned package, verified checksum or signature, or manual installer review before installing the oo CLI.

Risk: ParseHub request details and returned data are handled through OOMOL as part of connector execution.

Mitigation: Review data sensitivity and organizational approval for routing ParseHub connector activity through OOMOL before use.

## Reference(s):

- [ClawHub ParseHub skill page](https://clawhub.ai/oomol/skills/oo-parsehub)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ParseHub homepage](https://www.parsehub.com)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON request/response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing ParseHub action payloads.]

## Skill Version(s):

1.0.3 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
