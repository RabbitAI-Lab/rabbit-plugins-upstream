## Description:

Tracks stocks, ETFs, indices, crypto assets where available, and FX pairs with caching and provider fallback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent for market data lookup and simple financial tracking across securities, crypto assets, and FX pairs. It is not intended for trade execution, account actions, private financial-file handling, or credential handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad read, write, and command execution capability while finance-data boundaries are not clearly defined.

Mitigation: Review before installation, run with least-privilege permissions, and approve file writes or shell commands only when they are necessary for the requested finance lookup.

Risk: The security guidance warns against use for trading, account actions, private financial files, and credential handling.

Mitigation: Limit use to informational market-data lookup and analysis; do not provide account credentials, private financial documents, or instructions to place trades.

Risk: The security summary notes inconsistent instructions and behavior partly unrelated to finance lookup.

Mitigation: Check each proposed action against the user's finance task and decline unrelated automation, command execution, or file modification.

## Reference(s):

- [ClawHub finance skill page](https://clawhub.ai/thcjp/skills/finance)
- [Source artifact SKILL.md](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with optional JSON snippets and shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use financial symbols and intervals; artifact text mentions caching and provider fallback but does not define clear finance-data safety boundaries.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
