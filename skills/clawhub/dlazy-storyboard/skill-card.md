## Description:

Turns a storyboard into a multi-shot animated video with consistent characters, shot prompts, generated visuals, audio, subtitles, and final assembly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to develop multi-shot animated shorts with consistent characters, from story and shot planning through generated media and rendering.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files are sent to dLazy cloud services for processing.

Mitigation: Only provide material you want processed by the service.

Risk: Login stores an organization API key in the local CLI configuration, and project context can persist between sessions.

Mitigation: Revoke the key when it is no longer needed and clear saved project sessions when their context should be removed.

Risk: Media generation can consume organization credits.

Mitigation: Review expected generation use and available credits before starting larger jobs.

## Reference(s):

- [dLazy CLI project](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-storyboard)

## Skill Output:

**Output Type(s):** [Text, Images, Video, Audio, Subtitles]

**Output Format:** [Chat text and generated media files, assembled into a rendered animated video.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-scoped sessions can retain context for follow-up work.]

## Skill Version(s):

1.3.35 (source: server release metadata; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
