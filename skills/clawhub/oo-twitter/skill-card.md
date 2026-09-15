## Description:

X (Twitter) (x.com). Use this skill for ANY X (Twitter) request: reading, creating, updating, and deleting data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate X (Twitter) through the OOMOL `twitter` connector, including reading timelines and profiles, creating posts, managing Lists and Direct Messages, and uploading media with confirmation safeguards for state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands that execute downloaded code directly.

Mitigation: Prefer a pinned, signed, or package-manager installation path, or independently verify the OOMOL CLI installer source before running it.

Risk: Write and destructive X actions can change or remove account data.

Mitigation: Inspect the live action schema and confirm the exact payload, target, and effect with the user before running write or destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-twitter)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [X homepage](https://x.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON payloads, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs agents to inspect live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.4 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
