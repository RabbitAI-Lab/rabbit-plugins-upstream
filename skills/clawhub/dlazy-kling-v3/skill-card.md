## Description:

Powerful video generation with Kling v3. Supports high-quality text-to-video and image-to-video. 使用可灵 (Kling) v3 强大的文生视频与图生视频。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can request Kling v3 text-to-video or image-to-video generation, then receive generated media through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The available security review was partial and flags a mismatch involving the documented login and generation flow.

Mitigation: Review the CLI's login and generation behavior before running it.

Risk: Prompts and supplied local media are sent to dLazy hosted services for generation.

Mitigation: Only submit prompts and media that are appropriate to send to the service.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [CLI repository link listed in the skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Video assets, JSON, Shell commands]

**Output Format:** [Generated media URLs and JSON task results, invoked through the dlazy CLI]

**Output Parameters:** [Prompt, optional reference images, aspect ratio, duration, generation mode, and sound setting]

**Other Properties Related to Output:** [Generated media is hosted by dLazy; supplied local media may be uploaded to its hosted service.]

## Skill Version(s):

1.3.39 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
