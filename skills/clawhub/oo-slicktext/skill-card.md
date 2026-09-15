## Description:

SlickText lets an agent read, create, update, and delete SlickText contacts and retrieve authenticated brand details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage SlickText contact records and inspect brand information through an authenticated SlickText connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include an unverified remote installer script.

Mitigation: Review the installer source and prefer a signed or checksum-verified installation method before using this skill.

Risk: Create, update, and delete actions can change real SlickText account data.

Mitigation: Confirm the exact payload and intended effect with the user before running write or destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-slicktext)
- [SlickText Homepage](https://www.slicktext.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas before write or destructive SlickText operations.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
