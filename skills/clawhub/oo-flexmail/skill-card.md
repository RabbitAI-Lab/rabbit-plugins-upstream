## Description:

Flexmail (flexmail.be) supports agent-assisted reading, creation, update, and deletion of Flexmail data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Flexmail through an OOMOL-connected account, including contact, preference, interest, source, segment, language, and custom-field workflows. It guides agents to inspect live action schemas before running read, write, or destructive Flexmail connector actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes commands that install the oo CLI by piping remote scripts directly into a shell.

Mitigation: Review the setup step before installation and prefer a verifiable package or downloaded release with checksum or signature validation.

Risk: Write and destructive Flexmail actions can change or remove account data.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running any action tagged write or destructive.

## Reference(s):

- [Flexmail homepage](https://flexmail.be/en)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Flexmail Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-flexmail)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before payload construction; write and destructive actions require confirmation.]

## Skill Version(s):

1.0.2 (source: SKILL.md metadata and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
