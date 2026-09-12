## Description:

Seedance 2.5 is a dLazy CLI-accessed video generation skill for ByteDance's Seedance 2.5 model, supporting prompts, multimodal references, first/last frame control, clips up to 30 seconds, and resolutions up to 2160p.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke the dLazy-hosted Seedance 2.5 video generation API from an agent workflow, supplying text prompts and optional image, video, audio, or frame references to create generated video assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts and selected local image, video, or audio files to dLazy hosted API and media storage.

Mitigation: Use only media approved for upload to dLazy, and review applicable service terms before use.

Risk: The skill requires a dLazy API key stored in local CLI config or passed through the environment.

Mitigation: Use revocable organization-scoped keys, restrict local config access, and rotate or revoke keys when no longer needed.

Risk: The release installs or executes the third-party @dlazy/cli package through npm or npx.

Mitigation: Review the package or source before use in sensitive environments, and prefer npx or an isolated environment where practical.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-5)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, files]

**Output Format:** [JSON result payload from the dLazy CLI with generated asset URLs, plus an optional downloaded media file when --save is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; local media references may be uploaded to dLazy-hosted storage.]

## Skill Version(s):

1.2.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
