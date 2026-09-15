## Description:

Builder.io helps an agent read, create, update, list, and delete Builder.io content through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content operators use this skill to manage Builder.io content from an agent session while relying on the OOMOL-connected Builder.io account for credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands that execute downloaded shell or PowerShell scripts.

Mitigation: Install the oo CLI only from a trusted, verified package or pinned release, and validate checksums or signatures before execution.

Risk: The skill can create, update, and delete Builder.io content.

Mitigation: Require explicit user approval for the exact target, payload, and expected effect before any write or destructive action.

Risk: Builder.io operations run through the connected OOMOL account and its configured permissions.

Mitigation: Use a least-privilege Builder.io connection and review account scopes, connection status, and billing state before operational use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-builder-io)
- [Builder.io Homepage](https://www.builder.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute oo connector commands that return JSON responses containing data and meta.executionId.]

## Skill Version(s):

1.0.2 (source: release evidence and frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
