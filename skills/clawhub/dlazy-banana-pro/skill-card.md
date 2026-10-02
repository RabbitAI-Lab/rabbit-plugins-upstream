## Description:

Helps agents generate and edit images with Nano Banana Pro through dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate images from prompts or edit images using reference images, then receive links to the results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied image files may be sent to dLazy's hosted service, and generated images may be hosted there.

Mitigation: Share only prompts and files you are comfortable sending to dLazy; review hosted results before sharing them.

Risk: The CLI stores an API key locally and access to that key could permit account use.

Mitigation: Protect the key and rotate or revoke it from the dLazy dashboard if needed.

Risk: API use may consume account credits, and a global CLI install persists on the system.

Mitigation: Check the cost estimate with dry-run before generating; use the pinned npx command for one-off use if preferred.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-banana-pro)
- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Image links]

**Output Format:** [Text guidance and shell commands; JSON responses containing generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Images can optionally be saved locally; the skill specifies dLazy CLI version 1.2.3.]

## Skill Version(s):

1.2.27 (source: ClawHub release metadata; artifact frontmatter says 1.2.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
