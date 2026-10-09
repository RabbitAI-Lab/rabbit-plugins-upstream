## Description:

Helps agents write natural Persian Telegram messages and check drafts for leftover Latin words and Western digits before sending.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ehsanghaffar](https://clawhub.ai/user/ehsanghaffar)

### License/Terms of Use:

MIT-0

## Use Case:

Teams and developers using agents for Telegram chats, channels, and notifications can draft natural Persian replies, summaries, alerts, and button labels, then review language issues before sending.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Allowed Latin terms can reduce the checker’s strictness over time.

Mitigation: Review additions to the allowlist and run the strict check before sending.

Risk: Automated checks cannot ensure natural prose and may exempt unwanted Latin text in protected spans.

Mitigation: Read each draft for tone and language quality, including code-adjacent and parenthetical text.

## Reference(s):

- [Telegram Persian Enforcer on ClawHub](https://clawhub.ai/ehsanghaffar/skills/telegram-persian-enforcer)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Persian text or Telegram-formatted Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves intentional code, links, and identifiers; honors explicit requests for another language.]

## Skill Version(s):

1.0.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
