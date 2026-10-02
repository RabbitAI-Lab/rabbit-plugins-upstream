## Description:

LinkPix helps agents use Qinghu/qhkit to create and edit e-commerce images and videos, translate or improve media, generate scripts and storyboards, and run AI workflow tasks with status tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use LinkPix to turn product, advertising, video, translation, POD, and workflow requests into qhkit commands, status checks, and generated media or text outputs. It is aimed at e-commerce content production workflows that need images, videos, scripts, data files, or media-editing results from Qinghu services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can ask users to provide an API key in chat.

Mitigation: Use QHKIT_TOKEN or managed secret storage instead of pasting secrets into the conversation, and avoid logging or reprinting tokens.

Risk: The skill may install or run qhkit from npm, including latest or npx execution paths that can change over time.

Mitigation: Review and pin the @iqinghu/qhkit package version before deployment, and restrict global installs or npx execution to trusted environments.

Risk: Selected images, videos, audio, and workflow inputs may be uploaded to Qinghu services.

Mitigation: Submit only media the user is authorized to process and avoid uploading sensitive or regulated content unless the service and account controls are approved for that use.

Risk: Generate actions may consume credits and create tasks that cannot be cancelled.

Mitigation: Use estimate/options first, present key parameters and expected credit use, and require explicit user confirmation before any generate or script action.

## Reference(s):

- [LinkPix on ClawHub](https://clawhub.ai/autoagc/skills/linkpix)
- [AutoAGC publisher profile](https://clawhub.ai/user/autoagc)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu workbench](https://www.iqinghu.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Text, Markdown]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May install or run qhkit, configure QHKIT_TOKEN, upload user-provided media to Qinghu services, poll task status, and return generated media URLs, text outputs, data files, task IDs, and credit usage.]

## Skill Version(s):

0.1.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
