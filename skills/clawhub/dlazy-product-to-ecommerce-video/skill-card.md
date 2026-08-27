## Description:

Turns product specs, manuals, catalogs, or Amazon, Shopify, eBay, and Temu listings into conversion-focused shopping video projects with multi-language voiceover and an optional virtual host through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce teams, sellers, marketers, and developers use this skill to start or continue dLazy product-to-video projects from product documents, catalogs, and marketplace listings. It is intended for product ads, TikTok Shop content, cross-border selling videos, and related ecommerce creative workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached product files may be sent to dLazy APIs and media storage.

Mitigation: Submit only materials that are appropriate to share with dLazy, and avoid confidential product assets unless that use is approved.

Risk: The skill requires a dLazy API key for authenticated requests.

Mitigation: Use the documented dLazy login or API-key flow, keep keys out of prompts and shared logs, and rotate or revoke keys from the dLazy dashboard if exposed.

Risk: A global CLI install persists a third-party executable on the user's system.

Mitigation: Use the pinned npx invocation when an on-demand CLI run is preferred over a persistent global install.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and CLI-streamed text responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May upload attached product files to dLazy media storage and continue project-scoped chat sessions through dLazy project IDs.]

## Skill Version(s):

1.3.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
