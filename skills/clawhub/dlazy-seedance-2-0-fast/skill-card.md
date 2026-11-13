## Description:

Provides CLI guidance for requesting Seedance 2.0 Fast video generation with text prompts and optional multimodal or first/last-frame references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative users use the skill to request text-to-video or reference-guided generation through dLazy's Seedance workflow and receive task results or hosted output URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review has medium confidence and partial inspection; it notes a possible mismatch between the advertised video-generation purpose and the reported command, and the skill depends on a third-party CLI and login flow.

Mitigation: Before installing, consider whether you are comfortable with the pinned CLI and its login flow, and review its behavior if confirming the generation path matters to you.

Risk: Prompts and supplied media are sent to dLazy's hosted service, and local media paths may be uploaded for processing.

Mitigation: Avoid sending sensitive prompts or media unless you accept the service's handling; review dLazy's service terms.

## Reference(s):

- [ClawHub release](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0-fast)
- [dLazy CLI source (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [API Calls, Files, Guidance]

**Output Format:** [JSON result with generated output URLs or asynchronous task status; optionally downloaded media files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation settings can include text, image, video, and audio references; video may be requested through text-to-video or frame-based input.]

## Skill Version(s):

1.3.39 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
