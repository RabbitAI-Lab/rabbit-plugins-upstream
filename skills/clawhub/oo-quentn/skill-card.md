## Description:

Quentn lets agents operate Quentn through an OOMOL-connected account to read, create, update, and delete contacts, terms, and users via the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to automate Quentn CRM workflows through an OOMOL-connected account, including contact lookup, contact and term management, and user or term listing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup directs users to run remote oo CLI installer scripts directly in a shell.

Mitigation: Review the installer through a safer channel first, or prefer a pinned or package-manager installation when available.

Risk: Write and destructive actions can change or delete Quentn contacts and terms.

Mitigation: Inspect the live connector schema, confirm the exact target and payload with the user, and require explicit approval before state-changing actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-quentn)
- [Quentn homepage](https://quentn.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live connector schema inspection before payload construction; command responses are JSON.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
