## Description:

Creates marketing and product-ad videos from product details, listings, or a brief through dLazy's hosted video service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketers and sellers use this skill to turn product specifications, catalogs, or online listings into promotional videos for social campaigns and e-commerce, with multilingual voiceover and an optional virtual host.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files are sent to dLazy's hosted service.

Mitigation: Share only material approved for upload to the service.

Risk: The CLI may store an API key locally.

Mitigation: Protect local credentials and rotate or revoke the key if exposed.

Risk: The skill installs and runs a third-party CLI.

Mitigation: Review the pinned CLI package and source before installation where dependency vetting is required.

Risk: Continuing an existing project may reuse prior conversation context.

Mitigation: Start a fresh project unless prior context is intentionally needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-marketing-video)
- [dLazy CLI source referenced by the skill](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Streamed text response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-based follow-ups; video generation is handled by the hosted service.]

## Skill Version(s):

1.0.27 (source: ClawHub release metadata; bundled skill frontmatter says 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
