## Description:

Use when someone wants a montage with transitions between shots - action-sequence reel or multi-scene piece where narration is optional.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to plan, generate, review, and assemble visual transition reels from hero imagery, start and end stills, paired image-to-video clips, and optional background music.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can upload supplied or generated images to provider file and video APIs.

Mitigation: Review dependent skills and provide only media that is acceptable to send to those services.

Risk: The workflow can spend generation credits after approval gates.

Mitigation: Require plan, stills, and clips approval before paid video generation or assembly steps.

Risk: The workflow may install additional Pruna skills as dependencies.

Mitigation: Review the dependent skills before installation and deployment.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/pruna-ai/skills/visual-transition-reel)
- [Example prompt](artifact/example-prompt.md)
- [Transition plan template](artifact/templates/transition-plan.template.json)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, shell commands, guidance]

**Output Format:** [Markdown guidance with JSON plan templates and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides phased generation of stills, video clips, review gates, ffmpeg assembly, and a final scene manifest.]

## Skill Version(s):

1.0.10 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
