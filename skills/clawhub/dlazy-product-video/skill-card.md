## Description:

Turns a product's photos, product link, specification, manual, or catalog into a polished ecommerce demo or ad video with multi-language voiceover and an optional virtual host.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and ecommerce teams use this skill to start or continue a dLazy hosted product-video workflow for product demos, shopping ads, and cross-border selling videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, options, and attached local files may be sent to dLazy hosted APIs and media storage.

Mitigation: Use the skill only with content approved for dLazy processing, and avoid attaching sensitive or regulated data unless the service is approved for that use.

Risk: Authentication can store a dLazy API key in the local CLI configuration.

Mitigation: Use OS-user-restricted config permissions, prefer per-invocation DLAZY_API_KEY when persistence is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Using the skill requires installing or running a third-party npm CLI.

Mitigation: Use the pinned @dlazy/cli@1.2.3 package, prefer npx for non-persistent execution, and review the referenced package or source before installing globally.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-product-video)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with inline shell commands and hosted service responses; generated video assets may be returned through the dLazy workflow.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx, a dLazy API key, and network access to api.dlazy.com; attached files may be uploaded to files.dlazy.com.]

## Skill Version(s):

1.0.8 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
