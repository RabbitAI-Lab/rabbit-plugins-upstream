## Description:

Creates multi-shot storyboard video projects with scripts, characters, shot prompts, reference sheets, first and last frames, image-to-video shots, voice, music, sound effects, subtitles, and Remotion rendering through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, developers, and agent users use this skill to start or continue dLazy storyboard projects for multi-shot animated shorts with consistent characters. It is suited for workflows that combine story development, shot planning, generated media, voice or audio, subtitles, and final video assembly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on the dLazy CLI and hosted dLazy service.

Mitigation: Install only if you are comfortable trusting the dLazy CLI and service; prefer the pinned npx command when you do not want a persistent global binary.

Risk: Local files attached with the CLI may be uploaded to dLazy media storage.

Mitigation: Attach only files you intend to upload to dLazy.

Risk: The workflow requires a dLazy API key saved locally or supplied at runtime.

Mitigation: Use a revocable API key with normal user-level permissions and rotate or revoke it when needed.

## Reference(s):

- [dLazy CLI source link from metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-storyboard)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key and the dLazy CLI; attached files may be uploaded to dLazy media storage during use.]

## Skill Version(s):

1.3.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
