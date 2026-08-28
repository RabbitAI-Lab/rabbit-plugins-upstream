## Description:

LinkPix helps agents translate ecommerce creative requests into Qinghu qhkit CLI actions for AI-generated product images, marketing videos, ad assets, POD designs, scripts, translations, media edits, and workflow outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users, commerce teams, and agent developers use this skill to choose and run qhkit commands for ecommerce media creation and editing. It is intended for product images, main images, detail pages, ad videos, video translation, watermark or subtitle removal, POD assets, storyboard scripts, and Qinghu workflow tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send user-provided images, videos, audio, links, and Qinghu API credentials to the qhkit service for processing.

Mitigation: Use it only with media and credentials the user is authorized to share with Qinghu, and limit submitted assets to the specific task.

Risk: Face replacement, watermark or subtitle removal, and popular-video replication can implicate consent, copyright, brand, or platform rules.

Mitigation: Confirm rights and consent before running those actions, and avoid using the workflows to bypass watermarks or copy protected material without permission.

Risk: Generation actions may consume paid Qinghu credits and submitted tasks may not be cancellable.

Mitigation: Run estimate where supported and obtain explicit user approval for model or template, count or duration, reference media, and expected credits before any generate action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu workbench](https://www.iqinghu.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with qhkit command examples, JSON parameters, and status/result handling instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May lead qhkit to return images, videos, scripts, translated text, data files, media URLs, task IDs, and credit usage.]

## Skill Version(s):

0.1.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
