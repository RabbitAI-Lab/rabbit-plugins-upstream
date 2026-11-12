## Description:

Rebuilds a video as an editable HyperFrames project, checked against the original frame by frame.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Video editors and creators can use this skill to reconstruct videos as editable HyperFrames projects and compare the result with the source. Use only source media the user has the right to process.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow runs an unpinned CLI and may send video or audio to external services, which can expose private footage or identifiable people.

Mitigation: Review and pin a trusted CLI version, and process only media that is authorized for external sharing; avoid sensitive footage unless that processing is approved.

## Reference(s):

- [Opening a Reverse](references/start.md)
- [Re-shooting a person](references/people.md)
- [Animated and painted films](references/animated.md)
- [Matching what is drawn](references/match.md)
- [ClawHub skill release](https://clawhub.ai/heygen-com/skills/reverse-any-video)

## Skill Output:

**Output Type(s):** [Files, Code, Shell commands, Guidance]

**Output Format:** [Editable HyperFrames project files with implementation guidance and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reconstructed layers and timing are checked against the source video; fidelity depends on source analysis and generated or substituted assets.]

## Skill Version(s):

1.0.18 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
