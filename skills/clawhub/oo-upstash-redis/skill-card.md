## Description:

Provides an agent workflow for Upstash Redis requests, including reading, creating, updating, and deleting data through OOMOL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent inspect schemas and run Upstash Redis reads, writes, expirations, scans, and deletes through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can write, expire, or delete Redis keys.

Mitigation: Confirm the exact payload, target key, and expected effect with the user before approving state-changing or destructive actions.

Risk: The skill relies on the oo CLI and OOMOL account connection to operate an Upstash Redis instance.

Mitigation: Install and authenticate the oo CLI only when needed, and review the installer before running it if the CLI is not already installed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-upstash-redis)
- [Publisher Profile](https://clawhub.ai/user/oomol)
- [Upstash Redis](https://upstash.com/redis)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce live connector command output as JSON when the agent runs oo connector actions.]

## Skill Version(s):

1.0.0 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
