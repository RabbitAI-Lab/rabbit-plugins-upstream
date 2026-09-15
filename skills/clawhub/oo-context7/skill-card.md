## Description:

Context7 helps agents search libraries and retrieve Context7 documentation and code snippets through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to discover libraries in Context7 and retrieve targeted documentation or code snippets for implementation work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes an unverified remote installer run directly in a shell.

Mitigation: Review the setup path before installing and prefer a verified installer source, safer package-manager flow, or pinned installation method.

Risk: The skill relies on OOMOL-mediated Context7 access.

Mitigation: Use it only when OOMOL account mediation, connection setup, and billing requirements are acceptable for the deployment.

## Reference(s):

- [Context7 homepage](https://context7.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-context7)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payload patterns]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to inspect live action schemas before constructing Context7 requests.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
