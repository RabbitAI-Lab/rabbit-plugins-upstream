## Description:

Seedance 2.0 电商带货视频 | LinkPix helps ecommerce, advertising, and livestream teams use qhkit and Qinghu AI to create product-focused short videos from reference images with model selection, cost estimation, task polling, and result download guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, advertising creatives, livestream teams, and agents use this skill to prepare and run qhkit workflows for Seedance 2.0 product videos, including reference-media handling, model option lookup, credit estimation, job submission, status polling, and final video delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may upload product media to Qinghu AI and submit paid video-generation jobs, which can expose commercial assets and consume account credits.

Mitigation: Use approved media and accounts, run qhkit estimate where supported, and confirm model, duration, orientation, reference files, and expected credits before any generate command.

Risk: The skill discusses API-key setup and may prompt users to provide or configure credentials.

Mitigation: Prefer QHKIT_TOKEN or a secure local secret store, avoid pasting API keys into chat, and rotate credentials if exposure is suspected.

Risk: The skill may install qhkit, Node, Pillow, or sharp and otherwise change the local execution environment.

Mitigation: Review installation commands before execution, install dependencies manually where policy requires it, and verify downloaded Node artifacts with the documented checksum step.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-seedance-2-sales)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit task IDs, credit estimates, status summaries, and generated video URLs when jobs complete.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
