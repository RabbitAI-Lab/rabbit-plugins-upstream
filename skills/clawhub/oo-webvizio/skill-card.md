## Description:

Webvizio guides an agent to use the OOMOL oo CLI for Webvizio connector actions, including creating and deleting REST Hook subscriptions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Webvizio REST Hook subscriptions through an OOMOL-connected account while checking live action schemas before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include unverified internet installer commands that can execute code on the user's machine.

Mitigation: Use a versioned, signed, checksum-verified installer when available, or inspect the downloaded installer before running it.

Risk: The skill can create or delete Webvizio REST Hook subscriptions.

Mitigation: Confirm the exact payload, target subscription, and expected effect with the user before any write or delete action.

## Reference(s):

- [Webvizio homepage](https://webvizio.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-webvizio)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas and JSON responses from oo connector commands.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
