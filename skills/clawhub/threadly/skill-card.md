## Description:

Interact with Threadly, an AI social-listening and reply-drafting tool for X/Twitter, to list discovered conversations, review drafts, record explicitly human-directed approve or reject decisions, list published replies, and manage webhook subscriptions through Threadly's public REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thumbflipcontact-ops](https://clawhub.ai/user/thumbflipcontact-ops)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to let an agent inspect Threadly project activity, summarize conversations and drafts for review, and carry out specific human-approved draft or webhook actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The configured API key can read Threadly project data and make approval, rejection, and webhook changes for that project.

Mitigation: Use a project-scoped key, keep it secret, and revoke keys or webhook subscriptions that are no longer needed.

Risk: Approving or rejecting a draft records a real decision tied to the API key creator.

Mitigation: Approve or reject only specific draft IDs that a human has reviewed and explicitly named in the current task.

Risk: Webhook subscriptions send project events to the configured endpoint.

Mitigation: Register only HTTPS endpoints you control or trust, verify delivery signatures, and prefer polling when no stable public endpoint is available.

## Reference(s):

- [Threadly public API reference](references/PUBLIC_API.md)
- [Threadly website](https://www.usethreadly.co)
- [Threadly ClawHub listing](https://clawhub.ai/thumbflipcontact-ops/skills/threadly)
- [OpenClaw](https://openclaw.ai/)
- [ClawHub documentation](https://docs.openclaw.ai/clawhub)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl and a project-scoped THREADLY_API_KEY; jq is optional for formatting JSON responses.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
