## Description:

Generates 2K, 3K, or 4K images from prompts and optional reference images using the dLazy-hosted Seedream 5.0 service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, creators, and developers use this skill to generate high-resolution visuals, posters, and print-ready artwork from text prompts and reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference files are sent to dLazy's hosted service.

Mitigation: Submit only prompts and files you are comfortable sharing with dLazy.

Risk: Authentication may save an API key on the local device.

Mitigation: Use the DLAZY_API_KEY environment variable if local credential persistence is undesirable.

Risk: Installing the CLI introduces third-party software, and generation may use paid credits.

Mitigation: Review the pinned CLI package before use, run it with npx to avoid a persistent global install, and check costs before generating images.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, Image URLs]

**Output Format:** [Markdown guidance and CLI JSON responses with generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images may be downloaded to a user-selected local path.]

## Skill Version(s):

1.2.21 (source: ClawHub release; artifact frontmatter and pinned CLI specify 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
