## Description:

ByteDance's latest video generation model. Supports multi-modal reference (images, video, audio) to generate videos, as well as first/last frame and text-to-video modes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to request video generation from text prompts, multimodal references, or first and last frame images through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was partial and reported a possible mismatch between the skill's video-generation description and a login command, along with unresolved references.

Mitigation: Before installing or running the skill, confirm the command behavior and review unresolved references using trusted package documentation.

Risk: The skill documentation says prompts and referenced local media are sent to dLazy-hosted services for processing.

Mitigation: Only submit prompts and media that are appropriate to share with that service.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0)
- [dLazy service](https://dlazy.com)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Files, API Calls, Shell commands, Configuration instructions]

**Output Format:** [Generated video files and JSON API results, with Markdown usage and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is returned through hosted URLs; results can be downloaded to a local path.]

## Skill Version(s):

1.3.40 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
