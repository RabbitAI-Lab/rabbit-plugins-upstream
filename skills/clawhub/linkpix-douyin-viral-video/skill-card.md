## Description:

Helps agents create Douyin-oriented ecommerce short-video workflows with qhkit, including model selection, prompt shaping, asset upload, credit estimation, task polling, and result delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce operators, and agent users use this skill to prepare Douyin product videos, live-stream clips, review-style videos, and promotional short-form video jobs through LinkPix/qhkit. The skill guides setup, model discovery, user confirmation before paid generation, polling, and delivery of generated video URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or update qhkit and Node tooling in the user's environment.

Mitigation: Install only after reviewing the dependency path and use the documented qhkit package source.

Risk: Media provided by the user may be uploaded to the Qinghu/LinkPix service for generation.

Mitigation: Use only assets the user is comfortable sending to that external service.

Risk: Video generation can consume account credits and requires a qhkit API token.

Mitigation: Confirm the model, assets, duration, orientation, language, and estimated credits before any generate step.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-douyin-viral-video)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown]

**Output Format:** [Markdown with inline shell commands and JSON command arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May result in qhkit task IDs, credit estimates, status checks, and generated video URLs after user-approved paid generation.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
