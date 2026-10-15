## Description:

Retrieves real-time comments for a TikTok video by video ID using Qinghu's data service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and analysts use this skill to retrieve and review comments on a specified TikTok video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Skill instructions may install or update Node/npm and qhkit or change the local environment.

Mitigation: Review installation steps and preinstall a vetted, pinned qhkit version rather than running unpinned npx or @latest commands.

Risk: Qinghu API token setup involves handling a credential.

Mitigation: Use an approved credential-handling method and avoid exposing the token in shared output.

Risk: Qinghu comment requests can consume paid credits, with cost varying by result size.

Mitigation: Check the estimated credit cost and obtain approval before paid requests, especially bulk lookups.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-tiktok-video-comments)
- [Qinghu qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise comment summary with optional tabular file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the video ID and the Qinghu API response.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
