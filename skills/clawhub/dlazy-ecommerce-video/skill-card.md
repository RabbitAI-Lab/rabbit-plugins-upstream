## Description:

Turns product photos, product documents, catalogs, or ecommerce listing links into conversion-focused shopping ad videos with multi-language voiceover and an optional virtual host.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create ecommerce product videos for stores, marketplaces, TikTok Shop, and advertising workflows from product media or listing links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected uploaded files are sent to dLazy hosted services.

Mitigation: Avoid attaching sensitive product files unless the user accepts dLazy's service terms and data handling.

Risk: The dLazy CLI may store an API key in the local user configuration.

Mitigation: Use environment-scoped keys when appropriate, rotate or revoke keys from the dLazy dashboard, and prefer npx when a persistent global install is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-ecommerce-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and streamed hosted-service responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference hosted video-generation project state and uploaded product files managed by the dLazy CLI.]

## Skill Version(s):

1.0.16 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
