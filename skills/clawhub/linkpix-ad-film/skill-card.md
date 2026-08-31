## Description:

Generates cinematic LinkPix product advertising videos through qhkit workflows for model selection, prompt refinement, pricing estimates, paid-generation confirmation, status polling, and delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agents use this skill to prepare and run LinkPix/qhkit workflows for cinematic product advertising videos. It supports reference-image setup, prompt quality guidance, model option checks, credit estimates, user approval before paid generation, and delivery of generated video results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can upload user-provided product images or audio to the LinkPix service.

Mitigation: Confirm the user is comfortable sharing the selected assets and avoid submitting sensitive media unless the user has approved that use.

Risk: Paid video generation consumes credits and submitted generation tasks cannot be cancelled.

Mitigation: Run an estimate when supported, summarize the model, duration, inputs, and expected credits, and wait for explicit user approval before generation.

Risk: The workflow depends on a qhkit installation and a LinkPix API key.

Mitigation: Use the documented qhkit setup path, store the API key through qhkit configuration or QHKIT_TOKEN, and report configuration failures directly to the user.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-ad-film)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [LinkPix API key tutorial](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash commands and qhkit JSON parameter examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include model labels, reference asset paths, credit estimates, task IDs, status results, and generated video URLs.]

## Skill Version(s):

0.1.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
