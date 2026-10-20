## Description:

Guides agents in selecting and running dLazy video models for text-to-video, image-to-video, and other video-generation tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to choose a dLazy model and generate videos from prompts, images, video, or audio, including lip-synced clips.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected images, videos, or audio are sent to dLazy's hosted service.

Mitigation: Avoid submitting sensitive prompts or media without permission to share them with dLazy.

Risk: Generated media is hosted by dLazy, and API requests may consume account credits.

Mitigation: Check hosting requirements and account balance before submitting requests.

Risk: The CLI can save an API key to local configuration.

Mitigation: Protect the local configuration or use the per-invocation environment-variable option.

## Reference(s):

- [dLazy CLI source (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)
- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-video-generate)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON]

**Output Format:** [Markdown guidance and shell commands; the CLI returns JSON with generated media URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated videos are hosted by dLazy.]

## Skill Version(s):

1.4.33 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
