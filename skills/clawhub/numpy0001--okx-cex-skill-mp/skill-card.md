## Description:

Browse, search, install, update, remove, and verify AI trading skills from the OKX Skills Marketplace.

This skill is ready for commercial/non-commercial use.

## Publisher:

[numpy0001](https://clawhub.ai/user/numpy0001)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and trading-assistant operators use this skill to discover and manage marketplace skills for trading workflows. It helps agents produce marketplace search, install, update, remove, and verification guidance without placing orders or retrieving market data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install third-party trading skills across multiple local agent environments.

Mitigation: Install only marketplace skills from trusted publishers and review each downloaded SKILL.md before use.

Risk: The documented force-install path can bypass signature verification.

Mitigation: Avoid --force unless the source is trusted and the verification failure has been reviewed.

Risk: Marketplace access depends on the OKX CLI and configured API credentials.

Mitigation: Use a pinned CLI package version and configure credentials only in environments where marketplace access is intended.

## Reference(s):

- [OKX Homepage](https://www.okx.com)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and optional JSON command-output guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the okx CLI and marketplace API credentials for full marketplace access.]

## Skill Version(s):

1.3.8 (source: server release evidence; artifact metadata and CLI package reference 1.3.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
