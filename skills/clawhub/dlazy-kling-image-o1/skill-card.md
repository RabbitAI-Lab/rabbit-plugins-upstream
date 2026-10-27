## Description:

Generate images with the Kling Image O1 model from text prompts or reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate or edit images with Kling Image O1 from text prompts and reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference files are sent to dLazy-hosted services, and local reference files may be uploaded.

Mitigation: Use this skill only with prompts and files you intend to share with the service; follow any local-only or alternative-model preference.

Risk: Authentication stores a service API key in the local CLI configuration, and generation consumes service credits.

Mitigation: Protect the local configuration and API key, and review expected credit use before generating images.

## Reference(s):

- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kling-image-o1)

## Skill Output:

**Output Type(s):** [Images, API Calls, JSON]

**Output Format:** [Generated image assets returned as hosted URLs in a JSON response; images can optionally be saved locally.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image generation can run asynchronously; reference images may be supplied by URL or local path.]

## Skill Version(s):

1.3.32 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
