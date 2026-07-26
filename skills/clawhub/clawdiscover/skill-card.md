## Description: <br>
Discover and get notified of new AI tools and services relevant to an agent, with optional premium AI summaries and webhook alerts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[x4v13r1120](https://clawhub.ai/user/x4v13r1120) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use ClawDiscover to query service listings, filter tools by category, receive webhook notifications, and add periodic checks for newly launched services. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: External service-discovery calls, paid x402 endpoints, webhook registration, service submissions, and recurring checks can create cost or automation impact when configured too broadly. <br>
Mitigation: Keep paid endpoints, service submissions, webhook registration, and heartbeat scheduling under explicit user control. <br>
Risk: Requests to ClawDiscover could expose secrets, private URLs, or privileged internal webhook endpoints. <br>
Mitigation: Do not submit secrets, private URLs, or privileged internal webhook endpoints. <br>


## Reference(s): <br>
- [ClawDiscover on ClawHub](https://clawhub.ai/x4v13r1120/skills/clawdiscover) <br>
- [ClawDiscover website and API docs](https://clawdiscover.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with curl, JavaScript, and YAML examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces guidance for external API calls, optional x402 paid endpoints, webhook subscriptions, and recurring heartbeat checks.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
