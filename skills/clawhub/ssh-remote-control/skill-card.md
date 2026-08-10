## Description:

Enables an AI agent to connect to authorized Mac or Linux computers over SSH and run remote commands for file, application, system, and development operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lixiang92229](https://clawhub.ai/user/lixiang92229)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent administer authorized remote computers through SSH without installing an agent on the controlled machine.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote commands, screenshots, and file reads can reveal or change sensitive data on the target computer.

Mitigation: Install and use the skill only for computers the user owns or is authorized to administer, and review commands before execution.

Risk: A reused or broadly privileged SSH key could grant access beyond this skill's intended target.

Mitigation: Use a dedicated SSH key with a passphrase where practical, rotate it regularly, and avoid using daily login keys.

Risk: Broadly exposed SSH access increases the chance of unauthorized access attempts.

Mitigation: Use a restricted non-admin account, key-only authentication, authorized_keys restrictions, and avoid exposing SSH broadly.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/lixiang92229/skills/ssh-remote-control)
- [Project Homepage](https://github.com/lixiang92229/skill-ssh-remote-control)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash command examples and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands are intended for authorized SSH targets configured through environment variables.]

## Skill Version(s):

1.0.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
