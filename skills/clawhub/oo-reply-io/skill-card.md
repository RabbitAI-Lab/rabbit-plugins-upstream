## Description:

Operate Reply.io through an OOMOL-connected account to read, create, update, start, and pause Reply.io contacts and sequences.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and business operators use this skill to manage Reply.io contacts and sequences through the OOMOL oo CLI. It supports contact lookup, contact mutation, sequence lookup, sequence start or pause, and current-user verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote shell installation of the OOMOL CLI.

Mitigation: Review the installation path first and prefer a verified, version-pinned installer or official package-manager method.

Risk: The skill can create or update Reply.io contacts and start or pause sequences.

Mitigation: Only allow write or destructive actions after checking the exact target, action, and payload with the user.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-reply-io)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Reply.io homepage](https://reply.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, JSON, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Reply.io connector schemas before building action payloads.]

## Skill Version(s):

1.0.3 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
