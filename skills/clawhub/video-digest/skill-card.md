## Description:

Turns a YouTube video or supplied transcript into timestamped notes in Quick, Deep, or Research formats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

People who want to understand a video without watching it in full can use this skill to create timestamped summaries, structured notes, or source-backed checks of selected claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fetching public captions sends the supplied video reference to YouTube, and the transcript cache may remain until cleared.

Mitigation: Use a supplied transcript to skip fetching, or clear the temporary cache after use.

## Reference(s):

- [Output Modes](artifact/references/output-modes.md)
- [ClawHub release](https://clawhub.ai/bonniegeng-max/skills/video-digest)
- [Publisher profile](https://clawhub.ai/user/bonniegeng-max)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Timestamped Markdown notes or claim-verification tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Quick, Deep, Research, and Batch Quick formats; takeaways and excerpts link back to video timestamps.]

## Skill Version(s):

2.0.6 (source: frontmatter; server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
