## Description:

Turns a video idea into a reviewable production plan, then lays out story, character, scene, shot, and video-generation steps on a canvas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and production teams use this skill to turn an idea into a confirmed video-production plan and an executable canvas workflow for generating scenes and shots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill mixes canvas planning with instructions to execute dLazy terminal commands.

Mitigation: Review every proposed terminal command before execution and prefer the canvas workflow unless CLI execution is explicitly wanted.

Risk: Cloud generation can send prompts and local media to dLazy.

Mitigation: Share only material approved for upload and review dLazy's data-handling terms before use.

Risk: Using the global or npx dLazy CLI requires trusting the package and storing an API key.

Mitigation: Review the package before installation, protect the API key, and rotate it if exposed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-idea2video)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Canvas configuration, Shell commands]

**Output Format:** [Conversational Markdown plan summaries, structured plan data, and canvas workflow shapes; optional CLI commands for generation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The plan requires user confirmation before canvas expansion; running the canvas workflow generates media. Release version 1.3.33 differs from bundled skill frontmatter version 1.3.9.]

## Skill Version(s):

1.3.33 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
