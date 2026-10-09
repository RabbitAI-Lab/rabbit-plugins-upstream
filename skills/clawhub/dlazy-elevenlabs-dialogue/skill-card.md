## Description:

Guides agents in generating multi-voice ElevenLabs dialogue audio for character scenes, podcasts, and short skits using the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to prepare dialogue with distinct voices and expressive tags, then generate audio for podcasts, character scenes, or short skits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on an external CLI package.

Mitigation: Review @dlazy/cli before installing and use the pinned package version specified by the skill.

Risk: Prompts and any explicitly supplied media files are sent to dLazy services.

Mitigation: Avoid sharing sensitive content or files unless their upload is authorized.

Risk: Logging in saves the API key in local CLI configuration.

Mitigation: Use DLAZY_API_KEY per invocation when persistent local storage is not desired.

Risk: The skill's example command and sample output may not match its dialogue command options and audio result.

Mitigation: Confirm the actual flags and output with dlazy elevenlabs-dialogue -h before running it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-dialogue)
- [dLazy CLI repository (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package (skill metadata)](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked service returns a link to generated media; the CLI can also save the asset locally.]

## Skill Version(s):

1.3.25 (source: ClawHub release evidence; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
