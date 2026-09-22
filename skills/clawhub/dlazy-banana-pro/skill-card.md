## Description:

Generate/edit images with Nano Banana Pro, supporting text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to request image generation or editing through dLazy's hosted Nano Banana Pro service, using prompts and optional reference images. It is suited for agent workflows that need generated image URLs or saved image assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and provided image files are sent to dLazy's hosted service for generation or editing.

Mitigation: Use the skill only for content that is appropriate to send to dLazy, and avoid submitting confidential or regulated data unless that use is approved.

Risk: The dLazy CLI can save API keys in a local user configuration file.

Mitigation: Prefer per-invocation credentials or the documented npx path when avoiding persistent local configuration, and rotate or revoke API keys from the dLazy dashboard when needed.

Risk: Image generation requests may consume dLazy account credits.

Mitigation: Use the CLI dry-run or cost-estimate path when planning usage, and confirm account credit availability before long-running generation work.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-banana-pro)
- [dLazy publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked CLI may return hosted image URLs, async task identifiers, or save generated image assets to a requested local path.]

## Skill Version(s):

1.2.21 (source: server release metadata; artifact frontmatter reports 1.2.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
