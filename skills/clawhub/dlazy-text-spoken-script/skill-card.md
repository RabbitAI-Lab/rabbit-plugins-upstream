## Description:

Guides agents in writing conversational, story-driven short-video spoken scripts with a seven-step structure.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketing teams use this skill to draft spoken scripts for short videos, personal stories, and viewpoint-led content. The artifact also includes an optional image-generation workflow using the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The script-writing skill also directs agents to install and run a networked image-generation CLI.

Mitigation: Use the CLI only if image generation is intended; otherwise use a script-only version or separate the image workflow.

Risk: The CLI stores an API key locally and sends prompts or media to dLazy services.

Mitigation: Review the service and data before use, protect or rotate credentials, and avoid sending sensitive prompts or media.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-text-spoken-script)
- [dLazy CLI repository (tool referenced by skill; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Paragraph-form spoken script in Markdown; optional image prompts, commands, and result links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Seven-step narrative structure; conversational language and concrete examples]

## Skill Version(s):

1.3.25 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
