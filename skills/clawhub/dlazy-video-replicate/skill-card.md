## Description:

Video replicate tool: extracts the first frame and audio from the source video, runs video understanding for a prompt, and returns a Seedance 2.0 replicate bundle (first frame + audio + video).

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to call the dLazy video-replicate CLI for generating a Seedance 2.0 replication bundle from a source video, including the first frame, audio, and generated video output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill invokes third-party dLazy CLI software and calls dLazy-hosted services.

Mitigation: Review the pinned dLazy CLI package before installing or invoking it.

Risk: Prompts and selected video, audio, or image files are sent to dLazy-hosted services for processing.

Mitigation: Use only media and prompts approved for third-party hosted processing.

Risk: The dLazy API key may be stored in ~/.dlazy/config.json.

Mitigation: Treat the stored API key as sensitive, rotate or revoke it when needed, or use DLAZY_API_KEY per invocation to avoid persisting credentials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-replicate)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown instructions with bash commands and JSON CLI responses containing generated media URLs or async task status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save generated result assets to a local path when the CLI --save option is used.]

## Skill Version(s):

1.3.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
