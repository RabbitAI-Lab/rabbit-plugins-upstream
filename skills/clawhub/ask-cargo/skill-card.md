## Description:

Helps a GTM team answer Slack questions from its repository and workspace, propose approved work, capture useful threads, and open reviewable pull requests for changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Revenue operations, sales, and GTM engineering teams use a Slack agent to consult repository and workspace context, capture internal discussions, request pull requests, and approve priced actions or handoffs in a thread.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent can answer in any Slack channel the bot has joined, including sensitive or customer-shared channels.

Mitigation: Use an explicit internal channel allowlist; exclude Slack Connect and customer channels.

Risk: Repository instructions could override safety instructions.

Mitigation: Remove the rule giving repository conventions precedence over safety instructions.

Risk: Unpinned CLI installation or fallback execution could change behavior unexpectedly.

Mitigation: Pin and review the Cargo CLI version instead of using latest or an npx fallback.

Risk: A thread approval could authorize work beyond the intended request.

Mitigation: Tie approvals to trusted internal users and the exact proposed actions, records, and cost.

## Reference(s):

- [ClawHub release](https://clawhub.ai/cargo-ai/skills/ask-cargo)
- [Project homepage listed in metadata (source provenance unavailable)](https://github.com/getcargohq/gtm-skills)
- [Capture entry format](references/capture-entry.md)
- [Agent roster](references/roster.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration instructions]

**Output Format:** [Slack thread replies, proposed actions, and pull requests containing code or configuration changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Answers cite their supporting file or command; work requiring spend or handoff is proposed for approval before execution.]

## Skill Version(s):

0.2.1 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
