## Description:

Turns slides or documents into narrated slideshow videos with voiceover and transitions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users with a presentation or document use this skill to request an explainer, report, courseware, or training video in slideshow form.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI authenticates to a dLazy organization and can list its projects.

Mitigation: Review the CLI setup and requested organization access; authenticate only with an account whose project access is appropriate.

Risk: Files attached to a request are uploaded to dLazy media storage for processing.

Mitigation: Before attaching a document, confirm it is appropriate to send to the hosted service and remove sensitive content that is not needed.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-slideshow-video)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI project page](https://github.com/dlazy-ai/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video files, Text, Guidance]

**Output Format:** [Narrated slideshow video and text responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video content is produced through the dLazy hosted service.]

## Skill Version(s):

1.0.36 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
