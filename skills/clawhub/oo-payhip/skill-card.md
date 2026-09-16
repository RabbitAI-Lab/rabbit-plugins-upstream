## Description:

Payhip (payhip.com). Use this skill for ANY Payhip request: reading, creating, updating, and deleting data through the Payhip connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Payhip through an OOMOL-connected account, including coupon management and license verification workflows. It is intended for agent-assisted Payhip read, write, and delete operations via the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct remote shell installation commands for the oo CLI.

Mitigation: Review the setup instructions before installing and prefer verified or package-manager installation instructions over direct curl-to-shell or PowerShell execution.

Risk: The skill can perform Payhip write and destructive actions such as creating, updating, and deleting coupons or changing license state.

Mitigation: Confirm the exact payload, target, and expected effect with the user before write actions, and require explicit approval before destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-payhip)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Payhip Homepage](https://payhip.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Payhip connector JSON responses when actions are executed]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
