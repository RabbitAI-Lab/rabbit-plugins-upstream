## Description:

Text-to-vector model that outputs SVG results, suitable for logos, icons, and scalable design assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and designers use the skill to generate vector graphics such as logos, icons, and scalable design assets from text prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any supplied media are sent to dLazy, and generated assets are hosted by its service.

Mitigation: Send only prompts and media you are permitted to share with the service.

Risk: Authentication stores an API key in the local CLI configuration, and generation may consume account credits.

Mitigation: Use the device-code login, keep the local key private, and review costs before generating.

## Reference(s):

- [CLI project page listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image files, SVG vector graphics]

**Output Format:** [Generated vector graphic asset; the skill describes SVG output, while its example response shows an image URL with PNG MIME type.]

**Output Parameters:** [Prompt and optional aspect ratio]

**Other Properties Related to Output:** [Results are hosted by dLazy; generation can run asynchronously.]

## Skill Version(s):

1.3.33 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
