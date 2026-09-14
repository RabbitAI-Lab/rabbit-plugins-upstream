## Description:

This skill helps agents route Qinghu AI workflow requests and use qhkit to estimate, submit, poll, and deliver ecommerce video, image, and data workflow results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to choose and run Qinghu AI workflows for ecommerce video generation, model or apparel image editing, super-resolution, watermark removal, and short-video or creator data tracking. It guides agents through listing available workflows, inspecting required fields, estimating credits, submitting jobs, polling status, and returning generated media links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on a third-party qhkit CLI and external Qinghu workflow service.

Mitigation: Install only when the user intends to use Qinghu workflows, prefer a reviewed or pinned qhkit version, and verify configuration before submitting jobs.

Risk: Workflow submission can upload local media and consume paid credits.

Mitigation: Confirm credit estimates before generation and upload only media the user owns or is authorized to process.

Risk: API tokens may be exposed if pasted directly into shell commands or logs.

Mitigation: Prefer safer secret storage such as existing configuration files or environment variables, and avoid echoing tokens in responses.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-workflow-apps)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON command arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated media URLs and Qinghu credit usage after workflow completion.]

## Skill Version(s):

0.1.5 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
