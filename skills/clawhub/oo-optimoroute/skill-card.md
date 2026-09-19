## Description:

Use this skill to operate OptimoRoute through OOMOL's optimoroute connector for reading, creating, updating, and deleting OptimoRoute data instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage OptimoRoute orders through an OOMOL-connected account, including retrieving, creating, updating, merging, syncing, and deleting orders with confirmation for write or destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup section includes remote installer pipelines for the oo CLI.

Mitigation: Do not let an agent run those pipelines automatically; install the oo CLI through verified, user-controlled steps.

Risk: The skill can create, update, sync, merge, or delete OptimoRoute orders.

Mitigation: Inspect the live action schema and confirm write or destructive payloads and targets with the user before execution.

## Reference(s):

- [OptimoRoute homepage](https://optimoroute.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-optimoroute)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before payload construction; OOMOL injects credentials server-side.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
