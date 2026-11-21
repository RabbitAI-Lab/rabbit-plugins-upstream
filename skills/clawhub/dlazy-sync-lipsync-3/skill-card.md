## Description:

Given a video and audio input, this skill uses dLazy's sync-lipsync v3 service to generate a video with lip movements aligned to the audio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, video creators, and localization teams can align a speaker's lip movements with replacement audio for dubbing, localization, or virtual presenters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review says the scan did not verify the skill's lip-sync behavior or explain dlazy CLI login authentication, and unresolved local references leave the evidence incomplete.

Mitigation: Review the linked CLI project and confirm the login flow and command behavior before installation or execution.

Risk: The documented workflow uploads local video and audio to dLazy-hosted services.

Mitigation: Use only media the user is authorized to upload, and make the external transfer clear before running the skill.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy API key setup](https://dlazy.com/dashboard/organization/api-key)
- [ClawHub release](https://clawhub.ai/dlazyai/skills/dlazy-sync-lipsync-3)

## Skill Output:

**Output Type(s):** [Video, JSON, Shell commands]

**Output Format:** [Generated video file or hosted URL with a JSON CLI response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts video and audio inputs with a selectable sync mode; asynchronous tasks may return a task ID.]

## Skill Version(s):

1.3.42 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
