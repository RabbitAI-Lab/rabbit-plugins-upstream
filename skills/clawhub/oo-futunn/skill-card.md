## Description:

Futunn helps agents search and read Futunn account, market, trading, company, valuation, news, and community data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent retrieve Futunn account information, orders, positions, fills, market data, company data, valuation data, news, and community search results from an OOMOL-connected Futunn account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read sensitive account, order, position, fill, and market data available to a connected Futunn account.

Mitigation: Install only for trusted agents and accounts, keep Futunn connection scopes limited to the intended workflow, and review returned account data before sharing it outside the session.

Risk: The artifact suggests installing the oo CLI by piping a downloaded script into a shell.

Mitigation: Prefer a verified package or signed release path for the oo CLI, and review installation steps before executing them.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-futunn)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Futunn Homepage](https://open.futunn.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs the agent to inspect live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
