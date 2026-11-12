## Description:

GPT Image 2.5 Flare, the speed tier of OpenAI's GPT Image 2.5 series, for text-to-image and image editing. Fast and cost-effective for high-volume everyday generation; supports reference images, aspect ratios up to 21:9 and quality up to max.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators can generate or edit images from text prompts, optionally using reference images and choosing an aspect ratio and quality level.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was partial and medium-confidence; it noted a login command, unresolved references, and flagged whitespace.

Mitigation: Check that the login flow fits your needs and review the unresolved references before installation.

Risk: Prompts and local reference images are sent to dLazy-hosted services, and the security review does not establish credential or data handling practices.

Mitigation: Review dLazy's service and credential handling before use, and avoid sending sensitive prompts or images unless that handling is acceptable.

## Reference(s):

- [CLI project link (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)
- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2-5-flare)

## Skill Output:

**Output Type(s):** [Images, JSON, Files]

**Output Format:** [Hosted image URLs with JSON result metadata; optionally saved image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return an asynchronous task identifier with --no-wait; reference images, aspect ratio, and quality are configurable.]

## Skill Version(s):

1.2.29 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
