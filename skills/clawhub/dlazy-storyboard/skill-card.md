## Description:

Creates storyboard-to-video workflows for multi-shot animated shorts, covering scripts, character and shot prompts, reference sheets, first and last frames, image-to-video shots, voice/TTS, music, sound effects, subtitles, and Remotion rendering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, and developers use this skill to run or continue dLazy storyboard projects for multi-shot animated shorts with consistent characters, generated shot assets, audio elements, subtitles, and final video assembly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, selected project context, and files attached with --files are handled by the external dLazy service.

Mitigation: Only attach files approved for upload to dLazy, and avoid including secrets or sensitive material in prompts or project context.

Risk: The skill relies on an npm-distributed CLI and a local dLazy API key configuration.

Mitigation: Review the CLI source or package before installation, prefer npx for non-persistent use when appropriate, and rotate or revoke dLazy API keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-storyboard)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and terminal text with shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include prompts and commands that invoke the external dLazy CLI and SaaS workflow.]

## Skill Version(s):

1.3.15 (source: server release metadata; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
