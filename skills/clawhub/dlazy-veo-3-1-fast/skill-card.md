## Description:

Generates short text-to-video or image-to-video clips through the dLazy CLI using Google Veo 3.1 Fast.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to generate or extend short videos from prompts and optional image or video inputs through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party CLI and hosted service that require API credentials.

Mitigation: Review the @dlazy/cli source or npm package under strict supply-chain controls and prefer npx or another isolated execution method when possible.

Risk: Prompts, selected local media, and generated outputs may be sent to or hosted by dLazy services.

Mitigation: Confirm with the user before uploading local media or sensitive prompts, and avoid submitting confidential files unless the environment permits that service use.

Risk: Video generation can consume paid dLazy credits.

Mitigation: Use dry-run or confirm cost-sensitive requests before generation, especially for high-resolution or repeated runs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1-fast)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated video assets are returned as dLazy-hosted URLs or downloaded files when the save option is used.]

## Skill Version(s):

1.3.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
