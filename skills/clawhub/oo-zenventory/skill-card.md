## Description:

Zenventory (zenventory.com). Use this skill for ANY Zenventory request: reading, creating, and updating data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect Zenventory connector schemas and run JSON-based create, retrieve, list, search, and update actions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes pipe-to-shell installer snippets for the oo CLI.

Mitigation: Prefer a verified installation method or review and verify the installer before execution.

Risk: Create and update actions can change Zenventory account data.

Mitigation: Confirm exact payloads and intended effects with the user before running write actions.

## Reference(s):

- [Zenventory ClawHub release](https://clawhub.ai/oomol/skills/oo-zenventory)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Zenventory homepage](https://www.zenventory.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
