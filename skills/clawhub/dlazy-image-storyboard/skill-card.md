## Description:

Guides creators from a brief through approved character designs and panel scripts to cinematic or narrative storyboards, with image generation after confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and production teams use this skill to plan film, advertising, short-video, and educational storyboards, approve characters and scripts, and generate panels for a print-ready layout.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill calls a third-party CLI; its documentation disagrees about the pinned CLI version.

Mitigation: Review the CLI package and source before installing, and confirm the version used.

Risk: Login can persist an API key locally.

Mitigation: Use an environment-provided key when persistent storage is unwanted, and rotate or revoke keys as needed.

Risk: Prompts and supplied local media can be sent to dLazy cloud services.

Mitigation: Avoid private prompts and local media paths unless the upload is acceptable.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-image-storyboard)
- [dLazy CLI repository (referenced tool, not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Image URLs]

**Output Format:** [Markdown bullet lists with character specifications, per-panel scripts, generation commands, and image links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [User approval gates precede character, script, and image generation; final layouts target A4 landscape print or PDF export.]

## Skill Version(s):

1.3.31 (source: ClawHub release metadata; supplied skill frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
