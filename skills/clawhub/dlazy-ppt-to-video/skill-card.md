## Description:

Helps turn presentations and other documents into narrated explainer, pitch, courseware, or training videos using dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People preparing explainer, pitch, training, or courseware videos use this skill to turn presentations and other documents into a video workflow through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Attached presentations and other documents are uploaded to a third-party service, potentially exposing confidential content.

Mitigation: Upload only materials approved for dLazy's storage and processing terms; avoid confidential decks, spreadsheets, PDFs, and customer data without organizational approval.

Risk: The PPT-to-video title may obscure that the skill also accepts broader document inputs and uploads.

Mitigation: Confirm the files and intended destination with the user before attaching or uploading them.

Risk: A saved dLazy API key remains available on the local machine.

Mitigation: Prefer a per-invocation API key, or revoke the saved key when it is no longer needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-ppt-to-video)
- [dLazy CLI project (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package (listed in skill metadata)](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands]

**Output Format:** [Text responses with video-creation guidance and optional commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video creation is handled through the dLazy hosted service.]

## Skill Version(s):

1.0.26 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
