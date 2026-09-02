## Description:

Fast image generation with Doubao Seedream 5.0 Lite, supporting text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to generate or transform images through dLazy's hosted Seedream 5.0 Lite CLI workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local image files supplied to the skill may be sent to dLazy's hosted service.

Mitigation: Use the skill only when hosted processing is acceptable, and avoid submitting confidential prompts or files unless the user's data policy permits it.

Risk: Login can store a dLazy API key in the local CLI configuration.

Mitigation: Use per-invocation DLAZY_API_KEY or npx when less persistent local configuration is preferred, and rotate or revoke keys when needed.

Risk: Generic image-generation triggers can overlap with other installed image-generation skills.

Mitigation: Confirm the intended provider before invoking the skill when multiple image-generation options are available.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-lite)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON result objects containing generated image URLs or async task status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images may be returned as hosted file URLs, and the CLI can save result assets to a local path when requested.]

## Skill Version(s):

1.3.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
