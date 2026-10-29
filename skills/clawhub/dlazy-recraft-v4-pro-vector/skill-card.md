## Description:

Generates high-fidelity text-to-vector illustrations from prompts for production-ready visual assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers and developers use this skill to generate detailed vector-style illustrations from text prompts, with an optional aspect ratio. The generated image can be saved locally or returned as a hosted result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media files are sent to dLazy's hosted services, and generated results are hosted there.

Mitigation: Send only prompts and files you are comfortable sharing with the service, especially when working with sensitive material.

Risk: API credentials are stored in the local CLI configuration, and generation may incur costs.

Mitigation: Prefer device login over sharing keys in chat, remove or revoke keys when no longer needed, and consider the generation cost before submitting requests.

Risk: The documented installation runs a pinned third-party CLI package.

Mitigation: Review the pinned CLI before installing it.

## Reference(s):

- [CLI project page](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)
- [API key setup](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [JSON result containing generated image URLs (PNG in the documented example) and, for asynchronous requests, task status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results are hosted on files.dlazy.com and can be saved to a local path.]

## Skill Version(s):

1.3.34 (source: server-resolved release metadata; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
