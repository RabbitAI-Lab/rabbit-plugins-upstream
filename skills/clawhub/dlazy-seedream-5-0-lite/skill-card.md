## Description:

Generates images from text prompts or reference images using Doubao Seedream 5.0 Lite.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to generate images from text prompts or reference images through dLazy's hosted Doubao Seedream 5.0 Lite service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected images are sent to dLazy; local image files provided as inputs are uploaded to its media storage.

Mitigation: Submit only prompts and images you intend to share with the hosted service.

Risk: The CLI saves an API key in the user's local configuration, and generation consumes account credits.

Mitigation: Protect the saved key and rotate or revoke it if exposed; use the CLI dry-run option to review the estimated cost before generation.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [CLI homepage listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)
- [dLazy credits dashboard](https://dlazy.com/dashboard/organization/settings?tab=credits)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [Image files with a JSON result envelope]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return image URLs or an asynchronous task identifier; generated images are hosted by dLazy.]

## Skill Version(s):

1.3.35 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
