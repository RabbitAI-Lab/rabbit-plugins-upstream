## Description:

Helps an agent remove watermarks, logos, and corner marks from videos through the qhkit LinkPix video-edit workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to submit authorized video watermark-removal jobs, check task status, and return processed video links. It is intended for owned or otherwise authorized materials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary says the skill asks users to send an API key directly in chat.

Mitigation: Use QHKIT_TOKEN, qhkit local configuration, or a platform secret store instead of sharing API keys in chat.

Risk: Local videos passed to the skill may be uploaded to the qhkit/iqinghu service for processing and may incur credit charges after confirmation.

Mitigation: Confirm that the user is authorized to edit the videos, disclose upload and credit-charge expectations before submission, and wait for explicit user approval.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-video-watermark-remove)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [iqinghu console](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Markdown]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill can guide qhkit installation, token configuration, video job submission, polling, and delivery of returned video URLs.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
