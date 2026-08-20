## Description:

LinkPix guides agents to use the qhkit CLI for Qinghu media workflows that generate ecommerce images, videos, advertising assets, POD designs, storyboards, translated or edited videos, and related workflow outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to decide when LinkPix/qhkit applies, choose the right media-generation command, prepare JSON parameters, estimate credit use, submit tasks, poll status, and present generated images, videos, scripts, text, or data outputs to end users.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill instructs agents to perform global npm installs or upgrades for qhkit.

Mitigation: Ask the user to confirm before installing or upgrading qhkit, and explain permission or network failures instead of retrying silently.

Risk: The skill can use a Qinghu/LinkPix account token and submit tasks that spend credits.

Mitigation: Confirm intent and relevant cost estimates before submitting credit-consuming generation tasks.

Risk: The skill can upload local media files to Qinghu services.

Mitigation: Confirm before uploading private or sensitive assets, and only upload files needed for the requested task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with qhkit command examples and JSON parameter payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may lead an agent to install or upgrade qhkit, upload local media to Qinghu services, estimate or spend credits, and poll long-running generation tasks.]

## Skill Version(s):

0.1.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
