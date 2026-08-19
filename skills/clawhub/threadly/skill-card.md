## Description:

Interact with Threadly, an AI social-listening and reply-drafting tool for X/Twitter, to list discovered conversations, review drafted replies, list published replies, and manage webhook subscriptions through Threadly's public REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thumbflipcontact-ops](https://clawhub.ai/user/thumbflipcontact-ops)

### License/Terms of Use:

MIT

## Use Case:

External developers, operators, and social-listening teams use this skill to inspect Threadly conversations and drafts, then record explicit human approve or reject decisions for specific draft IDs. It can also manage conversation webhook subscriptions when the user has a stable public HTTPS endpoint.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A project-scoped Threadly API key gives the agent access to that project's Threadly data and actions.

Mitigation: Install the skill only for Threadly projects where agent access is acceptable, and provide only the required project-scoped THREADLY_API_KEY.

Risk: Approving or rejecting the wrong draft ID could record an unintended human decision.

Mitigation: Review the draft ID and content carefully, and instruct the agent to approve or reject only one specific draft ID per decision.

Risk: Webhook subscriptions send conversation events to the configured target URL.

Mitigation: Use only stable public HTTPS endpoints you control, verify Threadly delivery signatures, and prefer polling when no suitable endpoint is available.

## Reference(s):

- [Threadly public API reference](references/PUBLIC_API.md)
- [Threadly website](https://www.usethreadly.co)
- [ClawHub skill page](https://clawhub.ai/thumbflipcontact-ops/skills/threadly)
- [n8n community node for the same public API](https://github.com/thumbflipcontact-ops/n8n-nodes-threadly)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and API response summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call Threadly's public REST API with a project-scoped API key and return JSON responses or human-readable summaries.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
