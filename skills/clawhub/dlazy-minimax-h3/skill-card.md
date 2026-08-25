## Description:

Invokes the dLazy MiniMax Hailuo H3 video-generation CLI to create 5-15 second clips at up to 2K from text prompts, first and last frames, or multi-asset references with native stereo audio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call the dLazy MiniMax H3 video-generation service from an agent workflow, including text-to-video, frame-transition, and reference-asset generation. It is suitable when the user wants generated video output or a saved media file through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party dLazy account and may store an API key in the local CLI configuration.

Mitigation: Use the DLAZY_API_KEY environment variable for per-invocation credentials when persistent local storage is not desired, and rotate or revoke keys from the dLazy dashboard if exposure is suspected.

Risk: Media files passed to image, video, or audio options are uploaded to dLazy cloud services for processing.

Mitigation: Pass only media intended for third-party cloud processing and avoid sensitive or regulated files unless the user's organization has approved that use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-minimax-h3)
- [dLazy CLI source repository](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, json, files, guidance]

**Output Format:** [CLI commands and JSON responses with optional downloaded media files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated assets are hosted or downloaded through dLazy; async runs may return a generateId for later polling.]

## Skill Version(s):

1.2.6 (source: server release metadata; artifact frontmatter reports 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
