## Description:

Indexes video metadata from a PikPak cloud drive into a searchable Markdown or CSV inventory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

PikPak users can inventory and filter cloud-stored videos by quality or duration and export a local media index.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The default scan reads metadata across the entire PikPak drive, and the exported index may reveal private file names and paths.

Mitigation: Specify a folder ID for sensitive libraries and review the local Markdown or CSV index before sharing it.

Risk: The documentation promises a source column and source filtering that the generated index does not provide.

Mitigation: Do not rely on source details or source-based filtering until the skill is updated.

## Reference(s):

- [PikPak Media Index on ClawHub](https://clawhub.ai/pipiguai87-alt/skills/pikpak-media-index)

## Skill Output:

**Output Type(s):** [Markdown, Text]

**Output Format:** [Markdown table or CSV file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local snapshot of video names, paths, durations, resolutions, codecs and sizes; optional quality or duration filters.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
