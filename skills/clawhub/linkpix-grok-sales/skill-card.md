## Description:

Guides agents through using qhkit and Qinghu AI to create Grok-oriented e-commerce product videos from product images, prompts, and campaign requirements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, content teams, and their agents use this skill to prepare product-video prompts, select available qhkit video models, estimate generation cost, submit approved jobs, poll status, and return generated video links for social commerce campaigns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys may be exposed if users paste credentials directly into chat.

Mitigation: Configure the Qinghu token through a secure secret mechanism, environment variable, or out-of-band terminal flow.

Risk: The skill can install or upgrade unpinned host tooling.

Mitigation: Review installation commands first and run the skill in an isolated or low-risk environment.

Risk: Selected product media and prompts may be uploaded to an external video service and paid generation may consume credits.

Mitigation: Avoid sensitive media and require explicit user approval before submitting any paid generation task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-grok-sales)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key console](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Markdown, Text]

**Output Format:** [Markdown with inline bash commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit JSON responses, task identifiers, credit estimates, status updates, and generated video URLs.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
