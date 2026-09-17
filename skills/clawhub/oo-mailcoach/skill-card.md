## Description:

Mailcoach helps agents manage Mailcoach email lists and subscribers through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect live Mailcoach action schemas and manage email lists and subscribers through an authenticated OOMOL connection. It supports read, write, and destructive actions with confirmation guidance for state-changing operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write or destructive Mailcoach actions can change or remove lists and subscribers.

Mitigation: Confirm the exact action, target, payload, and expected effect with the user before running write or destructive commands.

Risk: First-time setup includes remote shell installer commands flagged by security review.

Mitigation: Avoid curl | bash or irm | iex installers unless the OOMOL installer channel is trusted; prefer signed, versioned, or manually verified installation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-mailcoach)
- [Mailcoach Homepage](https://www.mailcoach.app)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute oo CLI commands that return JSON data and execution metadata.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
