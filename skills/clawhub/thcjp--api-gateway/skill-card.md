## Description: <br>
Helps agents use a hosted Maton API gateway to manage connections, configure triggers, replay events, and route approved calls to services such as Slack, Gmail, Salesforce, and Stripe. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, automation builders, and teams use this skill to connect agent workflows to third-party SaaS APIs through a managed gateway, with read-first checks and explicit approval for write operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Trigger configurations can place MATON_API_KEY or OAuth tokens directly in stored downstream authorization headers. <br>
Mitigation: Prefer managed connection references or a platform secret mechanism, and review trigger definitions and logs for retained secrets before use. <br>
Risk: The skill can act across Maton-connected third-party services, including write operations after approval. <br>
Mitigation: Begin with read-only GET checks, verify the target account, and require explicit approval before every POST, PUT, PATCH, or DELETE request. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/api-gateway) <br>
- [Maton API gateway](https://api.maton.ai/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with bash commands, Python examples, API request examples, and JSON response shapes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include API call plans that require explicit user approval before non-GET actions.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
