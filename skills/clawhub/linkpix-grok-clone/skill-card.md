## Description:

Grok 爆款视频复刻 | LinkPix helps social media operators and short-video creators analyze a viral short-video structure, rewrite it for their own product, and use qhkit/LinkPix video generation to produce a new clip.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External social media teams and short-video creators use this skill to turn a public video link into a source script, rewrite the structure for their own product, estimate cost, and generate a new LinkPix/Qinghu video after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks the agent to collect and configure a Qinghu API key.

Mitigation: Use a scoped, revocable key, prefer secure secret storage, and avoid pasting secrets into chat when a secret store is available.

Risk: The skill can install or upgrade qhkit, Node, Pillow, and sharp-cli dynamically.

Mitigation: Prefer preinstalled and pinned versions; review installation commands before running them in a production environment.

Risk: Video generation tasks may consume credits and cannot be canceled after submission.

Mitigation: Run estimates where supported and require explicit user confirmation of model, duration, inputs, and expected credits before generation.

## Reference(s):

- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/linkpix-grok-clone)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides script extraction, rewrite review, cost estimation, task submission, polling, and delivery of generated video URLs.]

## Skill Version(s):

0.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
