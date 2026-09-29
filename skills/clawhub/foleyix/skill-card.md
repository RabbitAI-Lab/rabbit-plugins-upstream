## Description:

Generates narration, dialogue, sound scenes, effects, and ambience through a user's Foleyix account and downloads the resulting WAV audio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lvyinchao](https://clawhub.ai/user/lvyinchao)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents use their Foleyix account to create synthetic narration, dialogue, sound scenes, effects, or ambience, check generation status and quota, and download private WAV results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audio generation uses the connected account's quota.

Mitigation: Check available quota and confirm the prompt before starting a generation request; do not replace an unknown task automatically.

Risk: Login state and downloaded audio are private account data.

Mitigation: Keep the local Foleyix configuration directory private, review output paths, and log out to revoke the CLI connection when no longer needed.

## Reference(s):

- [Foleyix skill page](https://clawhub.ai/lvyinchao/skills/foleyix)
- [Foleyix skill documentation](https://foleyix.com/skill)
- [Foleyix CLI reference](references/cli.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Audio files]

**Output Format:** [CLI JSON responses and downloaded WAV files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation results include task status and an absolute output path when a WAV download succeeds.]

## Skill Version(s):

1.0.1 (source: frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
