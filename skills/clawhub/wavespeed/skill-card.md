## Description:

Generate or edit AI media (image, video, audio, 3D) by calling the wavespeed CLI on the user's machine.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wavespeed](https://clawhub.ai/user/wavespeed)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent select WaveSpeed models and run WaveSpeed CLI commands for media generation, editing, animation, upscaling, audio, and marketing creative workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and input files passed with @path are sent to WaveSpeed-hosted services.

Mitigation: Use @path only for files the user intends to upload, and avoid sensitive personal or confidential files unless approved.

Risk: Media generation runs can incur usage costs.

Mitigation: Check WaveSpeed usage or billing records before expensive or high-volume generation runs.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON result handling guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference WaveSpeed run IDs, output URLs, saved file paths, and usage or billing checks.]

## Skill Version(s):

0.4.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
