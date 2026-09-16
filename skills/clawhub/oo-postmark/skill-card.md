## Description:

Operate Postmark through an OOMOL-connected account for reading, creating, and updating transactional email resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Postmark server data, manage templates, search outbound messages and bounces, and send transactional or templated email through an OOMOL-connected Postmark account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of remote installer scripts.

Mitigation: Review the installer path before use and prefer a trusted package manager or pinned, checksum-verified oo CLI installer.

Risk: Write actions can send email or change Postmark templates through the connected account.

Mitigation: Confirm the exact payload, target server, recipients, and expected effect with the user before running any write action.

Risk: The skill depends on the active OOMOL account connection and connected Postmark server.

Mitigation: Verify the intended OOMOL account and Postmark connection when authentication, scope, credential, or billing errors occur.

## Reference(s):

- [ClawHub Postmark skill page](https://clawhub.ai/oomol/skills/oo-postmark)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Postmark homepage](https://postmarkapp.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Postmark connector responses as JSON containing data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
