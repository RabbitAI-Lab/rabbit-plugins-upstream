## Description:

Quo (OpenPhone) helps agents read, create, update, and delete Quo workspace data through the OOMOL connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Quo contacts, messages, phone numbers, users, and text messaging workflows from an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands that execute scripts directly in a shell.

Mitigation: Prefer the published install guide or independently verify the installer source before running pipe-to-shell commands.

Risk: Write and destructive connector actions can change or delete Quo workspace data.

Mitigation: Confirm the exact action, target, payload, and expected effect with the user before running write or delete commands.

Risk: Action payloads can become inaccurate if generated from stale assumptions.

Mitigation: Inspect the live connector schema immediately before constructing each action payload.

## Reference(s):

- [Quo (OpenPhone) ClawHub release](https://clawhub.ai/oomol/skills/oo-quo)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Quo homepage](https://www.quo.com)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live connector schema inspection before building action payloads.]

## Skill Version(s):

1.0.4 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
