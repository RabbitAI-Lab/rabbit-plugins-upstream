## Description:

marketing video, promo video, ad video, brand video — create a marketing / promo video from a product, brand, or brief. Use when the user wants a marketing, promotional, or advertising video for social or campaigns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, brands, and marketing teams can turn product details, marketplace listings, or a campaign brief into conversion-focused shopping and promotional videos. The workflow supports multilingual voiceover and an optional virtual host.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and options are sent to dLazy's hosted API, and files attached to a task are uploaded to its media storage.

Mitigation: Avoid including sensitive information in prompts or attachments, and review files before uploading them.

Risk: The CLI uses an organization-scoped API key and can list projects in that organization.

Mitigation: Protect the local CLI configuration, use the intended organization account, and rotate or revoke the key if it may have been exposed.

## Reference(s):

- [dLazy website](https://dlazy.com)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [CLI repository link listed in skill metadata](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Video, Text]

**Output Format:** [Marketing video assets with streamed text responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include multilingual voiceover and an optional virtual host.]

## Skill Version(s):

1.0.36 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
