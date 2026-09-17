## Description:

NeverBounce (neverbounce.com). Use this skill for ANY NeverBounce request - reading, creating, and updating data. Whenever a task involves NeverBounce, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate NeverBounce through OOMOL's oo CLI for email verification, account credit checks, and bulk verification job workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer one-liners that execute downloaded shell or PowerShell scripts.

Mitigation: Install the oo CLI through a verified package or pinned release with checksum or signature validation before using this skill.

Risk: Write actions can create, parse, or start NeverBounce bulk verification jobs.

Mitigation: Confirm the exact action, payload, and expected NeverBounce state change with the user before running actions tagged as write.

Risk: The skill relies on OOMOL server-side credential handling and the NeverBounce connector model.

Mitigation: Use it only in environments where OOMOL account connection, credential handling, and connector access are approved.

## Reference(s):

- [NeverBounce homepage](https://neverbounce.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-neverbounce)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include oo CLI commands, action schema inspection steps, NeverBounce action payloads, and CSV download guidance.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
