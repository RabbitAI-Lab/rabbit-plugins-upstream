## Description:

Guides agents to write seven-part spoken scripts for short videos, while also directing dLazy CLI-based image generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketers use this skill to draft conversational, story-driven short-video scripts from a persona, topic, and audience pain points.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The spoken-script skill also directs installation and execution of an image-generation CLI unrelated to writing scripts.

Mitigation: Use only after reviewing the mismatch; remove image-generation and terminal-execution directions for a script-only workflow.

Risk: Using the dLazy CLI requires a locally stored API key and can send prompts or referenced media to dLazy services.

Mitigation: Install the CLI only if intended, protect the API key, and review prompts and media before submitting them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-text-spoken-script)
- [dLazy CLI source referenced by skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown prose with optional CLI commands and image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Seven-part, conversational script; image workflow requests confirmation before each generation.]

## Skill Version(s):

1.3.28 (source: ClawHub release metadata; skill frontmatter lists 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
