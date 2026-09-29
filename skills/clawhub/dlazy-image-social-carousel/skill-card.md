## Description:

Guides social-media carousel design through a single direction confirmation, cover approval, and generation of matching slides.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketers use this skill to plan platform-specific social carousels, approve a cover design, and generate a consistent set of slides through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced media may be sent to dLazy services, where generated images are hosted.

Mitigation: Avoid sending confidential content without approval; review dLazy's data handling before use.

Risk: The dLazy API key may be stored in ~/.dlazy/config.json.

Mitigation: Use DLAZY_API_KEY per run when local storage is unsuitable, and rotate or revoke keys when needed.

Risk: The bundled skill version differs from the ClawHub release version, and CLI installation instructions name a separate version.

Mitigation: Review the linked CLI package and source, and confirm the intended version before installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-image-social-carousel)
- [dLazy CLI source (skill metadata link; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Shell commands, Image URLs]

**Output Format:** [Markdown with slide plans, approval prompts, CLI commands, and links to generated images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Images are generated and hosted by dLazy services.]

## Skill Version(s):

1.3.23 (source: ClawHub release; bundled skill frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
