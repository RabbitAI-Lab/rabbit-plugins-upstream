## Description:

Turns product photos, links, specs, manuals, or catalog material into conversion-focused ecommerce ad videos with multi-language voiceover and an optional virtual host.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, ecommerce operators, and marketing teams use this skill to create product, store, TikTok Shop, marketplace, and shopping ad videos from product images, links, or reference materials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on a third-party CLI and hosted SaaS service for ecommerce video generation.

Mitigation: Review the dLazy CLI source or npm package before installation when strict supply-chain controls apply; prefer npx or an isolated environment if a global CLI is not desired.

Risk: Files attached through the CLI can be uploaded to dLazy media storage.

Mitigation: Attach only files intended for processing by dLazy's service and avoid sensitive inputs unless the user's organization permits that data handling.

Risk: The skill requires a dLazy API key stored in local configuration or supplied through an environment variable.

Mitigation: Use OS-user-restricted configuration, rotate or revoke organization API keys when needed, and avoid exposing keys in prompts or shared logs.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-ecommerce-video)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands and streamed CLI text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May depend on an authenticated dLazy CLI session and may reference uploaded user-provided files.]

## Skill Version(s):

1.0.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
