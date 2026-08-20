## Description:

青虎AI workflow for creating door-opening outfit-change videos from one model image, up to four clothing images, and optional audio for fashion and commerce content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, commerce teams, and agent operators use this skill to prepare and run a Qinghu AI workflow that generates short outfit-change videos, confirms credit estimates before paid submission, and returns generated media URLs after polling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow requires installing and running the qhkit CLI.

Mitigation: Confirm the user accepts adding qhkit before installation and surface installation or configuration errors plainly.

Risk: The workflow requires a Qinghu API token and uploads model, clothing, and optional audio assets to Qinghu.

Mitigation: Ask the user to confirm token use and asset upload, and avoid proceeding when the user is not comfortable sharing those materials.

Risk: Generation is chargeable and may consume Qinghu credits.

Mitigation: Run a live estimate with the same parameters, show the credit estimate, and wait for explicit user approval before submitting generation.

Risk: Model likenesses, clothing images, and audio may require rights or consent for commercial use.

Mitigation: Remind the user to use owned or authorized assets before submitting a commercial generation job.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-door-outfit-change)
- [AutoAGC publisher profile](https://clawhub.ai/user/autoagc)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, JSON parameter examples, and generated media URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires qhkit, a Qinghu API token, user-supplied model and clothing assets, credit estimate confirmation before generation, and polling until the paid workflow completes.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
