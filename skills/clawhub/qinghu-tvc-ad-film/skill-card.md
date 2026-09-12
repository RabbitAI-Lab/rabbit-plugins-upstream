## Description:

Guides an agent through QinghuAI/qhkit workflow commands to generate cinematic TVC-style brand advertising videos from 1 to 8 product images, product details, audience, scene, style, language, and aspect-ratio inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to prepare paid product-advertising video generation requests, estimate credits, submit qhkit workflow jobs, poll status, and return the generated TVC video URL. It is intended for brand ads, product promos, cinematic ad assets, multilingual variants, and horizontal or vertical campaign materials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup can install or run an unpinned mutable npm CLI, including latest and npx execution paths.

Mitigation: Prefer a pinned, reviewed qhkit version with user-scoped installation before using the workflow.

Risk: The workflow handles user media and credentials for a paid video-generation service.

Mitigation: Use only media the user is authorized to upload, configure credentials in user-scoped settings, and avoid exposing tokens in shared logs or prompts.

Risk: Generation consumes Qinghu credits and may be costly.

Mitigation: Run the qhkit estimate command with the exact generation parameters and obtain user confirmation before submitting a generate request.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-tvc-ad-film)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Publisher profile](https://clawhub.ai/user/autoagc)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON workflow parameters, and generated media URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses qhkit workflow commands for options, estimate, generate, and status; generation should proceed only after credit estimate confirmation.]

## Skill Version(s):

0.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
