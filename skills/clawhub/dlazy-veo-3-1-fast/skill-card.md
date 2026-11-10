## Description:

Generates short videos from text prompts or reference frames with Google Veo 3.1 Fast through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use this skill to generate short videos from text prompts or supplied frames, or to extend a video. It sends requests through the dLazy service and can return hosted output links or save media locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review had medium confidence and incomplete evidence; a reported login operation does not clearly match the video-generation purpose.

Mitigation: Before installing, review the CLI and its authentication behavior through a trusted source and confirm the login flow meets your needs.

Risk: Prompts and local media supplied to the skill are sent to dLazy's hosted service, and local media may be uploaded for processing.

Mitigation: Do not submit sensitive prompts or media unless their transfer to the service is approved for your use case.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1-fast)

## Skill Output:

**Output Type(s):** [Files, API Calls, Guidance]

**Output Format:** [Hosted video URLs and JSON command results; optionally saved media files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Short video assets; asynchronous requests may return a task ID before completion.]

## Skill Version(s):

1.3.37 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
