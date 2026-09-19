## Description:

Operate Hex projects through an OOMOL-connected account using the oo CLI to inspect schemas, list and retrieve projects and runs, trigger published runs, and cancel in-progress runs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to work with Hex projects and project runs from an agent session through an OOMOL-managed Hex connection. It supports read workflows, published project execution, run cancellation, setup guidance, and billing or connection troubleshooting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes pipe-to-shell installer commands for the oo CLI.

Mitigation: Prefer a verified or package-managed oo CLI install, or review the installer before running it.

Risk: The skill relies on OOMOL as an intermediary for Hex account access.

Mitigation: Review Hex connection scopes before use and keep credentials limited to the access needed for the task.

Risk: Triggering or canceling Hex project runs can change state or consume account resources.

Mitigation: Require explicit user confirmation for the exact project, payload, and intended effect before triggering or canceling runs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-hex)
- [Hex Homepage](https://hex.tech)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include oo CLI commands, JSON request payloads, setup guidance, and JSON connector responses.]

## Skill Version(s):

1.0.2 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
