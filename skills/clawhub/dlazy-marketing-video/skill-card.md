## Description:

Creates marketing and ecommerce videos from product, brand, or campaign briefs, with multilingual voiceover and an optional virtual host.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams, ecommerce sellers, and brand owners use the skill to turn product information, listings, or campaign briefs into promotional videos for social media and advertising, with optional multilingual voiceover and a virtual host.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files are sent to dLazy's hosted service; attached files are uploaded to its media storage.

Mitigation: Use an organization you control and attach only files you are comfortable sending to the service.

Risk: The CLI uses an API key that can be saved in the local user configuration.

Mitigation: Use the documented per-invocation environment-variable option when appropriate, and rotate or revoke keys from your organization dashboard.

Risk: Video generation may incur service costs.

Mitigation: Consider generation costs before starting a video task.

Risk: The skill relies on a third-party CLI to connect to the hosted service.

Mitigation: Review the CLI before installing it.

## Reference(s):

- [CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video, Text]

**Output Format:** [Generated marketing video assets with streamed text responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include multilingual voiceover or an optional virtual host, depending on the brief.]

## Skill Version(s):

1.0.32 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
