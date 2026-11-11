## Description:

Generates detailed short-video storyboard scripts from user-provided themes, structured copy, or outlines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and video producers use this skill to turn a theme, outline, or structured script into a shootable short-video storyboard while preserving the supplied copy verbatim.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment flags authentication and external CLI instructions as unrelated to the stated storyboard-script purpose, and notes a workflow that expands into cloud image generation.

Mitigation: Clarify the CLI authentication and external package behavior, and remove image-generation steps or make them a separate, explicitly chosen task before installation. The assessment notes that its scan was partial and the external package behavior remains unknown.

## Reference(s):

- [CLI project (linked in skill metadata; skill provenance unavailable)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown storyboard with global video parameters and structured shot sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Shot descriptions include scene, camera movement, notes, and shooting technique; spoken copy is distributed verbatim across shots.]

## Skill Version(s):

1.2.35 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
