## Description:

Midjourney style generation, supports aspect ratio, Bot type, and output position (grid/U1-U4). Suitable for artistic and strongly stylized creative generation. Midjourney 风格出图入口，支持画幅、Bot 类型与输出位（grid/U1-U4）。适合艺术化、风格强烈的创意图生成。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to request Midjourney-style images and choose an aspect ratio, bot type, and grid or U1–U4 output. Results are returned as image links or an asynchronous task identifier in JSON.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scan has medium confidence and incomplete coverage, and reports a mismatch between the advertised image-generation purpose and the documented login behavior.

Mitigation: Review the CLI package and documented login flow before installation; the scan did not establish credential theft or other additional behavior.

Risk: Prompts and any supplied local media files are sent to dLazy-hosted services.

Mitigation: Avoid submitting sensitive prompts or files unless their handling is acceptable under your organization’s policies and the service terms.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [JSON containing image URLs or asynchronous task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image results are hosted remotely; asynchronous requests may return a task identifier before results are ready.]

## Skill Version(s):

1.3.38 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
