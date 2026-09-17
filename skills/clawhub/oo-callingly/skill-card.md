## Description:

Callingly lets an agent operate Callingly through an OOMOL-connected account to create, retrieve, update, delete, and list leads, calls, agents, schedules, and teams.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Callingly CRM and calling workflows through an OOMOL-connected account, including lead and call lifecycle actions, team lookup, and agent scheduling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill documents remote installer commands for first-time oo CLI setup.

Mitigation: Prefer a verified or package-managed oo CLI installation and inspect installer sources before execution.

Risk: The skill can create, update, and delete Callingly records.

Mitigation: Confirm the exact target, payload, and expected effect with the user before write or destructive actions.

Risk: OOMOL brokers access to the connected Callingly account.

Mitigation: Install only when the account owner is comfortable with OOMOL handling the Callingly connection and use scoped or rotated credentials where available.

## Reference(s):

- [Callingly homepage](https://callingly.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Callingly skill listing](https://clawhub.ai/oomol/skills/oo-callingly)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
