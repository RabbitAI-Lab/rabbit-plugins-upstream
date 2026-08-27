## Description:

AI电商工作流应用 | 青虎AI helps agents choose and run Qinghu AI ecommerce workflows through qhkit for video creation, image processing, model clothing changes, and short-video or creator data tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents supporting ecommerce creators or operators use this skill to select Qinghu workflows, prepare qhkit commands, estimate paid credit usage, submit approved jobs, poll status, and deliver generated media or data links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install Node or the qhkit package on the host system.

Mitigation: Review before installing and prefer an isolated environment or administrator-managed qhkit installation.

Risk: The skill may request an API key in chat.

Mitigation: Configure credentials outside chat where possible, such as through managed environment variables or approved local configuration.

Risk: Workflow jobs can upload local media to Qinghu and consume paid credits.

Mitigation: Use the skill only for intentional Qinghu workflows, confirm authorized media use, run estimates before submission, and require explicit approval before paid generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-workflow-apps)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu workbench login](https://www.iqinghu.com/workbench/login?urlCode=agentch)
- [Qinghu API keys page](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Markdown, Text]

**Output Format:** [Markdown with inline bash and JSON command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit workflow parameters, cost estimates, job status summaries, and generated media or data URLs.]

## Skill Version(s):

0.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
