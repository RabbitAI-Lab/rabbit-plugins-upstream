## Description:

Edit real footage with an agent: turn raw takes of a talking head, podcast, vlog, course or ad into a clean cut, then add captions, B-roll, motion graphics and sound with HyperFrames or Remotion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to turn existing talking-head, podcast, vlog, course, or ad footage into a reviewed edit, with optional captions and graphics. It guides an agent through proposing cuts, producing media and edit files, and checking the result for a person to review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary reports a confirmed shell-injection risk in a shell-based transcription command.

Mitigation: Review the command before running it, use a fixed trusted command, and do not interpolate untrusted text into shell commands.

Risk: The security summary reports unpinned command-line downloads.

Mitigation: Use reviewed, pinned CLI versions from trusted sources before processing footage.

Risk: The security summary flags privacy gaps when choosing transcription or other external services, and reports incomplete scan coverage.

Mitigation: Prefer local processing for sensitive footage; check service data handling before sending media or transcripts, and review unresolved referenced paths before execution.

## Reference(s):

- [Project homepage (metadata link)](https://github.com/vargHQ/skills/tree/main/edit-footage-with-code)
- [Editing guide](https://varg.ai/how-to/edit-a-video-with-hyperframes-and-agents)
- [HyperFrames guidance](references/hyperframes.md)
- [Remotion guidance](references/remotion.md)

## Skill Output:

**Output Type(s):** [Video files (MP4), JSON edit lists and transcripts, FCPXML timelines, Shell commands, Review and quality-check guidance]

**Output Format:** [Media files and structured edit artifacts, with Markdown guidance and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill proposes edit decisions for human review and provides checks for listening to and watching the finished cut.]

## Skill Version(s):

1.0.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
