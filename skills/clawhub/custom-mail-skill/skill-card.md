## Description:

Run the Custom Mail console locally with Docker - compose, preview, attachments, send history, and pluggable provider, theme, layout, and logo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xuxuclassmate](https://clawhub.ai/user/xuxuclassmate)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to run a private Docker-based mail console, configure provider credentials and branding, compose and preview messages, send email, and inspect send history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Docker image or source repository could be untrusted by the installing organization.

Mitigation: Confirm trust in the Docker image or GitHub repository before installation.

Risk: A weak admin password or unintended network exposure could allow unauthorized console access.

Mitigation: Use a strong ADMIN_PASSWORD and bind the service only where it is intended to be reachable.

Risk: Sent email content and attachments are shared with the configured mail provider.

Mitigation: Treat messages and attachments as data disclosed to the selected provider and configure provider credentials accordingly.

## Reference(s):

- [Custom Mail GitHub repository](https://github.com/InnoNestX/Custom-Mail)
- [Custom Mail documentation](https://innonestx.github.io/Custom-Mail/)
- [Custom Mail Docker Hub image](https://hub.docker.com/r/xuxuclassmate/custom-mail)
- [Custom Mail ClawHub skill page](https://clawhub.ai/xuxuclassmate/skills/custom-mail-skill)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, markdown]

**Output Format:** [Markdown with inline shell commands and environment variable examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Docker and may include setup for admin and mail provider credentials.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
