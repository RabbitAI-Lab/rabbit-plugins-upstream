## Description:

Guides agents to write conversational, story-driven short-video spoken scripts using a seven-step structure.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketers use this skill to draft short-video spoken scripts from a speaker persona, audience pain point, or topic. The artifact also directs agents toward a separate image-generation workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact requires image generation and terminal commands even though the skill is advertised as a spoken-script writer.

Mitigation: For script writing alone, use a version without the image-generation and terminal-command sections; review each command before execution.

Risk: Using the dLazy CLI sends prompts and selected media to dLazy services.

Mitigation: Install only if this external workflow is intended, and avoid submitting sensitive prompts or media without authorization.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-text-spoken-script)
- [dLazy CLI documentation and source (linked in skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands]

**Output Format:** [Plain text with optional image-generation commands and image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Seven-step, spoken-style script; image-generation steps require user confirmation.]

## Skill Version(s):

1.3.31 (source: ClawHub release evidence; artifact frontmatter states 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
