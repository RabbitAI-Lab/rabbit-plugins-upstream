## Description:

SureContact helps agents read, create, update, and delete SureContact contacts, lists, and tags through the OOMOL-connected oo CLI instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage SureContact contacts, lists, and tags through an OOMOL-connected account while confirming write and destructive operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write and destructive actions can change or remove SureContact contacts, lists, or tags.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running tagged write or destructive actions.

Risk: SureContact operations are mediated by OOMOL rather than direct credential handling.

Mitigation: Install only if OOMOL-mediated access is acceptable and keep the SureContact connection and scopes current in OOMOL.

Risk: First-time setup can involve pipe-to-shell oo CLI installation commands.

Mitigation: Review the oo CLI installation path or script before running install commands.

## Reference(s):

- [SureContact homepage](https://surecontact.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub SureContact skill page](https://clawhub.ai/oomol/skills/oo-surecontact)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON when commands are run with the documented --json option.]

## Skill Version(s):

1.0.3 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
