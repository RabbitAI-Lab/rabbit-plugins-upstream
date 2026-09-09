## Description:

Turns product photos, product links, specs, manuals, or catalogs into conversion-focused ecommerce ad videos with multilingual voiceover and an optional virtual host.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask the dLazy hosted ecommerce-video agent to generate shopping, store, TikTok Shop, or advertising videos from product images, links, or supporting product files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts, options, and attached product files to dLazy's hosted API and media storage.

Mitigation: Attach only files that are appropriate to upload to dLazy and review the service before using it with sensitive product data.

Risk: A globally installed CLI persists a local executable and stores API configuration on the user's machine.

Mitigation: Use `npx @dlazy/cli@1.2.3` for on-demand execution when a persistent global binary is unnecessary, and rotate or revoke the API key when access is no longer needed.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-ecommerce-video)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and service response text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference generated ecommerce video projects and uploaded product files through the dLazy hosted service.]

## Skill Version(s):

1.0.12 (source: server release metadata; artifact frontmatter lists 1.0.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
