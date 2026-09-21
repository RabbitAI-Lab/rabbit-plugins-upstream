## Description:

LinkPix helps agents use Qinghu AI media tools to generate and edit ecommerce images, videos, ad creatives, product-detail pages, POD print materials, storyboards, and short-video or creator data analyses through qhkit workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and ecommerce content teams use LinkPix to route media-production requests to qhkit commands for product images, batch edits, videos, translations, watermark or subtitle removal, storyboards, ad assets, POD print materials, and data-analysis workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to provide an API key during setup.

Mitigation: Use secure secret storage or the QHKIT_TOKEN environment variable instead of pasting API keys into chat whenever possible.

Risk: The skill can upload local media for image, video, face, watermark, subtitle, replication, and translation tasks.

Mitigation: Confirm exactly which files will be uploaded and verify rights, consent, and privacy expectations before submitting a qhkit task.

Risk: The skill installs or runs current npm packages rather than fixed reviewed versions.

Mitigation: Review the package source and installation command before use, and prefer pinned, reviewed package versions in controlled environments.

Risk: Some qhkit actions create tasks and consume credits.

Mitigation: Run estimate actions first and obtain explicit user confirmation for model, template, media inputs, quantity, duration, quality, language, and expected credits before generate or script actions.

## Reference(s):

- [LinkPix ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu Workbench](https://www.iqinghu.com)
- [Qinghu Workbench API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with qhkit command examples, JSON parameter examples, media URLs, task identifiers, status summaries, and generated text when a qhkit workflow returns text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill may upload local media through qhkit, reads live model or template options, estimates credits before paid submissions, and reports one-line JSON command results or failure messages.]

## Skill Version(s):

0.1.15 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
