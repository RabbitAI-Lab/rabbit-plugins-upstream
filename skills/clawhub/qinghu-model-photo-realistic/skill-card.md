## Description:

This skill helps agents use Qinghu AI's qhkit workflow to make model and person photos look more realistic by reducing AI-like skin artifacts, brightening skin, repairing details, and producing higher-resolution outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents working on e-commerce model or person imagery use this skill to run a paid Qinghu image-cleanup workflow through qhkit. The skill guides one-image-at-a-time estimation, user confirmation, submission, polling, and delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uploads model or person images to a paid external service and may consume credits.

Mitigation: Use qhkit estimate first, then confirm the exact image, field values, and estimated credits with the user before generation.

Risk: Using unauthorized person or commercial images can create rights and consent issues.

Mitigation: Use only images the user owns or is authorized to process, especially for commercial use.

Risk: The workflow is optimized for model and person photos, so product-only or scenery images may produce unsuitable results.

Mitigation: Route product-only or scenery images to a more appropriate image-restoration or general realism workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-model-photo-realistic)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, json, markdown]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents through qhkit options, estimate, generate, and status commands; final media URLs are returned by the external workflow status response.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
