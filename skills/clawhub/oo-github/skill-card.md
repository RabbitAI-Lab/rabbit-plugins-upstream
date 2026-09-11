## Description:

GitHub provides agent workflows for reading, creating, updating, and deleting GitHub data through the OOMOL-connected GitHub service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect GitHub action schemas and run authenticated GitHub read, write, and destructive operations after confirming the target and payload.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands can execute local code from OOMOL's CLI distribution path.

Mitigation: Install only after trusting OOMOL's distribution path and reviewing or otherwise verifying the installer before running it.

Risk: GitHub write and destructive actions can change or remove repository data.

Mitigation: Confirm the exact repository, target object, payload, and intended effect before allowing write or destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-github)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [GitHub](https://github.com)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include GitHub mutation commands; write and destructive actions require user confirmation of the exact target, payload, and effect.]

## Skill Version(s):

1.0.7 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
