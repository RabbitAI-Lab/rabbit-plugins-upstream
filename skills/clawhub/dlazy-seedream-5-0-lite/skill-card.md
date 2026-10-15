## Description:

Helps agents generate images from text prompts or reference images using dLazy's Seedream 5.0 Lite service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request text-to-image or image-to-image generation and retrieve the resulting images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected input images may be sent to dLazy, and generated images are hosted by dLazy.

Mitigation: Only submit content you are comfortable sharing with dLazy, and review its service terms before use.

Risk: Logging in can save an API key locally.

Mitigation: Protect the local key and rotate or revoke it through dLazy when no longer needed.

Risk: A global CLI installation persists beyond one use.

Mitigation: For one-off use, prefer the pinned npx command or review the pinned npm package before installing globally.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-lite)
- [dLazy CLI repository (linked in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The service returns hosted image URLs; the CLI can optionally save images locally.]

## Skill Version(s):

1.3.29 (source: server-resolved ClawHub release; bundled skill frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
