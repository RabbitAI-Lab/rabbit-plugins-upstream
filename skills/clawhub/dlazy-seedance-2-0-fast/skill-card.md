## Description:

Generates faster ByteDance Seedance 2.0 videos with text prompts, multi-modal references, and first/last-frame controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run dLazy Seedance 2.0 Fast video generation from an agent workflow with prompts and optional image, video, audio, or first/last-frame inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can save a reusable dLazy API key in a local CLI configuration file.

Mitigation: Prefer passing DLAZY_API_KEY per invocation, or verify that the local config file is readable only by the intended OS user.

Risk: Local image, video, or audio paths supplied to generation commands may be uploaded to dLazy-hosted storage for processing.

Mitigation: Only provide media files that are approved for upload to the dLazy service.

Risk: Video generation requests may consume dLazy account credits.

Mitigation: Use dry-run or review command parameters before generation when cost or credit balance is a concern.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0-fast)
- [dLazy publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source link](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [JSON, Files, Guidance]

**Output Format:** [JSON response with hosted generated media URLs; optional saved media file when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return an asynchronous task identifier when no-wait mode is used.]

## Skill Version(s):

1.3.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
