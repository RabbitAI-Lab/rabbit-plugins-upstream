## Description:

Helps create promotional shopping videos from product details, listings, or a marketing brief using dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketers and ecommerce sellers use this skill to request product advertising videos for social media and sales campaigns, then refine them through follow-up project conversations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached product files are sent to dLazy services.

Mitigation: Review the service and its terms before use, and avoid sharing sensitive materials without authorization.

Risk: An API key is saved in local CLI configuration.

Mitigation: Treat the saved key as sensitive and rotate or revoke it if exposed.

Risk: Project conversations retain context across requests.

Mitigation: Use a fresh project or clear the session when changing contexts or handling sensitive product materials.

## Reference(s):

- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Streaming CLI text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-scoped conversations support follow-up requests; attached files are uploaded to dLazy before use.]

## Skill Version(s):

1.0.18 (source: ClawHub release metadata; skill document frontmatter says 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
