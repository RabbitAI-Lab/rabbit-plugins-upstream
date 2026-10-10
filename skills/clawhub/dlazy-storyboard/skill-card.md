## Description:

Helps creators turn storyboards into multi-shot animated shorts with consistent characters, generated visuals, audio, subtitles, and assembled video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to plan and generate multi-shot animated shorts, including character references, shot visuals, audio, subtitles, and video assembly through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files are sent to dLazy's service.

Mitigation: Attach only files you intend to upload and review sensitive content before sending.

Risk: The skill requires a dLazy API key stored locally or supplied for each run.

Mitigation: Protect the key and rotate or revoke it from the dLazy dashboard when needed.

Risk: Running the pinned npm CLI executes third-party software.

Mitigation: Review the CLI before running it; use the pinned npx option to avoid a persistent global install.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-storyboard)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Conversational text with CLI commands and generated project results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May provide project-linked storyboard, media, and rendered video results through dLazy.]

## Skill Version(s):

1.3.27 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
