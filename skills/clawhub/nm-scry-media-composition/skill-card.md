## Description:

Combines GIFs and videos into composite tutorials with vertical or grid layouts via FFmpeg.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical documentation authors use this skill to combine separately generated GIFs, videos, and images into tutorial-ready composite media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated FFmpeg commands may overwrite output files or use manifest-provided prerequisite commands.

Mitigation: Review command arguments, output paths, overwrite flags, and prerequisite commands before execution.

Risk: Broad media-related triggers may activate the skill for loosely related requests.

Mitigation: Confirm the user is asking for multi-asset media composition before applying the workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-scry-media-composition)
- [Metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/scry)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with YAML examples and FFmpeg command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Focuses on local media composition workflows; users should review generated commands before execution.]

## Skill Version(s):

1.9.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
