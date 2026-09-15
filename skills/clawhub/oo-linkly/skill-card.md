## Description:

Linkly (linklyhq.com) supports reading, creating, updating, and deleting Linkly data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to manage Linkly short links through an OOMOL-connected account, including listing workspaces, listing or retrieving links, creating links, updating links, and deleting links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands that execute downloaded shell or PowerShell scripts.

Mitigation: Use an official, version-pinned installation method with checksum or signature verification before running the oo CLI.

Risk: The skill can create, update, or delete Linkly resources.

Mitigation: Confirm the exact target, payload, and expected effect with the user before write or destructive actions.

Risk: The skill operates through OOMOL-mediated access to a Linkly account.

Mitigation: Use it only when the user is comfortable with the OOMOL connection model and has connected the intended Linkly account.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-linkly)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Linkly homepage](https://linklyhq.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill may also return connector JSON data when Linkly actions are executed.]

## Skill Version(s):

1.0.3 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
