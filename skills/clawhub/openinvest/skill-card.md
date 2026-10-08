## Description:

Helps agents review multi-asset portfolios, retrieve market data, record holdings changes, and produce investment committee verdicts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[longsizhuo](https://clawhub.ai/user/longsizhuo)

### License/Terms of Use:

MIT-0

## Use Case:

Investors and their agents use this skill to inspect portfolios and prices, evaluate assets with an AI investment committee, and manage an investment ledger with user approval for changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An unpinned external backend can change between runs while handling portfolio data.

Mitigation: Pin OPENINVEST_SPEC to a reviewed version before installation or use.

Risk: Portfolio, cash, configuration, and holdings writes can alter a persistent investment ledger.

Mitigation: Require explicit user confirmation before each write and review the intended change.

Risk: Optional API and email credentials may be exposed if supplied in chat.

Mitigation: Configure credentials privately when possible; avoid pasting secrets into chat.

## Reference(s):

- [ClawHub openInvest release](https://clawhub.ai/longsizhuo/skills/openinvest)
- [openInvest project wiki](https://github.com/longsizhuo/openInvest/tree/main/docs/wiki)
- [Tools and commands](references/tools.md)
- [Committee protocol](references/committee-protocol.md)
- [Coordinator and Direct paths](references/two-paths.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance, Shell commands]

**Output Format:** [Markdown narrative and investment verdicts, with JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include portfolio summaries, prices, decision history, and proposed ledger changes.]

## Skill Version(s):

0.21.0 (source: release metadata, frontmatter, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
