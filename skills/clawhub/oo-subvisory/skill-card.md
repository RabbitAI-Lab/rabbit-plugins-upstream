## Description:

Subvisory (subvisory.com). Use this skill for reading, creating, updating, and deleting Subvisory categories, payment methods, and subscriptions through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Subvisory account data through approved oo CLI connector actions. It supports read, create, update, and delete workflows for categories, payment methods, and subscriptions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands for the oo CLI.

Mitigation: Use the installer only after independently trusting and verifying the OOMOL CLI source and installation guide.

Risk: The connector can create, update, and delete Subvisory account data.

Mitigation: Confirm exact write and delete payloads, target identifiers, and expected effects before approving state-changing actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-subvisory)
- [Publisher Profile](https://clawhub.ai/user/oomol)
- [Subvisory Homepage](https://www.subvisory.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON payload expectations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include oo CLI commands, JSON request payload guidance, and connector result summaries.]

## Skill Version(s):

1.0.2 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
