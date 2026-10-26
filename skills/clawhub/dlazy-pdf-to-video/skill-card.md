## Description:

PDF to video, PDF to explainer video, PDF to presentation video — parse the PDF, outline, storyboard, voiceover, build, validate. Use when the user gives a PDF and wants an explainer, report broadcast, courseware, or training video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn PDFs into explainer, report, courseware, or training videos through dLazy's file-to-video workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Documents attached to a request are uploaded to dLazy storage.

Mitigation: Only attach documents you are comfortable sending to dLazy, and review its retention terms before uploading.

Risk: The CLI stores an organization API key for authenticated requests.

Mitigation: Protect the saved key and revoke it when it is no longer needed.

Risk: Video generation uses account credits.

Mitigation: Check the service's credit costs before starting a generation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-pdf-to-video)
- [dLazy service](https://dlazy.com)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Video, Text, Guidance]

**Output Format:** [Generated video files and streamed text responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-scoped, multi-turn workflow; attached documents are uploaded to dLazy storage.]

## Skill Version(s):

1.0.31 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
