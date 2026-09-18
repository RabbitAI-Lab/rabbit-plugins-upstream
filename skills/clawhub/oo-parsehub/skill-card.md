## Description:

ParseHub enables agents to search and read ParseHub project data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect ParseHub projects available to a connected API key, including listing projects and retrieving a project by token.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include third-party pipe-to-shell installer commands for the OOMOL CLI.

Mitigation: Verify the installer source independently before running it, or use a signed or package-manager installation path when available.

Risk: ParseHub request and response data is routed through OOMOL for connector execution and server-side credential injection.

Mitigation: Install and use the skill only when routing this data through OOMOL is acceptable for the user's data handling requirements.

## Reference(s):

- [ClawHub ParseHub skill listing](https://clawhub.ai/oomol/skills/oo-parsehub)
- [ParseHub homepage](https://www.parsehub.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Text, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires fetching each connector action schema before building request payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
