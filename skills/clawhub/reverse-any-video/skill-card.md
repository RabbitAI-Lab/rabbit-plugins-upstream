## Description:

Rebuilds a video as an editable HyperFrames project and checks the render against the original frame by frame.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video editors use this skill to recreate videos they have the right to use as editable HyperFrames projects, rebuilding graphics and sub-assets and generating replacement shots for people when appropriate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can start paid HeyGen generation without approval and may omit credit-use information.

Mitigation: Get approval first, set a firm budget that covers retries, and include estimates and usage reporting in saved handoffs.

Risk: The workflow sends depicted people's footage to HeyGen by default.

Mitigation: Require approval for media uploads and confirm permission to process depicted people, or explicitly decline HeyGen.

Risk: An unverified or changing HyperFrames installation may not be the version the user intended to run.

Mitigation: Use a verified, pinned HyperFrames installation.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/heygen-com/skills/reverse-any-video)
- [Opening a Reverse](artifact/references/start.md)
- [Re-shooting a person](artifact/references/people.md)
- [Matching what is drawn](artifact/references/match.md)

## Skill Output:

**Output Type(s):** [Files, Code, Shell commands, Guidance]

**Output Format:** [Editable HyperFrames project files with HTML components, media assets, and Markdown handoff notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project structure follows the source video's dimensions, frame rate, duration, cuts, and original audio.]

## Skill Version(s):

1.0.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
