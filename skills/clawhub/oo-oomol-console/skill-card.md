## Description:

OOMOL Console (console.oomol.com) lets an agent read, create, update, and delete OOMOL Console data through the OOMOL Console connector instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and team administrators use this skill to operate OOMOL Console from an agent, including account and team reads, billing and usage review, member management, and Connection permission group administration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform write and destructive OOMOL Console actions, including team member changes and Connection permission group updates or deletion.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write or destructive actions, and inspect the live action schema before building payloads.

Risk: The documented first-time setup uses remote installer commands that execute downloaded scripts in a shell.

Mitigation: Use a verified and pinned installer path when possible, or inspect and validate the installer before execution.

## Reference(s):

- [OOMOL Console homepage](https://console.oomol.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-oomol-console)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before action payloads; connector responses are JSON.]

## Skill Version(s):

1.0.2 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
