## Description:

Findymail helps agents search and verify professional email information through a connected Findymail account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent retrieve Findymail credit usage, search professional contacts by name or domain, search employees, and verify email addresses through a connected Findymail account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that can execute code on the user's machine.

Mitigation: Review the oo CLI installation path first and prefer a signed package, pinned release, or downloaded installer that can be inspected before execution.

Risk: Connector calls can fail when the user is not authenticated, Findymail is not connected, credentials are expired, or account credit is insufficient.

Mitigation: Run setup, reconnection, or billing steps only after a matching command failure and follow the skill's scoped recovery guidance.

## Reference(s):

- [Findymail ClawHub skill page](https://clawhub.ai/oomol/skills/oo-findymail)
- [Findymail homepage](https://www.findymail.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Findymail connector results as JSON when actions are run.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
