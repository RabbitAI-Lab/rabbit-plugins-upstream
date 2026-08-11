## Description:

Detects pet vomiting or regurgitation behavior from fixed-camera indoor video and returns structured observations about event timing, frequency, movement cues, and visible vomitus characteristics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze pet-area videos for vomiting or regurgitation events in home monitoring, multi-pet care, senior pet care, or animal hospital observation workflows. The output is for visual behavior observation and should not be treated as a veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private home camera footage or video URLs may be sent to a remote cloud backend.

Mitigation: Use the skill only with videos intended for that service, and avoid submitting footage that contains sensitive people, locations, or private household details.

Risk: The skill can silently create or reuse account identity and service tokens with limited user control.

Mitigation: Run it in a dedicated test workspace or disposable account context when evaluating the skill, and review locally stored credentials before broader use.

Risk: Report history and generated report links may be associated with the remote service account context.

Mitigation: Review whether cloud report retention and account association are acceptable before using the history-report workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-vomiting-regurgitation-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](artifact/references/api_doc.md)
- [Analysis API error-code reference](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with structured JSON-like analysis content, command examples, and report links when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts a local video file path or video URL; supported documented formats are mp4, avi, and mov with a documented 10 MB maximum file size.]

## Skill Version(s):

1.0.7 (source: ClawHub release metadata; artifact frontmatter says 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
