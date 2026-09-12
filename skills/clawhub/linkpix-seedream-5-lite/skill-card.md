## Description:

This skill helps agents use qhkit to prepare, price, and run Seedream 5.0 Lite / Qwen-Image style image generation workflows for Chinese e-commerce product images, main images, posters, and promotional graphics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, designers, shop managers, and their agents use this skill to generate Chinese-language product main images, sale posters, campaign graphics, and visual variants through qhkit. The skill is oriented toward workflows that need readable Chinese text, reference-image handling, cost estimation, and explicit confirmation before paid image generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can expose a qhkit API token if a user pastes it into chat.

Mitigation: Use a platform secret store, an environment variable, or a local command run by the user instead of sending API keys through chat.

Risk: The workflow includes broad or unpinned install paths for qhkit and image-processing tools.

Mitigation: Prefer pinned, reviewed package versions and avoid sudo or global installs where possible.

Risk: The workflow can upload images and submit paid generation jobs.

Mitigation: Confirm the exact model, image count, size, quality, reference images, and estimated credit cost before generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-seedream-5-lite)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash and JSON command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide qhkit setup, prompt polishing, model selection, credit estimation, image upload, and paid image generation after user confirmation.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
