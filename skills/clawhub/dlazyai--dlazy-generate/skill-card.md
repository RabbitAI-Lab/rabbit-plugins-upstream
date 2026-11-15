## Description:

Routes image, video, and audio generation requests to suitable dlazy CLI models.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create or edit images, generate videos, and synthesize audio through dLazy models selected for their requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The broad activation trigger could cause the skill to run for requests outside the intended generation tasks.

Mitigation: Confirm the requested media type and intended dlazy action before running a command.

Risk: Prompts and supplied local media are sent to dLazy hosted services for processing.

Mitigation: Avoid submitting confidential prompts or media unless their use with the service is authorized.

Risk: The scanner reported a mismatch between the documented media-generation behavior and the implementation it inspected, with some local references unresolved.

Mitigation: Review the installed CLI package and its authentication setup before use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-generate)
- [CLI project link listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, Videos, Audio, Hosted media URLs]

**Output Format:** [Generated media files and URLs, returned in JSON result envelopes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can pass media outputs between dlazy commands; supplied local media may be uploaded for cloud processing.]

## Skill Version(s):

1.3.42 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
