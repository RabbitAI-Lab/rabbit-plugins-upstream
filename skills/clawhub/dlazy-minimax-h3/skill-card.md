## Description:

MiniMax Hailuo omni-modal video model with native stereo audio, producing 5-15 second clips at up to 2K. Supports text-to-video, first/last frame transitions and multi-asset references for character and scene consistency.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call dLazy's MiniMax H3 video-generation CLI for text-to-video generation, frame-transition videos, and reference-driven video outputs with optional local saving.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files are sent to dLazy cloud services for generation.

Mitigation: Use the skill only with prompts and media you are comfortable uploading to dLazy.

Risk: The skill uses a third-party CLI that stores an API key in the user's local configuration.

Mitigation: Review the dLazy CLI and service terms before installing, and rotate or revoke the API key when it is no longer needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-minimax-h3)
- [dLazy CLI Source](https://github.com/dlazyai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, json, files]

**Output Format:** [Markdown instructions with CLI commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media URLs are returned by the service; the CLI can save the generated asset to a local path.]

## Skill Version(s):

1.2.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
