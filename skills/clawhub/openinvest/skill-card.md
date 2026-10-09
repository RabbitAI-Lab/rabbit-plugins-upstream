## Description:

Helps agents review multi-asset portfolios, check prices, run an investment committee, and record portfolio decisions and transactions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[longsizhuo](https://clawhub.ai/user/longsizhuo)

### License/Terms of Use:

MIT-0

## Use Case:

Investors and their agents use this skill to review holdings and market data, obtain committee verdicts, and manage portfolio records. First-time setup is handled by a separate skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Portfolio details and optional API or email credentials may be exposed.

Mitigation: Limit access to trusted agents and configure Gmail or App Password delivery only when needed.

Risk: The backend package may be fetched without a fixed version.

Mitigation: Pin a reviewed backend version using OPENINVEST_SPEC.

Risk: The skill can change persistent portfolio and configuration data.

Mitigation: Require explicit confirmation before buy, sell, deposit, withdraw, or configuration changes.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/longsizhuo/skills/openinvest)
- [Committee protocol](references/committee-protocol.md)
- [Direct and coordinator paths](references/two-paths.md)
- [Tools and commands](references/tools.md)
- [Adding tracked assets](references/adding-assets.md)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown portfolio summaries and committee memos, JSON verdicts, and command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can update persistent portfolio and configuration records when directed.]

## Skill Version(s):

0.22.1 (source: frontmatter, CHANGELOG, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
