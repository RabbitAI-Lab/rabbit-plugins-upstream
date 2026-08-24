## Description:

Audio generation skill that selects an appropriate dLazy CLI audio or TTS model for prompts, including text-to-speech, music, sound effects, voice cloning, and dialogue audio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users use this skill to route audio-generation requests to dLazy CLI models for TTS, music, sound effects, dialogue, and voice cloning. The skill is suited for agents that need concise model selection guidance, authentication setup, and executable shell commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and local media paths provided to the CLI may be sent to dLazy services for generation or media hosting.

Mitigation: Use the skill only for content approved for dLazy processing, avoid sensitive media unless permitted, and review requested inputs before execution.

Risk: The CLI stores or reads a dLazy API key and generated requests may consume paid account credits.

Mitigation: Prefer per-invocation credentials or npx when appropriate, monitor credit usage, and rotate or revoke the API key from the dLazy dashboard when access changes.

Risk: A persistent global CLI install increases local dependency surface area.

Mitigation: Use the pinned npx invocation when a persistent global install is not needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-audio-generate)
- [dLazy CLI Source](https://github.com/dlazyai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands; dLazy CLI invocations return JSON envelopes with generated media URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a pinned dLazy CLI install specification and may produce hosted audio or media URLs through the CLI.]

## Skill Version(s):

1.3.10 (source: server release evidence; artifact frontmatter reports 1.3.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
