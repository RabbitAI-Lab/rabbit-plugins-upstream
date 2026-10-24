## Description:

MiniMax Hailuo omni-modal video model with native stereo audio, producing 5-15 second clips at up to 2K. Supports text-to-video, first/last frame transitions and multi-asset references for character and scene consistency.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to generate short videos from text prompts, frame transitions, and image, video, or audio references through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference media is uploaded to dLazy for generation, and login stores an organization API key locally.

Mitigation: Only submit media appropriate for cloud processing; use the documented environment-variable option if preferred, protect local credentials, and revoke unused keys.

Risk: The description and CLI help differ on supported resolution limits, and generation may incur costs.

Mitigation: Confirm the currently supported resolution and review estimated generation costs before submitting a request.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-minimax-h3)
- [dLazy](https://dlazy.com)
- [CLI project homepage (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Files, JSON, Shell commands, Configuration instructions]

**Output Format:** [Generated video files and JSON result/task responses; Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation supports prompts and optional frame or media references; output may be asynchronous.]

## Skill Version(s):

1.2.30 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
