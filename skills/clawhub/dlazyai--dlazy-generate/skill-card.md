## Description:

Selects a dLazy CLI model to generate images, videos, or audio from a user's request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to choose and invoke dLazy models for image, video, and audio generation or editing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files are sent to dLazy's hosted service.

Mitigation: Review prompts and files before submitting sensitive content.

Risk: Generation may consume dLazy credits.

Mitigation: Check credit balance and expected cost before running requests.

Risk: CLI login stores an API key in local configuration.

Mitigation: Use per-invocation DLAZY_API_KEY and npx when persistent credentials or a global install are unwanted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-generate)
- [dLazy CLI source (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Text]

**Output Format:** [CLI commands and JSON responses containing generated-media URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is hosted by dLazy; commands may accept local media files as inputs.]

## Skill Version(s):

1.3.31 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
