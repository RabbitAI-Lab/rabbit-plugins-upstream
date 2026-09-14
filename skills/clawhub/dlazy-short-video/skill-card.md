## Description:

短视频生成 Short Video helps agents use the dLazy short-video template to produce 15-25 second vertical videos with storyboard, first frames, image-to-video clips, TTS voiceover, Remotion assembly, and burned-in subtitles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate social-platform vertical short videos through the dLazy CLI and hosted service, optionally continuing project sessions and attaching reference files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on the external dLazy npm CLI and hosted dLazy service.

Mitigation: Use the pinned CLI version, prefer npx for one-off execution, and install only after deciding that the dLazy CLI and service are trusted for the task.

Risk: Running npm globally can leave a persistent executable on the system.

Mitigation: Use npx instead of a global install when a persistent binary is not needed, and avoid running npm with administrator privileges.

Risk: Files attached to the CLI may be uploaded to dLazy media storage.

Mitigation: Attach only files intended for upload and avoid including sensitive local data unless sharing it with dLazy is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-short-video)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, shell commands, files, guidance]

**Output Format:** [Markdown with inline bash code blocks, CLI output text, and generated vertical MP4 deliverables from the hosted service]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; local files attached with the CLI may be uploaded to dLazy media storage.]

## Skill Version(s):

1.2.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
