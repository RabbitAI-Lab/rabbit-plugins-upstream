## Description:

Rebuild any video file as an editable HyperFrames project - motion graphics, talking heads, live action or AI-generated footage - checked against the original frame by frame. Use to reverse, recreate, remake, replicate or copy a video, or 「复刻这个视频」「照着这个视频做一个」.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video creators use this skill to reconstruct a source video as an editable HyperFrames project and compare the reconstruction with the original. The source video should be one they have the right to use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill repeatedly runs an unpinned HyperFrames package, so the software used may change between runs.

Mitigation: Review and pin a specific package version before running the workflow in a controlled environment.

Risk: Reconstruction may send media to HeyGen or cloud services without a clear privacy approval step.

Mitigation: Confirm that the media may be shared with those services and obtain any required approval before processing it.

Risk: The security scan was partial because three references could not be resolved.

Mitigation: Resolve and review the unavailable references before relying on the scan as a complete assessment.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/heygen-com/skills/reverse-any-video)
- [Publisher profile](https://clawhub.ai/user/heygen-com)
- [Opening a Reverse](artifact/references/start.md)
- [Re-shooting a person](artifact/references/people.md)
- [Animated and painted films](artifact/references/animated.md)
- [Matching what is drawn](artifact/references/match.md)

## Skill Output:

**Output Type(s):** [Code, Files, Shell commands, Guidance]

**Output Format:** [Editable HyperFrames project files and Markdown handoff]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Frame-timed reconstruction checked against the source video.]

## Skill Version(s):

1.0.17 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
