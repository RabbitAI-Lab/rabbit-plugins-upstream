## Description:

Creates storyboards for multi-shot animated shorts, including scripts, character and shot prompts, reference images, video shots, voice, music, sound effects, subtitles, and final assembly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to plan and produce a multi-shot animated short with consistent characters. It guides the dLazy storyboard agent through scripting, shot creation, media generation, and final rendering.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment has medium confidence and only partial analysis, so it may not identify every issue in the CLI package or skill content.

Mitigation: Before installing, review the CLI package and login flow, and inspect the padded section of the Chinese skill document as the security guidance recommends.

Risk: Prompts are sent to dLazy's API, and attached local files are uploaded to its media storage.

Mitigation: Avoid sending sensitive material unless that data sharing is appropriate; review the CLI behavior and dLazy service terms before use.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)
- [API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Video and audio files]

**Output Format:** [Markdown guidance and CLI commands; generated storyboard and media assets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a project-scoped hosted agent; attached local files are uploaded for use as media references.]

## Skill Version(s):

1.3.43 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
