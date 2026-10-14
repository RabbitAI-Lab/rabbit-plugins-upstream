## Description:

Helps agents track a multi-asset portfolio, check market prices and strategy, and produce investment committee analysis and verdicts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[longsizhuo](https://clawhub.ai/user/longsizhuo)

### License/Terms of Use:

MIT-0

## Use Case:

Investors and their agents use this skill to review holdings, prices and decisions, request multi-asset analysis, and maintain portfolio records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Portfolio, cash, trade, holding, and configuration changes can alter financial records without consistent confirmation.

Mitigation: Require the agent to summarize exact write actions and obtain user approval before recording trades, changing cash or holdings, deleting holdings, or changing configuration.

Risk: Investment committee verdicts or market data may be mistaken for reliable financial advice.

Mitigation: Treat verdicts as informational, not financial advice; verify current prices and review assumptions before making investment decisions.

Risk: Using the skill grants access to an investment ledger and calls external market and language-model services.

Mitigation: Install only if comfortable with that access and review what portfolio information is shared with external services.

## Reference(s):

- [openInvest ClawHub release](https://clawhub.ai/longsizhuo/skills/openinvest)
- [Tools and commands](artifact/references/tools.md)
- [Committee protocol](artifact/references/committee-protocol.md)
- [Onboarding](artifact/references/onboarding.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown, Shell commands]

**Output Format:** [Markdown analysis and verdicts, with structured command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can read and update portfolio records and decision history.]

## Skill Version(s):

0.24.3 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
