## Description:

Combines selecting an event callback address with registering an event callback address.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Integration teams use this skill to choose callback URLs for event subscriptions and record selected callback destinations for service handoffs, account updates, and subscription workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent may suggest or record an incorrect or unauthorized callback URL for a real subscription workflow.

Mitigation: Review callback destinations before using them for production account, service, or event subscription traffic.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/event-callback-url)
- [ClawHub publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text, guidance, configuration]

**Output Format:** [Text or Markdown with callback URL and subscription receipt fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces callback_url and recorded_callback values for agent-mediated event subscription workflows.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
