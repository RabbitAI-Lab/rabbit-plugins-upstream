## Description:

Use this skill to read, create, update, and delete Sendbird data through OOMOL's oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Sendbird users, group channels, messages, session tokens, and moderation actions from an OOMOL-connected account. It supports read, write, and destructive workflows while requiring confirmation for state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer fallback commands could execute unverified code if run blindly.

Mitigation: Use official installation documentation or a verified package and checksum path before installing the oo CLI.

Risk: Write and destructive Sendbird actions can alter or delete users, channels, messages, tokens, and moderation state.

Mitigation: Confirm the exact target, payload, and expected effect with the user before every write or destructive action.

Risk: The skill operates through an OOMOL-connected Sendbird account.

Mitigation: Install and use it only when the user trusts OOMOL and intends to let an agent manage that Sendbird account.

## Reference(s):

- [Sendbird homepage](https://sendbird.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-sendbird)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands call the oo CLI and may return JSON responses containing data and meta.executionId.]

## Skill Version(s):

1.0.4 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
