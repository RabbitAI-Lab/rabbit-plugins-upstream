## Description:

Youzan helps agents inspect schemas and run OOMOL oo CLI connector actions for Youzan shop, item, order, logistics, refund, inventory, and on-sale item data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers with an OOMOL-connected Youzan account use this skill to retrieve shop, item, order, logistics, refund, inventory, and after-sale information through the oo CLI while checking live action schemas before requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands that could be unsafe if pasted and run without verification.

Mitigation: Prefer an official, verifiable install method or inspect and verify the installer before running it.

Risk: The skill uses OOMOL as the credential-holding connector for the user's Youzan account.

Mitigation: Install only when that trust boundary is acceptable and keep Youzan connections scoped and current.

Risk: Connected-account reads can expose sensitive shop, order, refund, inventory, and logistics data.

Mitigation: Treat outputs as sensitive and share them only with users authorized to access the connected Youzan account.

Risk: The scope wording is broader than the documented action list.

Mitigation: Use the listed actions and inspect the live action schema before constructing each request.

## Reference(s):

- [ClawHub Skill: Youzan](https://clawhub.ai/oomol/skills/oo-youzan)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Youzan homepage](https://www.youzan.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands rely on live connector schemas and a configured OOMOL-connected Youzan account.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
