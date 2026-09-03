## Description:

Creates multi-shot animated short storyboard and video assets, including scripts, character and shot prompts, reference sheets, first and last frames, shot videos, voice/TTS, music, SFX, subtitles, and Remotion-rendered output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to start or continue dLazy storyboard projects for multi-shot animated shorts with consistent characters, uploaded references, and generated audio, subtitle, and video assembly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and user-selected file attachments are sent to dLazy's hosted service.

Mitigation: Use the skill only with content intended for upload, and review organizational data-sharing requirements before attaching files.

Risk: The dLazy API key is stored in local CLI configuration unless supplied per invocation.

Mitigation: Check permissions on ~/.dlazy/config.json on shared systems, rotate or revoke keys when needed, or use DLAZY_API_KEY per invocation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-storyboard)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and terminal command guidance for invoking the dLazy CLI and interpreting responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference generated storyboard, video, audio, subtitle, or project outputs produced by the hosted dLazy workflow.]

## Skill Version(s):

1.3.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
