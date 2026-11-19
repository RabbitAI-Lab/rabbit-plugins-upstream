## Description:

Smart Money analytics on OKX: leaderboard traders, position tracking, trade records, closed-position history, aggregated consensus signals, and signal history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[okx-retail](https://clawhub.ai/user/okx-retail)

### License/Terms of Use:

MIT

## Use Case:

OKX users can use this skill to explore leaderboard traders, review trader performance and position history, and examine aggregated smart money signals. It returns read-only analytics in response to trader and market questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential checks may display local API-key profile or OAuth session information.

Mitigation: Keep credential checks local, review output before sharing, and never paste credentials or session details into chat.

Risk: Two local references were unresolved in the supplied security evidence, so some setup guidance may be incomplete.

Mitigation: Confirm the relevant setup guidance is available in the installed OKX skill collection before following credentialed workflows.

## Reference(s):

- [Trader Commands Reference](references/trader-commands.md)
- [Signal Commands Reference](references/signal-commands.md)
- [Workflow Reference](references/workflows.md)
- [Templates and Formatting Reference](references/templates.md)
- [OKX](https://www.okx.com)
- [ClawHub Skill Page](https://clawhub.ai/okx-retail/skills/okx-cex-smartmoney)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown summaries and tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only trader and signal analytics; values depend on the selected query and time period.]

## Skill Version(s):

1.5.1 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
