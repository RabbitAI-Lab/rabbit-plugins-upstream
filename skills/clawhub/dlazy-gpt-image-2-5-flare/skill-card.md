## Description:

Generates and edits images through dLazy's hosted GPT Image 2.5 Flare service, with reference-image, aspect-ratio, and quality options.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to generate images from prompts or edit images with reference inputs through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected images are sent to dLazy, and generation may spend service credits.

Mitigation: Only submit content you are authorized to share, review applicable service terms and costs, and use --dry-run to inspect the payload and estimate cost before generation.

Risk: The saved dLazy API key can authorize service use.

Mitigation: Protect the local key, review the pinned CLI before installation, and rotate or revoke the key if it is exposed.

## Reference(s):

- [dLazy CLI documentation](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [JSON results with generated image URLs and metadata; optionally a downloaded image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated assets are hosted by dLazy; asynchronous requests may return a task identifier before results are ready.]

## Skill Version(s):

1.2.22 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
