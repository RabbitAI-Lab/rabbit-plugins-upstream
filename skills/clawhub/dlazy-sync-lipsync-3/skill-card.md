## Description:

Helps agents generate a lip-synced video from an input video and audio for dubbing, localization, or virtual presenters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to align a speaker's lip movements in video with supplied audio for dubbing, localization, and virtual presenters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the third-party CLI and using its account service requires trusting the provider.

Mitigation: Review the dLazy CLI and account service before installation or use.

Risk: Provided local video and audio may be uploaded to dLazy for processing.

Mitigation: Submit only media you are willing to share with dLazy.

Risk: Saved API keys can be exposed on shared or CI machines.

Mitigation: Use DLAZY_API_KEY instead of saved login on shared or CI machines.

Risk: Some documentation examples use prompt and image references that may not match this video-and-audio command.

Mitigation: Check the command help and confirm input flags rather than copying those examples.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-sync-lipsync-3)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI on GitHub](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI can return a generated media URL or an asynchronous task ID.]

## Skill Version(s):

1.3.24 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
