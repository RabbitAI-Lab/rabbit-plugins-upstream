## Description:

Helps agents review multi-asset portfolios, analyze market symbols with an AI investment committee, and record portfolio decisions and transactions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[longsizhuo](https://clawhub.ai/user/longsizhuo)

### License/Terms of Use:

MIT-0

## Use Case:

Investors and their agents use this skill to inspect holdings and live prices, request investment-committee analysis, review past decisions, and log changes to positions or cash records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run a backend package without a fixed version.

Mitigation: Pin OPENINVEST_SPEC to a reviewed package version before use.

Risk: Investment activity can expose API credentials and Gmail app passwords.

Mitigation: Use dedicated, revocable credentials and protect the local configuration.

Risk: Position or cash-record changes may alter sensitive portfolio records.

Mitigation: Confirm the intended changes with the user before writing them.

Risk: Portfolio history and committee transcripts may persist locally or on a remote hub.

Mitigation: Review access to local and remote storage before using the skill.

## Reference(s):

- [openInvest ClawHub release](https://clawhub.ai/longsizhuo/skills/openinvest)
- [Tools and commands](references/tools.md)
- [Committee execution paths](references/two-paths.md)
- [Onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands]

**Output Format:** [Markdown responses and JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include portfolio summaries, committee verdicts, and transaction confirmations.]

## Skill Version(s):

0.24.0 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
