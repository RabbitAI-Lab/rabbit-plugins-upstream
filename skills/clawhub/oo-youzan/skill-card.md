## Description:

Youzan helps agents search and read Youzan shop, item, order, logistics, refund, and after-sale data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers with an OOMOL-connected Youzan account use this skill to inspect shop profile, inventory, on-sale items, orders, logistics, refunds, and after-sale records without handling raw credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup guidance includes remote installer commands for the oo CLI.

Mitigation: Use verified OOMOL install instructions where possible and review fetched installer scripts before execution.

Risk: Order, refund, logistics, and shop results may contain sensitive business or customer data.

Mitigation: Treat connector responses as sensitive data and share or store only what is necessary for the task.

Risk: The skill depends on an OOMOL-connected Youzan account.

Mitigation: Install only if the user trusts OOMOL and is comfortable granting the connector access to Youzan account data.

## Reference(s):

- [ClawHub Youzan Skill Page](https://clawhub.ai/oomol/skills/oo-youzan)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Youzan Homepage](https://www.youzan.com/)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration, Text]

**Output Format:** [Markdown with inline shell commands and JSON result descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI to inspect live action schemas before running Youzan connector actions.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
