## Description:

A Slack-mention agent that answers GTM questions from repository and workspace context, proposes reviewable pull requests for changes, and requests approval before running or handing off work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Revenue operations, sales leadership, and GTM engineers use this skill to configure a shared Slack agent that answers from GTM context, opens pull requests for requested edits, and routes approved work to deployed agents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Slack mention can expose repository or workspace context in any channel where the bot is present, including shared channels.

Mitigation: Review the bot's channel membership; prefer explicit internal channel IDs and keep it out of customer or shared channels.

Risk: The agent has broad GTM repository and workspace authority, while spend, handoffs, and change controls largely rely on prompt rules.

Mitigation: Review the CDK plan and GitHub permissions before deployment; enforce approvals and high-impact restrictions outside the prompt where supported, and review pull requests before merging.

Risk: Installing the latest Cargo CLI can change deployment behavior unexpectedly.

Mitigation: Pin and review the Cargo CLI version before installation or deployment.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/cargo-ai/skills/ask-cargo)
- [Project homepage (listed in release metadata)](https://github.com/getcargohq/gtm-skills)
- [Ask Cargo documentation (listed in skill metadata)](https://github.com/getcargohq/gtm-skills/tree/main/ask-cargo)
- [Agent roster template](references/roster.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration guidance]

**Output Format:** [Markdown with TypeScript configuration and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Slack replies may contain cited answers, approval proposals, and pull request links.]

## Skill Version(s):

0.1.1 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
