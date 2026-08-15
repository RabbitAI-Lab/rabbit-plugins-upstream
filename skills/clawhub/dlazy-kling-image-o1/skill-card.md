## Description:

Generates Kling O1 images from text prompts or reference images through the dLazy hosted API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate or edit images with Kling O1 using text prompts and optional reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local API-key storage can expose credentials if the user config file is readable by other processes or users.

Mitigation: Prefer DLAZY_API_KEY for per-invocation authentication when handling sensitive work, or verify permissions on ~/.dlazy/config.json after using dlazy login or dlazy auth set.

Risk: Prompts and private reference images are sent to dLazy services for hosted generation.

Mitigation: Review prompts and image inputs before invocation, especially when they contain private or sensitive content.

Risk: Broad image-generation triggers can cause accidental invocation.

Mitigation: Use explicit Kling or dLazy invocation language before sending prompts or reference images.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-kling-image-o1)
- [dLazy CLI Homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Service Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Files, Shell commands, Guidance]

**Output Format:** [JSON with hosted image URLs and optional async task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May upload reference images to dLazy media storage and return files.dlazy.com URLs; async mode returns a generateId for polling.]

## Skill Version(s):

1.3.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
