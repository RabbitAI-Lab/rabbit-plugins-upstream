## Description:

This skill helps agents submit and query mmaudio tasks that generate sound effects and video dubbing through api.a7w.cn using a user-provided API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[2253128](https://clawhub.ai/user/2253128)

### License/Terms of Use:

MIT

## Use Case:

External developers and agents use this skill to configure an a7w API key, submit asynchronous mmaudio generation jobs, poll task status, and retrieve JSON results for generated sound effects or video dubbing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles paid API credentials and can store them locally or read them from the environment.

Mitigation: Use only an API key you control, keep it out of source control, store it with restricted local permissions, and rotate it if exposure is suspected.

Risk: The client can be pointed at a custom host through A7W_HOST or --host.

Mitigation: Do not set A7W_HOST or --host unless you intentionally trust the endpoint receiving the API key and request payloads.

Risk: The included client can access more of the a7w plugin marketplace than just mmaudio.

Mitigation: Use the documented mmaudio commands for this skill and review any command that lists, dumps, or calls other available plugins.

Risk: Submitted media URLs and generated content may involve private data, paid usage, or content-compliance obligations.

Mitigation: Avoid sensitive or private media URLs, confirm account balance and billing expectations before submitting jobs, and review generated content for rights and policy compliance.

## Reference(s):

- [Getting Started](references/getting-started.md)
- [Submit API](references/api-submit.md)
- [Query API](references/api-query.md)
- [ClawHub Skill Page](https://clawhub.ai/2253128/skills/sanjianke-mmaudio)
- [a7w API Marketplace](https://api.a7w.cn/)
- [AI Plugin Marketplace](https://aigc.a7w.cn/)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a user-provided API key, may write JSON results when an output path is requested, and may poll asynchronous tasks until completion.]

## Skill Version(s):

1.0.5 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
