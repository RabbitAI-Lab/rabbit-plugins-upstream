## Description:

Helps agents generate or edit images with Vidu Q2 from text prompts and optional reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users create or edit Vidu Q2 images using text prompts and optional reference images through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied images or media are sent to dLazy's hosted service.

Mitigation: Send only content you are comfortable sharing with dLazy; review inputs before invoking the skill.

Risk: Authentication may save an API key locally, and generation consumes dLazy credits.

Mitigation: Use a per-invocation key if local storage is undesirable, and check the cost estimate before submitting.

Risk: Broad image-generation phrases may trigger the skill unexpectedly; it relies on an installed CLI.

Mitigation: Invoke it explicitly for Vidu Q2 or dLazy requests, and review the pinned CLI before installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-t2i)
- [dLazy CLI source (linked in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown instructions and CLI examples; image-generation results return JSON with image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return an asynchronous task ID; generated images can be saved locally.]

## Skill Version(s):

1.3.27 (source: ClawHub release metadata; skill files state 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
