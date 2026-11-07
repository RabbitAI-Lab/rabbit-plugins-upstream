## Description:

Helps agents review multi-asset portfolios, prices, strategies and decision history, record position changes, and run a four-role investment committee analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[longsizhuo](https://clawhub.ai/user/longsizhuo)

### License/Terms of Use:

MIT-0

## Use Case:

Investors use this skill through an AI agent to review holdings, market prices, strategy, and past decisions, and to record position changes. It can also run committee analysis for supported assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Transcript-saving instructions can execute commands embedded in pasted content.

Mitigation: Use structured MCP transcript submission instead of shell-pasting transcripts.

Risk: Automatic holdings parsing does not clearly explain which model provider may receive portfolio data.

Mitigation: Confirm the model provider before importing real holdings; use structured holdings_v2 to avoid external onboarding parsing.

Risk: Broker autopilot can enable live trading, and the downloaded backend and setup components have not been reviewed in this release evidence.

Mitigation: Keep broker autopilot disabled unless deliberately configured, and review the backend and setup components before relying on them.

Risk: An optional background service may run without being needed.

Mitigation: Install the background service only when it is wanted.

## Reference(s):

- [Tools and commands](references/tools.md)
- [Coordinator committee protocol](references/committee-protocol.md)
- [Hermes committee protocol](references/committee-protocol-hermes.md)
- [Coordinator and Direct paths](references/two-paths.md)
- [Adding tracked assets](references/adding-assets.md)
- [Onboarding reference](references/onboarding.md)
- [Troubleshooting](references/troubleshooting.md)
- [Project wiki](https://github.com/longsizhuo/openInvest/tree/main/docs/wiki)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown, Shell commands, Text]

**Output Format:** [Text or Markdown analysis and guidance, with shell commands and structured tool results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asset symbols and, where relevant, portfolio or strategy context shape the result.]

## Skill Version(s):

0.34.2 (source: frontmatter, CHANGELOG, released 2026-11-06)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
