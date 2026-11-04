## Description:

Fast response and generation of short videos with Google Veo 3.1 Fast.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to generate short videos from text prompts or input frames, or to extend an existing video, through dLazy's Veo 3.1 Fast service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local media supplied for generation are sent to dLazy; local image or video inputs are uploaded to its media storage.

Mitigation: Review prompts and use only media you are comfortable uploading before submitting a generation request.

Risk: Generation can incur charges, and login saves the organization API key in the local CLI configuration.

Mitigation: Use the CLI dry run to review the payload and cost estimate, protect access to the local configuration, and revoke the key through dLazy if needed.

Risk: The reviewed artifacts contain instructions only; the security of the external CLI and hosted service was not established by this verdict.

Mitigation: Assess the CLI and hosted service separately before relying on them for sensitive workflows.

## Reference(s):

- [dLazy](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Files, API Calls]

**Output Format:** [Generated video files or hosted result URLs, with JSON status and output metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Short videos generated from prompts and optional frame or video inputs; duration and resolution depend on generation mode and selected options.]

## Skill Version(s):

1.3.36 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
