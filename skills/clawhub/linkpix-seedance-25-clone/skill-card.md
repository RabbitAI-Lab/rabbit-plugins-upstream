## Description:

Helps short-video creators, MCN teams, and brand marketers use Qinghu AI and qhkit to analyze a viral video, rewrite its structure for their own product, and generate a Seedance 2.5-style video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, agencies, and marketing teams use this skill to convert a source social-video link into an analyzed script, adapt the structure and pacing for a product, and submit a qhkit video-generation task after user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks the agent to install and run qhkit through Node/npm.

Mitigation: Install only after reviewing the package source and expected PATH or npm changes in the target environment.

Risk: The workflow requires a live Qinghu API key for service access.

Mitigation: Provide credentials through a secret manager or environment variable where possible, and avoid pasting long-lived keys into chat.

Risk: The workflow can upload source videos, product images, or generated prompts to an external service.

Mitigation: Use only media and links the user has rights and consent to process.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-seedance-25-clone)
- [Publisher profile](https://clawhub.ai/user/autoagc)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce rewritten script comparisons, qhkit status guidance, and generated-video delivery links when the external service completes.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
