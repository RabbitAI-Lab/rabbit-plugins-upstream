## Description:

Helps agents turn talking-head, podcast, vlog, course, or ad footage into a reviewed cut, then add timed captions, B-roll, graphics, and sound.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT

## Use Case:

Developers and video creators use the skill to plan and edit existing footage with FFmpeg and word timings, add optional HyperFrames or Remotion overlays, and review the result before delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated shell commands or components may handle input unsafely.

Mitigation: Review and correctly quote or escape arguments before running generated commands or components.

Risk: Confidential footage or names may be exposed through external transcription, judging, or web search services.

Mitigation: Keep confidential footage local unless you authorize the specific provider, and disable web searches for private names.

Risk: Unreviewed dependencies or large media inputs can create avoidable execution and processing risks.

Mitigation: Use reviewed, pinned dependencies in an isolated media project and limit media size.

Risk: Automated checks may miss editing problems that require listening or visual review.

Mitigation: Retain human review of the media and edit before delivery.

## Reference(s):

- [Project homepage](https://github.com/vargHQ/skills/tree/main/edit-footage-with-code)
- [ClawHub skill page](https://clawhub.ai/vargai/skills/edit-footage-with-code)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Files]

**Output Format:** [Markdown instructions and generated media/edit files such as MP4, JSON, FCPXML, HTML, and TSX]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on the source footage, transcript timings, and selected editing workflow.]

## Skill Version(s):

1.0.1 (source: frontmatter, server metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
