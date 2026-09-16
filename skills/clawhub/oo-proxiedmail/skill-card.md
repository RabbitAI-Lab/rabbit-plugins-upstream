## Description:

ProxiedMail helps agents read, create, and update ProxiedMail data through an OOMOL-connected account instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate a connected ProxiedMail account through OOMOL, including listing and updating proxy bindings and reading received-email data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path tells users to execute remote installer scripts directly in a shell.

Mitigation: Review the oo CLI installation path before installing, and prefer an official, versioned, signed, or checksum-verified installer.

Risk: Once connected, the skill can read ProxiedMail email data and create or update proxy email bindings.

Mitigation: Use the skill only with an account where that access is intended, and confirm exact payloads before running write actions.

## Reference(s):

- [ProxiedMail homepage](https://proxiedmail.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub ProxiedMail skill page](https://clawhub.ai/oomol/skills/oo-proxiedmail)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
