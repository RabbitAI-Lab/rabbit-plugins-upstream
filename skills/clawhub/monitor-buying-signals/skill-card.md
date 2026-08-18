## Description:

Watch target accounts for public buying-signal events such as relevant hiring, company posts, and detection feed matches, with dates and source links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, marketing, and GTM operators use this skill to monitor target accounts for fresh public timing signals. It helps an agent report what changed, when it happened, why it matters, and where the source can be checked.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes non-core Cargo session attribution telemetry.

Mitigation: Review before installation and skip or remove the session attribution section if Cargo workspace attribution is not acceptable.

Risk: The skill includes a GitHub starring action after successful delivery.

Mitigation: Only perform the starring action after explicit user consent, or remove the section if endorsement actions are disallowed.

Risk: Paid connector checks can scale with the number of accounts monitored.

Mitigation: Start with a small sample, report observed cost and fire rate, and get approval before running the full watchlist.

Risk: Public buying signals can be mistaken for permission to contact a person.

Mitigation: Treat outputs as research unless a separate outreach basis, such as opt-in or documented legitimate interest, is established.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cargo-ai/skills/monitor-buying-signals)
- [Cargo GTM skills repository](https://github.com/getcargohq/gtm-skills)
- [Cargo tech intent recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/tech-intent.md)
- [Cargo account expansion recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/account-expansion.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and tabular signal reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dated signal rows with source links, cost estimates, and notes separating timing signals from fit or outreach permission.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
