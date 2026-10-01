## Description:

Turns product documents or ecommerce listings into shopping-video projects with multilingual voiceover and an optional virtual host through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants and marketing teams use this skill to create product ads and cross-border shopping videos from product specifications, catalogs, or ecommerce listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached local files are sent to the third-party dLazy service.

Mitigation: Review content before submission and attach only files you are comfortable sharing with dLazy.

Risk: Authentication requires a dLazy API key, which can be saved in local CLI configuration.

Mitigation: Use a per-run DLAZY_API_KEY if you prefer not to save the key, and rotate or revoke it if exposed.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance, Video]

**Output Format:** [Streamed plain-text responses; video file format unspecified]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports project-based follow-up and optional local-file attachments.]

## Skill Version(s):

1.3.21 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
