## Description:

Langbase helps agents read, create, retrieve, and delete Langbase memory data through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Langbase memories through an OOMOL-connected account, including listing and retrieving memories and creating or deleting them after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include commands that directly execute downloaded installer scripts.

Mitigation: Install the oo CLI only from a trusted source and prefer verified or manually reviewed installation steps before execution.

Risk: The skill can create and delete Langbase memories.

Mitigation: Confirm the exact payload for write actions and the target memory for destructive actions before running them.

## Reference(s):

- [Langbase homepage](https://langbase.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-langbase)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands operate through the oo CLI and may return JSON connector responses.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
