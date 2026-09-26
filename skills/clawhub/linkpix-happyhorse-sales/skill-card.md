## Description:

Helps ecommerce, brand, livestream commerce, and commercial content teams generate HappyHorse 1.1 product-marketing videos through LinkPix and qhkit from prompts plus optional image, video, or audio references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, brand teams, livestream commerce teams, and commercial creators use this skill to prepare, estimate, submit, poll, and deliver short product videos for advertising, product display, social commerce, and marketplace listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install npm and Node tooling or alter PATH configuration on the local system.

Mitigation: Use a sandbox or preinstalled qhkit where possible, review installation commands before execution, and avoid persistent PATH changes unless approved.

Risk: Selected product images, videos, or audio may be uploaded to the qhkit provider during generation.

Mitigation: Confirm that referenced media is approved for upload before running generation commands.

Risk: The skill needs qhkit credentials and may store an API token locally.

Mitigation: Provide tokens through a trusted secret mechanism when available and avoid exposing credentials in chat logs or shell history.

Risk: Generation commands can consume credits and create tasks that cannot be canceled.

Mitigation: Review model, duration, media inputs, orientation, and estimated credits with the user before submitting generation requests.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-happyhorse-sales)
- [AutoAGC publisher profile](https://clawhub.ai/user/autoagc)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key console](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)
- [Qinghu API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, JSON]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce task IDs, status summaries, credit estimates, and generated video URLs returned by qhkit.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
