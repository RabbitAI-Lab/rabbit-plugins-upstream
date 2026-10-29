## Description:

Generates high-quality videos with Kling v3 from text prompts or reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use the skill to generate videos from text prompts or up to two reference images, with controls for aspect ratio, duration, mode, and sound.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are sent to dLazy-hosted services; local media may be uploaded for processing.

Mitigation: Avoid sending sensitive prompts or media unless approved, and provide only media cleared for external processing.

Risk: The skill requires a dLazy API key stored in local CLI configuration, and generation uses service credits.

Mitigation: Prefer device-code login, protect or rotate the key, and use the dry-run option to review the payload and estimated cost before generation.

## Reference(s):

- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Video files, JSON]

**Output Format:** [Video asset URL or saved video file, with JSON result metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return an asynchronous task ID before the generated video is ready.]

## Skill Version(s):

1.3.35 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
