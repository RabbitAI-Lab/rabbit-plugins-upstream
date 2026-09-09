## Description:

Helps Ozon and Ozon Global sellers generate marketplace-ready product images, carousel sets, detail images, and promotional graphics through Qinghu AI/LinkPix using qhkit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External Ozon sellers and cross-border ecommerce operators use this skill to prepare white-background product images, Russian-language selling-point images, detail-page visuals, carousel sets, and promotional graphics for Ozon marketplace listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Qinghu API keys could be exposed if pasted into chat.

Mitigation: Configure the key locally through QHKIT_TOKEN, qhkit config, or a secure secret store, and avoid sharing the raw token in chat.

Risk: Mutable runtime installs can change qhkit or supporting tool behavior between runs.

Mitigation: Review install commands before use and prefer controlled package versions or a prepared environment for repeatable production workflows.

Risk: Product images are uploaded to Qinghu and generation can spend Qinghu credits.

Mitigation: Confirm selected files, model or template, output count, quality, language, and estimated credits before submitting any generation task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-ozon-image)
- [Publisher profile](https://clawhub.ai/user/autoagc)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key console](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides qhkit setup, option lookup, estimates, approved generation calls, and delivery of returned image URLs.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
