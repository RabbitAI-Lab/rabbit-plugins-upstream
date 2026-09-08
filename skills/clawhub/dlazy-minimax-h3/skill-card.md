## Description:

MiniMax Hailuo omni-modal video model with native stereo audio, producing 5-15 second clips at up to 2K, with support for text-to-video, first/last frame transitions, and multi-asset references for character and scene consistency.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate short MiniMax Hailuo videos through the dLazy CLI from prompts, frame references, or multiple media assets. It is useful when an agent needs to create or retrieve generated video outputs while preserving requested scene, character, or asset consistency.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts, parameters, and referenced media files to the third-party dLazy API and media storage.

Mitigation: Only pass media approved for upload to dLazy, and review applicable dLazy service terms before operational use.

Risk: The dLazy API key may be stored in local CLI configuration or supplied through an environment variable.

Mitigation: Treat the key as a credential, keep local config permissions restricted to the user, and rotate or revoke the key if compromise is suspected.

Risk: Installing the skill may execute a third-party npm CLI package, including as a global binary.

Mitigation: Review the linked dLazy CLI source and npm package before installing, and prefer the pinned npx invocation when a persistent global install is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-minimax-h3)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files]

**Output Format:** [Markdown guidance with bash commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill invokes the dLazy CLI, which returns hosted result URLs or asynchronous task IDs; the bundled install command is pinned to @dlazy/cli@1.2.3.]

## Skill Version(s):

1.2.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
