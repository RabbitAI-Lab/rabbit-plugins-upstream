## Description:

Valyu (valyu.ai). Use this skill for ANY Valyu request -- searching and reading data. Whenever a task involves Valyu, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search and read web, academic, financial, and proprietary data through Valyu using an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands that execute scripts directly in a shell.

Mitigation: Review the official oo CLI installation documentation, verify the installer source or checksum when available, and approve setup steps explicitly before running them.

Risk: The skill depends on an OOMOL-connected Valyu account and server-side credential injection.

Mitigation: Use only connected accounts and scopes that are appropriate for the task, and resolve authentication, credential, or billing errors before retrying connector actions.

## Reference(s):

- [Valyu homepage](https://valyu.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON connector payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses from connector runs include a data object and execution metadata.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
