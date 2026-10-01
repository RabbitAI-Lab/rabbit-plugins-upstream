## Description:

Helps agents choose a dLazy video model and generate videos from text prompts, images, or other media.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate video from prompts, animate images, create frame-guided clips, and produce talking-head or lip-synced video through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are sent to dLazy for cloud generation, and generated files are hosted on its storage.

Mitigation: Only submit content you are comfortable sharing with dLazy; review its service terms before use.

Risk: The skill uses a pinned npm CLI and requires a dLazy API key that may be stored in local user configuration.

Mitigation: Review the CLI before installing; use DLAZY_API_KEY per invocation if you do not want the key saved in local configuration.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-video-generate)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with inline commands and generated video links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated video files are hosted by dLazy.]

## Skill Version(s):

1.4.24 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
