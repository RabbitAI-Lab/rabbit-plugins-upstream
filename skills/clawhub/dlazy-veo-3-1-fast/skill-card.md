## Description:

Generates short text-to-video or image-to-video clips with Google Veo 3.1 Fast through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to ask an agent to invoke dLazy's hosted video generation service for fast Google Veo 3.1 Fast text-to-video, image-to-video, and video extension workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The dLazy CLI can store an API key in a local configuration file.

Mitigation: Use DLAZY_API_KEY per run or npx for non-persistent usage, and verify permissions on ~/.dlazy/config.json after login.

Risk: Local media provided to image, video, or audio fields may be uploaded to dLazy-hosted storage.

Mitigation: Confirm user approval before passing local media paths and avoid sending sensitive media unless the service terms and account controls are acceptable.

Risk: Video generation can consume paid credits.

Mitigation: Confirm expected cost and account balance before allowing generation, especially for high-resolution or repeated runs.

Risk: The documented dry-run behavior should not be treated as a guarantee that no network or upload behavior occurs.

Mitigation: Use dry-run only as an estimate aid and avoid passing sensitive local paths unless network behavior has been independently confirmed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1-fast)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with bash commands; CLI responses are JSON with hosted media URLs or task status, with optional downloaded video files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return asynchronous task identifiers when no-wait mode is used.]

## Skill Version(s):

1.3.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
