## Description:

Professional tier of Seedream 5.0, stronger on fine detail, typography and complex composition. Suited to commercial key visuals and demanding brand assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can create Seedream 5.0 Pro images from text prompts, with optional reference images, for detailed commercial visuals and brand assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local reference images are sent to dLazy hosted services, and local reference files are uploaded for processing.

Mitigation: Submit only prompts and images you intend to share with dLazy, and review the service terms.

Risk: The dLazy CLI stores an API key in the local user configuration when using its login flow.

Mitigation: Protect the CLI configuration, or pass the key through DLAZY_API_KEY when appropriate; rotate or revoke exposed keys.

Risk: Image generation can incur usage costs.

Mitigation: Use --dry-run to review the payload and cost estimate before submitting a generation request.

## Reference(s):

- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [JSON response with generated image URLs and metadata; optional image files saved locally]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image generation supports prompts and up to 10 reference images; output URLs are hosted by dLazy.]

## Skill Version(s):

1.2.32 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
