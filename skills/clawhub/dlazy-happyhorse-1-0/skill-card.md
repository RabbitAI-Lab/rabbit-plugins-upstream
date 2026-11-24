## Description:

Generates or edits Happy Horse 1.0 videos from text prompts, first frames, reference images, or existing videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to create short videos from text, first-frame or reference images, and to edit existing video. Requests require a dLazy API key and are processed through the hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan found the inspected content focused on authentication rather than the advertised video features. Its review was partial: referenced local paths and the CLI package were not inspected; the scan did not establish credential theft.

Mitigation: Review the CLI package and referenced local paths before relying on the skill, and proceed only if comfortable with its authentication behavior.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-happyhorse-1-0)
- [CLI project link listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video, Hosted media URLs, Shell commands]

**Output Format:** [JSON result with generated media URLs; optionally a downloaded video file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous task IDs and saving generated media to a local path.]

## Skill Version(s):

1.3.44 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
