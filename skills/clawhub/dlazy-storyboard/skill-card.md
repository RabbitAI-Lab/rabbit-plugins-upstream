## Description:

Storyboard helps agents run a dLazy-hosted storyboard workflow for multi-shot animated shorts, including script, character and shot prompts, reference sheets, first and last frames, image-to-video shot generation, voice or TTS, music, sound effects, subtitles, and Remotion assembly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and creative teams use this skill to start or continue dLazy storyboard projects that turn multi-shot animation concepts into structured prompts, media generation steps, and assembled video outputs. It is best suited for animated shorts that need consistent characters across shots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, options, and selected attachments are sent to dLazy hosted services.

Mitigation: Avoid sending confidential or regulated data unless the user's organization has approved dLazy for that data.

Risk: Authentication stores a dLazy API key in local CLI configuration unless the user supplies it per invocation.

Mitigation: Use the per-run DLAZY_API_KEY environment variable or rotate and revoke stored keys from the dLazy dashboard when access changes.

Risk: The skill depends on a Node-based CLI distributed through npm or npx.

Mitigation: Use the pinned @dlazy/cli@1.2.3 install command from the release metadata and review the package before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-storyboard)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and terminal text with inline shell commands and project guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference hosted dLazy project outputs and uploaded media URLs when users attach files.]

## Skill Version(s):

1.3.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
