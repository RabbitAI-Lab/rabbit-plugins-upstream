## Description:

Tracks promises made on sales calls, checks whether they were kept, and posts due or overdue follow-ups to an internal Slack channel each weekday morning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales representatives and sales leaders use this skill to track commitments from recorded calls, verify completed follow-ups against activity records, and receive reminders for outstanding next steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Customer quotes or sensitive sales details could be posted to the wrong audience.

Mitigation: Set and review the locked Slack channel before deployment; use an internal channel with appropriate access.

Risk: Instructions embedded in call transcripts, emails, or notes could influence the agent's actions.

Mitigation: Treat source records as untrusted data and add explicit prompt rules or tests before deploying.

Risk: A mistaken activity match could close a commitment before it is fulfilled.

Mitigation: Keep evidence models read-only and close commitments only on clearly matching, cited activity or call evidence.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/cargo-ai/skills/next-step-tracker)
- [Cargo GTM skills homepage (listed in ClawHub metadata)](https://github.com/getcargohq/gtm-skills)
- [Nudge message reference](references/nudge.md)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Slack-formatted reminder message]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Groups due and overdue promises by owner and cites source call entries; posts at most once per day.]

## Skill Version(s):

0.1.1 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
