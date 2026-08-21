## Description:

Converts PDFs and other documents into explainer, report, courseware, or training videos by helping parse content, create outlines and storyboards, generate voiceover, build, and validate.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to route PDF or document-to-video work to dLazy, producing explainers, report broadcasts, courseware, or training videos from supplied documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected documents are sent to dLazy endpoints.

Mitigation: Confirm before attaching files and avoid sending sensitive documents unless approved for dLazy processing.

Risk: The local API-key storage claim was not fully supported by the inspected CLI.

Mitigation: Use DLAZY_API_KEY per invocation where appropriate, check local config file permissions, and rotate or revoke the key if exposure is suspected.

Risk: The security verdict is suspicious due to hosted-service data transfer and key-handling concerns.

Mitigation: Review the security summary and guidance before deployment, and install only when the data-transfer and credential-handling model is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-pdf-to-video)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands and streamed CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May upload attached files to dLazy media storage and stream hosted agent output through the dLazy CLI.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact frontmatter says 1.0.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
