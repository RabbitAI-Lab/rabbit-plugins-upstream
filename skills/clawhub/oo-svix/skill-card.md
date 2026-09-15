## Description:

Helps agents manage Svix applications, endpoints, event types, and messages through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Svix connector schemas, run read actions, and manage webhook infrastructure such as applications, endpoints, event types, and messages. It is intended to keep credentials out of agent prompts while requiring confirmation before write, dispatch, or delete operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends running remote installer scripts directly.

Mitigation: Prefer an official, versioned installer with checksum or signature verification before installing the oo CLI.

Risk: Write, delete, and message-dispatch actions can change Svix state or send webhook messages.

Mitigation: Confirm the exact target, payload, and intended effect with the user before running write, destructive, or dispatch actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-svix)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Svix Homepage](https://www.svix.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call oo connector schema before building request payloads and oo connector run for Svix actions.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
