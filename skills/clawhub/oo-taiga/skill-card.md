## Description:

Taiga (taiga.io). Use this skill for ANY Taiga request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, project managers, and agent users use this skill to inspect and manage Taiga projects, issues, tasks, and user stories through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path may ask users to run a remote installer directly in a shell.

Mitigation: Review official installation instructions and verify the installer before execution.

Risk: Write or update actions can change Taiga data through the connected account.

Mitigation: Confirm the exact action, target, and payload before allowing create or update commands.

Risk: The skill depends on an OOMOL-connected Taiga account and server-side credential handling.

Mitigation: Install and use it only when the publisher and account connection model are trusted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-taiga)
- [Taiga homepage](https://taiga.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Taiga connector payloads and summarize JSON responses returned by the oo CLI.]

## Skill Version(s):

1.0.3 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
