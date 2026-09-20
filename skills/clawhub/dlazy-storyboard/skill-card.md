## Description:

分镜脚本 Storyboard helps agents use the dLazy storyboard template to create multi-shot animated shorts with scripts, character and shot prompts, reference sheets, first and last frames, shot videos, voice, music, sound effects, subtitles, and Remotion assembly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, developers, and agents use this skill to start or continue dLazy storyboard projects for multi-shot animated shorts with consistent characters. It routes prompts and optional attachments through the dLazy CLI and hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected attachments are sent to dLazy, and attached files are uploaded to dLazy storage.

Mitigation: Attach only files intended for upload and avoid sending sensitive content unless it is approved for dLazy processing.

Risk: The CLI may save a dLazy API key under the user's profile.

Mitigation: Use OS user account protections, prefer per-invocation DLAZY_API_KEY when appropriate, and rotate or revoke the key from the dLazy dashboard when needed.

Risk: A global install persists the dLazy CLI on the system.

Mitigation: Use the pinned npx command when a temporary invocation is preferred.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-storyboard)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return project-scoped chat guidance and dLazy CLI commands; generated media is produced by the external dLazy service.]

## Skill Version(s):

1.3.18 (source: server release metadata; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
