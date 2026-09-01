## Description:

Helps agents search, browse, install, update, remove, and verify AI trading skills from the OKX Skills Marketplace.

This skill is ready for commercial/non-commercial use.

## Publisher:

[searchworld](https://clawhub.ai/user/searchworld)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage marketplace skills for AI trading agents, including discovery, installation, updates, removal, and signature verification. It is not used to place trades, fetch market data, or manage trading bots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installed third-party skills can run with the local agent's permissions.

Mitigation: Review each skill before installation and install only skills from sources the user trusts.

Risk: Using the documented force option bypasses signature verification.

Mitigation: Avoid force installation unless the user intentionally accepts the package source and verification risk.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/searchworld/skills/okx-cex-skill-mp)
- [OKX homepage](https://www.okx.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May request JSON output from OKX CLI commands when the user needs machine-readable results.]

## Skill Version(s):

1.4.5 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
