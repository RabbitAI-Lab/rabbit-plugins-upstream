## Description:

Create marketing, promotional, or advertising videos from a product, brand, or brief.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers and ecommerce sellers can turn product information, listings, or a campaign brief into shopping and promotional videos. The workflow supports multilingual voiceover and an optional virtual host.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts are sent to dLazy, and files attached to a request are uploaded to its media storage.

Mitigation: Use an organization you intend to authorize and attach only files you want uploaded.

Risk: The CLI saves a reusable API key, and video generation may incur charges.

Mitigation: Protect the key in your user configuration, rotate or revoke it when needed, and account for generation charges.

Risk: The external CLI package and hosted service were not fully verified in the release security review.

Mitigation: Review the pinned CLI package and dLazy service terms before installing or sending sensitive information.

## Reference(s):

- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video, Text, Guidance]

**Output Format:** [Marketing video assets with text responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include multilingual voiceover and an optional virtual host; media file formats are not specified.]

## Skill Version(s):

1.0.33 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
