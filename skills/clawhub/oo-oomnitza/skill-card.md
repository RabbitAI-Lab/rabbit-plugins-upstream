## Description:

Enables agents to search and read Oomnitza assets, users, and instance metadata through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent inspect Oomnitza assets, users, and connection metadata through approved OOMOL and Oomnitza credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute code from network URLs.

Mitigation: Review the oo CLI installation method before use; prefer a trusted package manager or signed/checksummed installer, and avoid elevated privileges unless OOMOL documents that requirement.

Risk: Read actions can retrieve Oomnitza asset and user records from the connected account.

Mitigation: Use an account with appropriate least-privilege access, inspect the live connector schema before running actions, and confirm requests that could expose sensitive records.

## Reference(s):

- [Oomnitza homepage](https://www.oomnitza.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-oomnitza)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Directs agents to inspect live connector schemas before constructing action payloads; connector runs return JSON responses.]

## Skill Version(s):

1.0.3 (source: SKILL.md frontmatter, server metadata, release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
