## Description:

A Slack-accessible agent that answers questions about a go-to-market repository and Cargo workspace, opens pull requests for requested changes, captures threads, and hands approved work to deployed agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Revenue operations, sales, and go-to-market teams use this agent in Slack to query repository and workspace information, request reviewable repository changes, capture relevant discussions, and route approved tasks to other agents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mutable repository instructions can override the agent's safety and approval rules.

Mitigation: Change instruction precedence so repository files cannot override safety, approval, secrecy, Slack, or destructive-action rules before installation.

Risk: Broad Slack access can expose internal repository or workspace details in shared or customer channels.

Mitigation: Keep the bot out of shared and customer channels, or restrict its trigger to explicit channel IDs.

Risk: Unpinned CLI installation can change the toolchain without review.

Mitigation: Pin the Cargo CLI to a reviewed version.

Risk: Excessive service-user permissions or direct changes could bypass review.

Mitigation: Verify the service user remains viewer-only and that changes land as pull requests, never direct merges or deploys.

## Reference(s):

- [Ask Cargo release on ClawHub](https://clawhub.ai/cargo-ai/skills/ask-cargo)
- [Project homepage (listed in release metadata)](https://github.com/getcargohq/gtm-skills)
- [Capture entry format](references/capture-entry.md)
- [Agent roster format](references/roster.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Pull requests, Repository files, Guidance]

**Output Format:** [Slack thread replies with cited answers, proposals, and pull request links; Markdown repository changes when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cost-bearing work and agent handoffs require approval in the Slack thread; changes are proposed as pull requests, not merged or deployed.]

## Skill Version(s):

0.2.3 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
