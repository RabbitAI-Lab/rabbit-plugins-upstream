## Description:

Converts storyboard ideas into multi-shot animated video assets through the dLazy hosted storyboard service, including scripts, character and shot prompts, reference sheets, i2v shot videos, voice/TTS, music, SFX, subtitles, and Remotion rendering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to start or continue dLazy storyboard projects for multi-shot animated shorts with consistent characters, prompts, reference assets, audio, subtitles, and rendered video outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, options, and attached files are sent to dLazy's hosted API and media storage.

Mitigation: Use the skill only for data intended for dLazy, and do not attach secrets or private files unless upload is intentional.

Risk: The dLazy API key may be stored in a local CLI configuration file.

Mitigation: Prefer per-run DLAZY_API_KEY for non-persistent use, verify local config file permissions, and rotate or revoke keys if exposure is suspected.

Risk: The skill depends on installing or invoking the pinned @dlazy/cli package with npm or npx.

Mitigation: Use the pinned CLI version declared by the artifact and review the package or source before installing in sensitive environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-storyboard)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline shell commands and streamed service responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference generated media, uploaded files, project ids, authentication state, and dLazy service errors.]

## Skill Version(s):

1.3.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
