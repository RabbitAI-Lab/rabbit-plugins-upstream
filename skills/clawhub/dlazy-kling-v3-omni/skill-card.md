## Description:

Versatile video generation with Kling v3 Omni, supporting multimodal inputs to generate videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to generate videos from text prompts and image or video references through dLazy's hosted Kling v3 Omni service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence says the scan was partial and does not establish how the CLI login operation relates to the stated video-generation purpose.

Mitigation: Before installing or authenticating, review the linked CLI source and confirm that the login operation is expected for this workflow; treat the benign scan result as limited evidence.

Risk: Prompts and supplied local media are sent to dLazy's hosted API and media storage for generation.

Mitigation: Review prompts and media for sensitive content before invoking the skill, and use only material approved for upload to the service.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3-omni)
- [CLI repository linked in skill metadata (server-resolved provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)
- [dLazy API key setup](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Video assets, JSON]

**Output Format:** [Generated video URLs or saved video files with JSON task and result metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation may complete asynchronously; results can include a task identifier or hosted output URLs.]

## Skill Version(s):

1.3.38 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
