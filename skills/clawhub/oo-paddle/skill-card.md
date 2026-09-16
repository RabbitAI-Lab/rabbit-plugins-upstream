## Description:

Paddle (paddle.com). Use this skill for ANY Paddle request: reading, creating, and updating data through the OOMOL Paddle connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Paddle products, prices, and customers through an OOMOL-connected account. It supports read actions and user-confirmed write actions for catalog and customer workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path recommends running a remote installer directly in the shell.

Mitigation: Review the installer source and prefer a signed or package-manager installation path before using the skill.

Risk: Write actions can create or update Paddle customers, products, and prices.

Mitigation: Confirm the exact payload and intended effect with the user before running any write action.

Risk: Connector action schemas may change over time.

Mitigation: Inspect the live action schema before constructing a payload.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-paddle)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Paddle Homepage](https://www.paddle.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May run oo CLI connector actions that return JSON responses from Paddle.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
