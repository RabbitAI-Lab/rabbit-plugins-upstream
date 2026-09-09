## Description:

Guides agents through using Qinghu qhkit to create Seedance 2.0 e-commerce product videos from product images and selling points, including model discovery, estimation, task submission, polling, and delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External commerce operators, ad creative teams, livestream teams, and their agents use this skill to prepare Seedance 2.0 product showcase videos for marketplace listings, short-form ads, and social commerce campaigns. It helps select live qhkit model labels, estimate credits, submit video jobs, poll status, and deliver generated video results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask for a Qinghu API key and could expose credentials if users paste secrets into chat.

Mitigation: Use a minimally scoped Qinghu API key when available, configure credentials locally or through QHKIT_TOKEN, and avoid pasting secrets into chat.

Risk: The skill can propose qhkit, Node, npm install, and upgrade commands that alter the local environment.

Mitigation: Review the exact package names, registry, download source, and upgrade command before approving installation or execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-seedance-2-sales)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON CLI payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit status summaries, estimated credit use, task IDs, and generated video URLs.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
