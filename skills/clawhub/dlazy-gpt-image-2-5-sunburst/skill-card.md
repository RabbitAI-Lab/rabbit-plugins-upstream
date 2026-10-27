## Description:

An agent skill for generating and editing detailed images with GPT Image 2.5 Sunburst through dLazy, including work guided by reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can create or edit images from prompts, with optional reference images, when they need detailed compositions or legible in-image text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference images are sent to the third-party dLazy service for processing.

Mitigation: Only submit prompts and images that are appropriate to share with that service.

Risk: API use consumes dLazy credits, and authentication credentials may be stored locally.

Mitigation: Use the documented device-code login or an environment variable, review estimated cost with --dry-run, and revoke stored credentials when no longer needed.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Images, Files, Text]

**Output Format:** [Generated image assets, with CLI text reporting and result URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports prompt-based generation, up to five reference images, multiple aspect ratios including 21:9, and quality settings up to max.]

## Skill Version(s):

1.2.22 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
