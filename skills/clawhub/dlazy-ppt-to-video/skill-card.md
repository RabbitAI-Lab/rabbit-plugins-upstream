## Description:

ppt to video, powerpoint to video, slides to video, presentation to video — parse the deck, outline, storyboard, voiceover, build, validate. Use when the user gives a PPT / PowerPoint / Keynote and wants an explainer, pitch, courseware, or training video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People preparing presentations, courseware, or training materials can use this skill to turn PowerPoint and other documents into narrated explainer videos. It supports starting a project and continuing work in a project-scoped session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan rates the skill suspicious with medium confidence because its triggers and actions may extend beyond its stated presentation-to-video purpose.

Mitigation: Review the trigger scope and consider whether report-analysis requests should be allowed to initiate video generation.

Risk: The skill uses an authenticated external CLI that can list organization projects and upload attached local files; the security evidence says package details were unavailable and the scan is incomplete.

Mitigation: Review the CLI and external-service handling before installation, authorize only intended project access, and attach only files approved for upload.

## Reference(s):

- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video, Text, Guidance]

**Output Format:** [Generated video files, streamed text responses, and Markdown usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-scoped sessions; attached local files are uploaded to dLazy media storage.]

## Skill Version(s):

1.0.39 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
