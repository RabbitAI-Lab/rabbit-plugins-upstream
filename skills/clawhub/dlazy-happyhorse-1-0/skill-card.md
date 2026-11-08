## Description:

Happy Horse 1.0 provides text-to-video, first-frame-to-video, reference-to-video, and video editing modes, routing each request to the matching model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate videos from text prompts, first frames, reference images, or existing videos through dLazy's hosted Happy Horse 1.0 service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media are sent to dLazy's hosted service, and local media may be uploaded to its storage.

Mitigation: Only submit media you intend to upload and are authorized to use; avoid sending sensitive content unless appropriate for the service.

Risk: The CLI stores an API key in the user's local configuration, and requests may incur charges.

Mitigation: Protect the API key, rotate or revoke it when needed, and use --dry-run to review estimated charges before generation.

Risk: The review covered the skill documents; the pinned CLI executable and hosted service remain unverified.

Mitigation: Review the pinned CLI before installation and review dLazy's service terms before use.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video, JSON]

**Output Format:** [JSON response with generated video URLs; optionally a saved video file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video mode, duration, resolution, and aspect ratio vary by request; generation can be asynchronous.]

## Skill Version(s):

1.3.38 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
