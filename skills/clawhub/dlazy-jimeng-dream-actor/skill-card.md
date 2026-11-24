## Description:

Convert static character images into vivid action videos with Jimeng Dream Actor. 使用即梦 (Jimeng) Dream Actor，将静态人物图片转化为生动的动作视频。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can turn a static character image into an action video by providing a prompt and image to Jimeng Dream Actor.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan is benign but medium confidence and partial, with some package and service references unresolved.

Mitigation: Review the documented login flow and pinned CLI install commands before setup, and confirm the package and service details you intend to use.

Risk: Prompts and local media supplied to the skill are sent to dLazy's hosted API and media storage.

Mitigation: Submit only prompts and media you are permitted to share with the service.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-dream-actor)

## Skill Output:

**Output Type(s):** [Media assets, JSON]

**Output Format:** [Generated media with a JSON result containing hosted asset URLs and task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Media may be returned asynchronously; generated files are hosted by the service.]

## Skill Version(s):

1.3.43 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
