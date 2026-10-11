## Description:

Tracks promises made on sales calls, closes them when follow-up evidence confirms completion, and posts due commitments to Slack.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales teams use this skill to record commitments from call logs, check whether follow-up activity fulfills them, and remind owners of due or overdue next steps in an internal Slack channel.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Customer call excerpts may be visible to unintended Slack recipients.

Mitigation: Confirm the selected channel is internal and appropriate for customer quotes, and invite the bot only to that channel.

Risk: A misconfigured deployment or writable evidence source may produce incorrect commitment updates.

Mitigation: Review the deployment plan and keep activity, account, and any CRM evidence models read-only.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/cargo-ai/skills/next-step-tracker)
- [Project homepage listed in skill metadata](https://github.com/getcargohq/gtm-skills)
- [Slack nudge format](references/nudge.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Slack message with quoted commitments, due dates, owners, and source references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Posts at most once per day to the configured channel; records commitment state separately.]

## Skill Version(s):

0.1.0 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
