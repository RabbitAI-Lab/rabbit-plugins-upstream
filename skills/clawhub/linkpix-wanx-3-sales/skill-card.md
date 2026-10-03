## Description:

Helps Taobao, Tmall, 1688 merchants, and Alibaba ecosystem operators use Qinghu AI and qhkit to create Alibaba Wanx 3.0 ecommerce sales videos from text, product images, and detailed product prompts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce merchants, store operators, and agents assisting them use this skill to plan, configure, estimate, submit, poll, and deliver short product-sales video generation tasks through Qinghu AI/qhkit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or update unpinned npm or Python tooling and alter the agent runtime environment.

Mitigation: Review installation steps before execution, prefer pinned package versions, and avoid persistent PATH or shell-startup changes unless required.

Risk: The skill handles Qinghu API tokens and can upload product images, videos, or audio to an external service.

Mitigation: Use scoped credentials where possible, confirm media upload is acceptable before running commands, and remove stored tokens when the workflow is complete.

Risk: Video generation can spend service credits and submitted tasks may not be cancellable.

Mitigation: Run estimates when supported, present key parameters and expected credits to the user, and require explicit approval before generation commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-wanx-3-sales)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline JSON and bash command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit commands for options lookup, estimates, video generation, task status polling, media handling, and token configuration.]

## Skill Version(s):

0.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
