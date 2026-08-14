## Description:

Use when a Project Protocol video needs short-form candidate planning, approval, horizontal extraction, or reviewed 9:16 delivery before or after the shared main render.

This skill is ready for commercial/non-commercial use.

## Publisher:

[whitetowerai](https://clawhub.ai/user/whitetowerai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video production agents use this skill to plan approved short-form clips from Project Protocol videos, bind those choices to a verified main render, and create horizontal or reviewed 9:16 derivatives.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes local video assets and invokes ffmpeg/Python, which can create project-scoped media, review, and final output artifacts.

Mitigation: Install it only for projects where that local video workflow is intended, confirm /video-understand, ffmpeg/ffprobe, and Pillow are available, and run it inside the intended project root.

Risk: Candidate selection or vertical crop decisions can affect whether generated shorts are complete, accurate, and visually usable.

Mitigation: Use the hash-bound candidate and vertical review gates, and proceed to final extraction or rendering only after explicit human approval or clearly delegated agent approval.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/whitetowerai/skills/video-to-shorts)

## Skill Output:

**Output Type(s):** [guidance, shell commands, JSON, markdown, media files]

**Output Format:** [Markdown protocol instructions with PowerShell command examples, JSON plans and receipts, review pages, and project-scoped video outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes work/shorts, work/cache/shorts, review/06-shorts, and final/shorts artifacts; requires /video-understand, ffmpeg/ffprobe, Python, and Pillow.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
