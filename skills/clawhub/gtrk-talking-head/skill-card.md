## Description:

Guides an agent through turning one or more talking-head recordings into a packaged video editing project, including audio alignment, rough cutting, supporting visuals, music, subtitles, and export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gitruck](https://clawhub.ai/user/gitruck)

### License/Terms of Use:

MIT-0

## Use Case:

Video creators and editors use this skill to organize a talking-head recording workflow from raw footage through a reviewable, packaged editing project. It helps an agent coordinate local editing steps and optional cloud processing through the gtrk CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Footage may be unsuitable for cloud processing, and cloud steps may incur charges.

Mitigation: Confirm the footage is suitable for cloud processing and review charges before running cloud steps.

Risk: Transcription or rough-cut choices may produce an inaccurate edit.

Mitigation: Set the transcription language for the recording and inspect the rough cut before continuing through the workflow.

Risk: Removing source or intermediate media can make editing projects incomplete or unusable.

Mitigation: Retain the original footage and intermediate media files.

## Reference(s):

- [Gitruck CLI](https://github.com/Gitruck/cli)
- [gtrk-talking-head on ClawHub](https://clawhub.ai/gitruck/skills/gtrk-talking-head)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Video editing project files]

**Output Format:** [Markdown workflow guidance with shell command examples and editing project files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May coordinate local editing and paid cloud-processing steps; final export is completed through the editing client or supported local tools.]

## Skill Version(s):

1.3.9 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
