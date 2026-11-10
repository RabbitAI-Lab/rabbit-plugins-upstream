## Description:

Convert storyboard contents into a video-generation pipeline that can be added to the canvas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use storyboard details such as dialogue, scene prompts, aspect ratio, and resolution to build a video-generation pipeline and add it to the canvas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented authentication and remote generation steps extend beyond storyboard retrieval and can send prompts or media to dLazy-hosted services.

Mitigation: Use a dedicated API key, keep it out of prompts, and submit only media approved for dLazy's hosted services; rotate or revoke the key if it is exposed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-video-storyboard-generate)
- [dLazy CLI repository link listed in skill metadata (provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Configuration, Guidance]

**Output Format:** [JSON video-generation pipeline with canvas drawing guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Combines shared audio and scene-image elements with per-storyboard audio and video elements; positions follow storyboard order with 100-pixel gaps.]

## Skill Version(s):

1.2.36 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
