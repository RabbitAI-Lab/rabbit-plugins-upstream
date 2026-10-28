## Description:

Guides an agent to write colloquial, story-driven short-video spoken scripts using a seven-step structure.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and social media teams use the skill to draft short-video spoken scripts, character stories, and personal-brand viewpoints. It structures each script around a hook, audience resonance, a concrete story, a central viewpoint, and a memorable ending.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scriptwriting skill redirects requests into an unrelated cloud image-generation workflow, which may require CLI setup and cloud processing.

Mitigation: For scriptwriting alone, use a text-only skill or remove the mandatory image workflow. If image generation is needed, separately authorize CLI setup and cloud processing, review the exact package version and provider costs, and submit only content intended to be shared with dLazy.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-text-spoken-script)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Colloquial spoken-script prose in Markdown paragraphs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a seven-step narrative structure; specific persona, audience pain point, or topic is supplied by the user.]

## Skill Version(s):

1.3.36 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
