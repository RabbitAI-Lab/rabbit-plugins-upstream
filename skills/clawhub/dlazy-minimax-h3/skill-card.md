## Description:

Helps agents create short MiniMax H3 videos from text prompts, frame transitions, or reference media through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short videos with text prompts, first and last frames, or image, video, and audio references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media may be sent to the hosted dLazy service.

Mitigation: Only submit content you are authorized to share with that service.

Risk: Signing in may save an API key locally.

Mitigation: Protect the local key and rotate it in the dLazy dashboard if it is exposed.

Risk: Using a third-party npm CLI may leave a persistent global installation.

Mitigation: Review the package before use and choose the documented npx invocation if a global install is unnecessary.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-minimax-h3)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI project (publisher-provided link)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides commands for generating videos and interpreting returned asset links; media generation occurs through the dLazy service.]

## Skill Version(s):

1.2.23 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
