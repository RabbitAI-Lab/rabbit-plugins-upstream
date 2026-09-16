## Description:

Intercom helps agents read, create, and update Intercom data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Intercom schemas, read workspace records, and create or update contacts and conversations through an OOMOL-connected Intercom account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes pipe-to-shell installer commands for the oo CLI.

Mitigation: Use a verified package, pinned release, or manually downloaded installer with checksum or signature validation.

Risk: The skill operates through OOMOL as an intermediary for the user's Intercom workspace.

Mitigation: Install only after confirming that this trust relationship is acceptable for the workspace.

Risk: Write actions can modify Intercom contacts and conversations.

Mitigation: Review the exact action payload and user-visible effect before approving any write operation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-intercom)
- [Intercom homepage](https://www.intercom.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown text with shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return JSON responses from the oo CLI; write actions require user confirmation.]

## Skill Version(s):

1.0.4 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
