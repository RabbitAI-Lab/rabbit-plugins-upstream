## Description:

Helps agents operate Onfleet tasks through the OOMOL oo connector, including reading, creating, updating, completing, cloning, and deleting tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External operators and agents use this skill to manage Onfleet task workflows through an OOMOL-connected account. It is suited for reading task data and for carefully approved task creation, updates, completion, cloning, and deletion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write and destructive actions can change, complete, clone, or delete Onfleet tasks.

Mitigation: Confirm the exact target, payload, and expected effect with the user before create, update, complete, clone, or delete actions.

Risk: Connector action schemas can differ from assumptions in the skill text.

Mitigation: Inspect the live action schema with the oo CLI before constructing each payload.

Risk: Authentication, connection scope, expired credentials, or billing errors can block operation.

Mitigation: Use the documented setup and troubleshooting steps only after a matching command failure.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-onfleet)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Onfleet Homepage](https://onfleet.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
