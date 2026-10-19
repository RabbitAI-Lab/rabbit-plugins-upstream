## Description:

Clones a voice from reference audio and generates speech for new text using Vidu Audio Clone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use reference audio and a text prompt to request voice-cloned speech through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference audio are sent to a third-party hosted service.

Mitigation: Use only content you are authorized to share and review the service's data handling before sending sensitive material.

Risk: Cloned voices could be used without a speaker's permission.

Mitigation: Obtain appropriate consent before cloning or publishing a person's voice.

Risk: The CLI can save an API key locally.

Mitigation: Use the per-invocation DLAZY_API_KEY option if you do not want the key saved on disk.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-vidu-audio-clone)
- [dLazy CLI repository (skill metadata link)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown with generation status and a link to the hosted result]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may return a task ID before the result is ready.]

## Skill Version(s):

1.3.31 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
