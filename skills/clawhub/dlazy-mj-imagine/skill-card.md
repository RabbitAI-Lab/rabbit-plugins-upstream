## Description:

Generates stylized images through dLazy's hosted service with selectable aspect ratio, bot type, and grid or upscale output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request stylized images, choose an aspect ratio and bot type, and receive a grid or selected upscale.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media are sent to dLazy's hosted service, and generated files are hosted on dLazy storage.

Mitigation: Only submit prompts and local files you intend to share with dLazy.

Risk: Authentication may save an API key in the local CLI configuration.

Mitigation: Protect the local configuration and rotate or revoke the key if it is exposed.

Risk: Installing a third-party CLI grants it execution access on the user's machine.

Mitigation: Review the CLI before installing; use the pinned npx @dlazy/cli@1.2.3 option to avoid a persistent global install.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-mj-imagine)
- [dLazy CLI repository (listed in skill metadata; import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Image URLs]

**Output Format:** [Text guidance and JSON CLI results with hosted image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return an asynchronous task ID or save a generated image locally.]

## Skill Version(s):

1.3.21 (source: server-resolved ClawHub release; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
