## Description:

Creates narration, dialogue, podcasts, sound scenes, effects, and ambience through a user's Foleyix account and downloads the resulting private WAV audio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lvyinchao](https://clawhub.ai/user/lvyinchao)

### License/Terms of Use:

MIT-0

## Use Case:

Foleyix account holders use this skill to turn written sound descriptions or scripts into audio, check available quota and tasks, and retrieve completed WAV files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting an account exposes private audio tasks and uses the account's generation quota.

Mitigation: Have the user approve login in the browser, check quota before generation, and use logout to revoke the CLI connection when no longer needed.

Risk: Private login state could be disclosed if local configuration files are shared.

Mitigation: Keep private configuration files out of agent context and shared projects.

## Reference(s):

- [Foleyix skill homepage](https://foleyix.com/skill)
- [Foleyix audio creation guide](https://foleyix.com/instruction)
- [Foleyix CLI reference](artifact/references/cli.md)
- [Foleyix prompt-writing guide](artifact/references/prompt-writing.md)

## Skill Output:

**Output Type(s):** [Audio files, Text, Shell commands]

**Output Format:** [Private WAV audio files with text or JSON task and quota results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Audio generation uses the connected account's quota; completed results must be checked before delivery.]

## Skill Version(s):

1.1.0 (source: frontmatter, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
