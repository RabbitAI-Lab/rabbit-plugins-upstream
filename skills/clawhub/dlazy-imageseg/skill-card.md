## Description:

Separates a subject from an image background and returns a URL for the transparent result.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to remove image backgrounds for product photos, portraits, and composites.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Provided images may be uploaded to dLazy's hosted service.

Mitigation: Avoid submitting sensitive images without approving that transfer.

Risk: CLI login may persist an API key in local configuration.

Mitigation: Use DLAZY_API_KEY for per-invocation credentials when persistent storage is unwanted.

Risk: The example uses --prompt although the documented image option is --image.

Mitigation: Check dlazy imageseg -h and provide the input with --image.

## Reference(s):

- [dLazy CLI source (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Image URL]

**Output Format:** [JSON response containing a hosted transparent-image URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may return a task ID instead; --save can download the image.]

## Skill Version(s):

1.3.23 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
