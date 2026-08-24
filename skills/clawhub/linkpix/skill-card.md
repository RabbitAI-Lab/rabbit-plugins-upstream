## Description:

LinkPix helps agents use the qhkit CLI to route ecommerce media requests into Qinghu AI workflows for product images, ad creatives, videos, translations, edits, storyboards, POD assets, and task status checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers, marketers, and agent operators use this skill to choose and run qhkit commands for generating or editing product imagery, ad videos, translated media, storyboards, POD assets, and marketplace-ready creative batches. It is intended for authorized commercial media workflows that may require API credentials, uploads, estimates, paid task confirmation, and status polling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local media files may be uploaded to Qinghu/qhkit services during generation, editing, translation, or workflow estimation.

Mitigation: Use only media the user owns or is authorized to process, disclose upload behavior before use, and avoid sending sensitive media unless the deployment has approved handling terms.

Risk: Generation actions can create paid tasks or consume account credits.

Mitigation: Run an estimate when available and require explicit user confirmation of model, inputs, output count or duration, and expected credits before any paid task is submitted.

Risk: The skill may require API keys or credential persistence for qhkit access.

Mitigation: Prefer managed secrets or environment variables, avoid asking users to paste API keys in chat when a safer channel exists, and rotate credentials if exposure is suspected.

Risk: Media-manipulation capabilities such as face replacement, watermark removal, subtitle removal, and viral-video recreation can create rights, consent, or authenticity concerns.

Mitigation: Limit use to authorized content and review requests and outputs for consent, intellectual-property, marketplace, and platform-policy compliance.

Risk: The skill includes host setup and package installation guidance for qhkit and supporting runtimes.

Mitigation: Review install commands before deployment, use trusted package sources approved by the environment, and restrict installation privileges where possible.

## Reference(s):

- [LinkPix ClawHub skill](https://clawhub.ai/autoagc/skills/linkpix)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu website](https://www.iqinghu.com)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON parameter examples; qhkit commands return one-line JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may include local media upload paths, task estimates, paid generation confirmation steps, and status polling instructions.]

## Skill Version(s):

0.1.10 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
