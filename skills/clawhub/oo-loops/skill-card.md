## Description:

Loops helps an agent operate Loops through an OOMOL-connected account for reading, creating, updating, deleting contacts, managing contact metadata, listing mailing lists, and sending events.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent inspect Loops schemas and run Loops connector actions through the oo CLI for contact, mailing list, property, and workflow event tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands.

Mitigation: Review the setup path before installing and use a trusted, verifiable oo CLI installation method.

Risk: Loops write, event-send, and delete actions can change or remove account data.

Mitigation: Require explicit user confirmation of the exact payload, target, and expected effect before running those actions.

## Reference(s):

- [Loops homepage](https://loops.so)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Loops Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-loops)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo connector schemas before write, event-send, or delete actions.]

## Skill Version(s):

1.0.4 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
