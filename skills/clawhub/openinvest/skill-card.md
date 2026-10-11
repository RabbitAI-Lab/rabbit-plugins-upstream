## Description:

Helps agents review multi-asset portfolios, check market data, record positions, and produce investment committee verdicts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[longsizhuo](https://clawhub.ai/user/longsizhuo)

### License/Terms of Use:

MIT-0

## Use Case:

Individual investors and their agents use this skill to inspect holdings and market prices, assess potential trades through a four-role committee, and maintain portfolio records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Portfolio data and configured LLM, hub, or email credentials are sensitive.

Mitigation: Grant access only when appropriate, avoid sharing secrets in chat, and redact broker screenshots before sharing.

Risk: The default backend package is not version-pinned.

Mitigation: Pin OPENINVEST_SPEC to a reviewed openinvest version.

Risk: Write commands can persistently change investment records.

Mitigation: Confirm every proposed write and its details before committing it.

## Reference(s):

- [openInvest on ClawHub](https://clawhub.ai/longsizhuo/skills/openinvest)
- [Tool and command reference](references/tools.md)
- [Committee protocol](references/committee-protocol.md)
- [Onboarding guide](references/onboarding.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Guidance]

**Output Format:** [Markdown verdicts and portfolio summaries; structured JSON tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save committee decisions and update investment records when requested.]

## Skill Version(s):

0.24.1 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
