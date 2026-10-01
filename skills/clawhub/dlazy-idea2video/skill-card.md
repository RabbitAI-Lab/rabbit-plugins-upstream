## Description:

Guides creators from an idea through a reviewed video-production plan, then expands the plan into canvas nodes for story, characters, scenes, shots, and final video assembly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and production teams use the skill to turn a video idea into a reviewable story-to-video workflow on a canvas, with character portraits, shot frames, generated clips, and a final merge.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow calls for terminal commands and installing a third-party CLI that stores an API key locally.

Mitigation: Review the CLI package before installation, use npx to avoid a persistent global install if preferred, and require explicit approval for each command.

Risk: Prompts and referenced media may be transmitted to dLazy's hosted generation service.

Mitigation: Use only content authorized for upload and confirm the service and data-handling terms before sending sensitive material.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-idea2video)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Configuration, Shell commands]

**Output Format:** [Markdown plan summaries and canvas workflow instructions, with optional CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user confirmation before advancing the plan or running generation commands; source-import provenance for this release is unavailable.]

## Skill Version(s):

1.3.26 (source: server-resolved ClawHub release metadata; bundled frontmatter says 1.3.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
