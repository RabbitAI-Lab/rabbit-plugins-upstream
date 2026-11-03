## Description:

Turns product specifications, manuals, catalogs, or marketplace listings into conversion-focused shopping video projects with multilingual voiceover and an optional virtual host.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and marketing teams use this skill to create product advertising videos from product information or marketplace listings, including cross-border campaigns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files are sent to dLazy, and attached files are uploaded to its media storage.

Mitigation: Use the intended dLazy organization and project, and attach only material you are comfortable sharing with dLazy.

Risk: Authentication saves an API key locally, and video generation consumes account credits.

Mitigation: Protect the local CLI configuration, rotate or revoke the key if needed, and expect generation to use credits.

Risk: The external CLI executable and hosted service were not verified by this assessment.

Mitigation: Review the pinned CLI before installing it.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance, Video projects]

**Output Format:** [Markdown guidance and CLI commands; video generation is requested through the dLazy service.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; generation consumes account credits. Files attached to a request are uploaded to dLazy media storage.]

## Skill Version(s):

1.3.35 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
