## Description:

Creates lip-synced talking-person videos from a source video and replacement speech audio using the dLazy-hosted Tongyi VideoRetalk service, with optional reference-face selection for videos containing multiple faces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content-production agents use this skill to invoke VideoRetalk for dubbing and lip-sync workflows, supplying a talking-person video, speech audio, and optionally a reference face image when multiple faces appear.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local video, audio, and reference image paths provided to the skill may be uploaded to dLazy cloud endpoints for processing.

Mitigation: Process only media you have rights and consent to use, avoid sensitive media unless appropriate for the service, and review dLazy service terms before use.

Risk: The skill requires a dLazy API key and may save credentials in the local CLI configuration.

Mitigation: Use DLAZY_API_KEY for per-invocation credentials or rotate and revoke saved keys from the dLazy dashboard when needed.

Risk: The examples and command flags in the artifact documentation are inconsistent.

Mitigation: Run dlazy videoretalk -h or use --dry-run to verify parameters before submitting a job.

Risk: Lip-sync generation can create media that misrepresents a person's speech or likeness.

Mitigation: Use the skill only with appropriate rights, consent, and disclosure for the intended media workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-videoretalk)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON responses with hosted media URLs and optional downloaded media files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return an asynchronous generateId when --no-wait is used; --save downloads the result asset locally.]

## Skill Version(s):

1.3.12 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
