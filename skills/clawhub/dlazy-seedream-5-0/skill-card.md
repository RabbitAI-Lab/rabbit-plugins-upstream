## Description:

Generates 2K, 3K, or 4K images from text prompts and reference images for posters, key visuals, and large-format print.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and design teams use this skill to generate or revise high-resolution images from prompts and optional reference images for posters, key visuals, and print.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly supplied local media are sent to dLazy's hosted service; generated results are hosted there.

Mitigation: Only submit content you are comfortable sharing with dLazy; review hosted-service terms before use.

Risk: The CLI can store an API key locally.

Mitigation: Protect local credentials and rotate or revoke the key from the dLazy dashboard when needed.

Risk: Image-generation requests can consume paid credits, and global CLI installation persists locally.

Mitigation: Review cost estimates with dry-run before generating and use npx instead of a global installation if persistence is unwanted.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0)
- [dLazy CLI homepage (release metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Text and JSON result with hosted image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports optional reference images, 2K/3K/4K resolution, asynchronous generation, and saving returned images locally.]

## Skill Version(s):

1.2.28 (source: server release; bundled skill and CLI install specify 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
