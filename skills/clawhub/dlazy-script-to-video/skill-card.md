## Description:

Turns a script into a storyboarded, shot-by-shot video by generating scenes, assembling the shots, and checking the result.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to turn scripts into multi-shot animated videos with consistent characters, narration, music, and subtitles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Attached local files are uploaded to the dLazy service.

Mitigation: Attach only files you are comfortable uploading to dLazy.

Risk: The dLazy CLI may save an API key locally after login.

Mitigation: Use DLAZY_API_KEY per run if you do not want a saved local key.

Risk: Project sessions retain context for later conversations.

Mitigation: Avoid including sensitive material in sessions unless retention is acceptable.

Risk: Using the skill requires installing a third-party CLI package.

Mitigation: Review the dLazy CLI package before installing it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-script-to-video)
- [dLazy CLI homepage listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package listed in skill metadata](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Video generation guidance]

**Output Format:** [Streaming terminal text and project-based video generation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project sessions support follow-up requests; optional reference files are uploaded to dLazy.]

## Skill Version(s):

1.0.24 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
