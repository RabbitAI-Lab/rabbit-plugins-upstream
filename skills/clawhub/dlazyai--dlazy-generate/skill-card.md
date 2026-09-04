## Description:

A comprehensive generation skill that helps an agent select and run dLazy CLI models for image, video, and audio generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to turn natural-language creative requests into dLazy CLI commands for generating images, videos, audio, speech, music, vector assets, segmentation masks, upscaling, and related media outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generation commands can send prompts and selected local media files to dLazy cloud services.

Mitigation: Avoid passing sensitive files and confirm the exact command and file paths before running generation requests.

Risk: The skill can use stored credentials and may trigger paid API calls.

Mitigation: Prefer npx or the DLAZY_API_KEY environment variable for less persistent use, monitor credit usage, and rotate or revoke API keys when needed.

Risk: Broad activation can route varied creative requests into authenticated CLI actions with limited confirmation.

Mitigation: Ask for user confirmation before running commands that upload files, consume credits, or use ambiguous media inputs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-generate)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source link from metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Text]

**Output Format:** [Markdown guidance with inline bash commands; dLazy CLI commands return JSON envelopes and hosted media URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx and a dLazy API key; generation commands may upload selected local media files to dLazy-hosted endpoints.]

## Skill Version(s):

1.3.11 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
