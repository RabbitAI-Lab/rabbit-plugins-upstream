## Description:

Generate dynamic videos based on a single first frame image and prompts using Jimeng.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to request a Jimeng video from a first-frame image and a text prompt, then retrieve the generated result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review found no clear malicious behavior, but the supplied commands show a dLazy login flow rather than the advertised video-generation workflow, and the CLI package was not included in the evidence.

Mitigation: Before installing or using the skill, verify the CLI package and its authentication and generation flows, and confirm it provides the expected video-generation workflow.

Risk: Prompts and local image files are sent to dLazy hosted services for processing and storage.

Mitigation: Send only prompts and media that are appropriate to share with the service under your privacy and data-handling requirements.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first)
- [CLI project link listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Video files, JSON]

**Output Format:** [Video result URL or saved video file, with JSON task and result metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports 5- or 10-second duration options and asynchronous task IDs.]

## Skill Version(s):

1.3.38 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
