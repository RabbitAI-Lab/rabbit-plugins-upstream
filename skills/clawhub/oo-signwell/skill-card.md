## Description:

SignWell (signwell.com). This skill supports reading, creating, and updating SignWell data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate SignWell workflows from an agent through the OOMOL-connected oo CLI, including account, template, and document lookup, document creation from templates, draft sending, and reminder sending.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup guidance may ask users to run unverified remote installer scripts directly in a shell.

Mitigation: Review the installer path before use and prefer a verified, version-pinned source or official package process.

Risk: Write actions can create documents, send drafts for signing, or send reminder emails in SignWell.

Mitigation: Confirm the exact SignWell document, recipients, payload, and expected effect before allowing write actions.

## Reference(s):

- [SignWell homepage](https://www.signwell.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub SignWell skill page](https://clawhub.ai/oomol/skills/oo-signwell)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector schemas and JSON command output when actions are run.]

## Skill Version(s):

1.0.3 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
