## Description:

Templated helps agents manage Templated renders, templates, and account information through the OOMOL-connected oo CLI instead of calling the Templated API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Templated action schemas, create or retrieve renders, list or filter templates, and manage account-related checks through an authenticated OOMOL connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path includes remote installer scripts that execute in a shell.

Mitigation: Review the setup path before installing and prefer a pinned, verifiable oo CLI release or inspect the installer before running it.

Risk: The skill can create renders and delete renders in a connected Templated account.

Mitigation: Require explicit user approval before create_render or delete_render actions, including confirmation of the target render or payload.

## Reference(s):

- [Templated homepage](https://templated.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution and returns CLI JSON responses when actions are run.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
