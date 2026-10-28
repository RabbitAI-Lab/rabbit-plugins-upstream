## Description:

pdf to video, pdf to explainer video, pdf to presentation video — parse the PDF, outline, storyboard, voiceover, build, validate. Use when the user gives a PDF and wants an explainer, report broadcast, courseware, or training video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users who have a PDF can use this skill to request an explainer, report, courseware, or training video through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached documents are handled by dLazy's hosted service, and projects retain conversation context.

Mitigation: Upload only documents you are comfortable sharing with dLazy, use the intended project, and clear the saved session when its context should be dropped.

Risk: Authentication can save an organization API key in local CLI configuration, and generation consumes service credits.

Mitigation: Use the documented login flow instead of sharing a key in chat, and check available credits before generating videos.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-pdf-to-video)
- [dLazy](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Video files, Text, Guidance]

**Output Format:** [Generated video files with text status and guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation uses dLazy's hosted service.]

## Skill Version(s):

1.0.33 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
