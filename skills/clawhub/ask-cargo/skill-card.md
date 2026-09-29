## Description:

A Slack agent that answers GTM repository and workspace questions, prepares changes as pull requests, and hands off approved work to deployed agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Team members ask questions about their GTM repository and workspace in Slack, request reviewable pull requests, and approve agent handoffs or work in the thread.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Repository instructions can override approval, confidentiality, or prohibited-operation rules.

Mitigation: Before installation, change instruction precedence so repository files cannot override those rules.

Risk: The bot may answer in customer or shared Slack channels it can reach.

Mitigation: Verify channel reach before deployment and keep the bot out of customer and shared channels.

Risk: Installing an unpinned Cargo CLI can introduce unreviewed changes.

Mitigation: Pin or preinstall the Cargo CLI before deployment.

Risk: Pull requests and actions that spend, send, or modify records require human oversight.

Mitigation: Require human review of pull requests and explicit approval before those actions proceed.

## Reference(s):

- [Ask Cargo ClawHub release](https://clawhub.ai/cargo-ai/skills/ask-cargo)
- [Publisher-listed project homepage](https://github.com/getcargohq/gtm-skills)
- [Agent ownership roster](references/roster.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands]

**Output Format:** [Slack thread replies, proposed commands, and GitHub pull requests]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Answers cite supporting files or commands; proposed work awaits approval in the Slack thread; code changes are submitted for review rather than merged or deployed.]

## Skill Version(s):

0.1.0 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
