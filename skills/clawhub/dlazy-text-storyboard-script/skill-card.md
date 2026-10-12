## Description:

Generates shot-by-shot short-video storyboard scripts from themes, outlines, or supplied copy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and production teams use the skill to turn themes or existing copy into short-video shot plans with scene directions, camera movements, and spoken lines. The skill also contains separate instructions for generating images through dLazy's cloud CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The text-only storyboard description conflicts with instructions to install and use cloud image generation.

Mitigation: Review the workflow before installing; use it only if dLazy image generation is intended.

Risk: dLazy login or API-key setup stores credentials locally, and prompts and parameters are sent to dLazy services.

Mitigation: Approve cloud processing and avoid sharing sensitive prompts or credentials unnecessarily.

Risk: Local media may be uploaded, and generated results may be hosted on dLazy URLs.

Mitigation: Check media permissions and data-handling requirements before submitting files or sharing result links.

## Reference(s):

- [dLazy CLI source (tool reference, not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Image URLs]

**Output Format:** [Markdown storyboard with video parameters and shot-by-shot descriptions; optional dLazy CLI commands and hosted image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Storyboard directions call for preserving supplied spoken copy verbatim; the separate image-generation workflow requires dLazy cloud access.]

## Skill Version(s):

1.2.24 (source: ClawHub release; embedded frontmatter: 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
