## Description:

1Password Events API (1password.com). Use this skill for ANY 1Password Events API request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to read 1Password Events API audit events, item usage events, and sign-in attempts through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes direct execution of an unverified remote installer.

Mitigation: Review the installer source first, or use a verified package, pinned release, or manual installation path before running setup.

Risk: The skill accesses 1Password event data through an OOMOL-connected account.

Mitigation: Confirm the OOMOL connection, account scope, and organizational authorization before requesting audit, item usage, or sign-in event data.

## Reference(s):

- [1Password Events API homepage](https://1password.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides the agent to inspect live connector schemas before constructing payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
