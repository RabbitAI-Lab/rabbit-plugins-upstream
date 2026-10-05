## Description:

Helps create ecommerce marketing videos from product briefs, documents, or listings, with multilingual voiceover and an optional virtual host.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants and marketing teams use this skill to turn product information or online listings into short promotional videos for ecommerce and social campaigns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authentication requires a dLazy API key stored in CLI configuration or supplied via an environment variable.

Mitigation: Protect the key, limit access to the configuration, and rotate or revoke it if exposed.

Risk: Prompts and selected local files are sent to dLazy's hosted service.

Mitigation: Review content before submission and upload only files approved for that service.

Risk: Project sessions retain context across follow-up requests.

Mitigation: Use separate projects for sensitive work and clear saved sessions when appropriate.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-marketing-video)
- [dLazy CLI repository (linked in skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Streaming text with video-generation results from the hosted service]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results and follow-up conversations are associated with a dLazy project.]

## Skill Version(s):

1.0.21 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
