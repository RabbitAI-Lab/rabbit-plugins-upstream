## Description:

This skill routes agents through Qinghu AI ecommerce workflow applications via qhkit for video generation, image processing, watermark removal, model outfit workflows, and short-video or creator data tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to choose and run Qinghu AI workflow applications for ecommerce media creation, image repair, watermark removal, video enhancement, and daily short-video or creator data tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may direct agents to install or upgrade qhkit and related Node tooling.

Mitigation: Review installation steps before use, prefer a preinstalled or pinned qhkit setup, and require explicit approval for install or upgrade commands.

Risk: The skill uses Qinghu credentials and can upload selected media to Qinghu services.

Mitigation: Use only authorized Qinghu credentials and approved media, and confirm that selected files are appropriate before running workflow commands.

Risk: The skill can submit paid generation jobs that consume Qinghu credits.

Mitigation: Run an estimate first and require explicit user approval of the workflow, parameters, media, and expected credit use before generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-workflow-apps)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON command arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can estimate credits, submit paid workflow jobs after explicit approval, upload selected local media through qhkit, poll workflow status, and return generated media URLs.]

## Skill Version(s):

0.1.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
