## Description:

AfterShip (aftership.com). Use this skill for AfterShip requests involving reading, creating, updating, and deleting data through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate an OOMOL-connected AfterShip account for shipment tracking workflows, including reading, creating, updating, retracking, completing, and deleting tracking records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup examples include pipe-to-shell installation commands for the oo CLI, which create local execution risk if run automatically.

Mitigation: Review and install the oo CLI through a verified method; do not allow an agent to run the installer automatically.

Risk: The skill can create, update, complete, retrack, and delete AfterShip tracking records.

Mitigation: Confirm write and destructive actions with the user, including the exact payload and target record, before execution.

Risk: Embedding raw JSON directly in shell commands can lead to quoting mistakes or unintended payload changes.

Mitigation: Prefer passing JSON through a safely created file and inspect the live action schema before running connector commands.

## Reference(s):

- [AfterShip homepage](https://www.aftership.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-aftership)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
