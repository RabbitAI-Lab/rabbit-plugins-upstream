## Description:

Feathery (feathery.io) lets agents read, create, update, and delete Feathery data through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators with Feathery-connected OOMOL accounts use this skill to inspect connector schemas and run Feathery read, write, and delete actions for forms, users, submissions, sessions, account details, and hidden fields.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends executing remote installer scripts directly in a shell without verification.

Mitigation: Install oo from a verified official package or separately download and inspect or verify the installer before running it.

Risk: Write and destructive Feathery actions can change or delete account data.

Mitigation: Confirm the exact payload, target, and expected effect with the user before running write or delete connector actions.

## Reference(s):

- [ClawHub Feathery skill page](https://clawhub.ai/oomol/skills/oo-feathery)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Feathery homepage](https://www.feathery.io/)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: evidence release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
