## Description:

Healthchecks.io (healthchecks.io). Use this skill for ANY Healthchecks.io request — reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Healthchecks.io checks through an OOMOL-connected account, including reading check data, creating or updating checks, pausing or resuming monitoring, and deleting checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path can run remote oo CLI installer scripts.

Mitigation: Review and independently verify the oo CLI installer source before running remote install commands, or install the CLI through a trusted internal process.

Risk: Healthchecks.io write and delete actions can change monitoring state or remove checks.

Mitigation: Confirm the exact target, payload, and expected effect with the user before write actions, and require explicit approval before destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-healthchecks-io)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Healthchecks.io homepage](https://healthchecks.io)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs the agent to inspect live action schemas before constructing connector requests.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
