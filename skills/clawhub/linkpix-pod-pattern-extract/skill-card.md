## Description:

This skill helps agents extract print patterns from product or apparel images as reusable high-resolution POD design assets through the qhkit image workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, POD operators, and design agents use this skill to turn apparel or product photos into reusable flat print artwork. The skill also guides users on setup, output review, and unsupported requests such as vector or transparent-layer extraction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade qhkit globally and change the local Node/npm environment.

Mitigation: Prefer a pinned qhkit package version, review install or upgrade commands before running them, and use npx or an isolated environment when global installation is not appropriate.

Risk: Local images are uploaded to the provider for generation, and qhkit requires an API token.

Mitigation: Use only images approved for external processing and configure QHKIT_TOKEN through environment or secret-management practices that avoid exposing the token in shell history.

Risk: Generated pattern extraction can differ from the source artwork and may involve brand or IP content.

Mitigation: Review generated outputs for fidelity and copyright or trademark concerns before reuse.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-pod-pattern-extract)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [iQingHu LinkPix workspace](https://www.iqinghu.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON CLI parameters; qhkit responses are JSON that may contain generated image URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include setup steps, qhkit command invocations, generated image URLs, actual credit usage, and user-facing failure messages from the CLI.]

## Skill Version(s):

0.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
