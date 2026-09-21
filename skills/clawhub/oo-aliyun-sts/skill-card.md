## Description:

Alibaba Cloud STS (alibabacloud.com) supports reading, creating, and updating Alibaba Cloud STS data through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to request Alibaba Cloud STS temporary credentials through an OOMOL-connected Alibaba Cloud account. It supports assuming roles and retrieving federated credentials after checking the live connector schema for each action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can request Alibaba Cloud STS temporary credentials.

Mitigation: Require confirmation before any credential-returning action and verify the action payload and expected effect with the user.

Risk: The artifact includes remote installer commands that pipe downloaded scripts to a shell.

Mitigation: Prefer a verified package or separately reviewed installer before installing the oo CLI.

## Reference(s):

- [Alibaba Cloud RAM and STS](https://www.alibabacloud.com/product/ram)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-aliyun-sts)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash, PowerShell, text, and JSON command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can return JSON connector responses that include temporary credential data.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
