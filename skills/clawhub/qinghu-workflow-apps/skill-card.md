## Description:

Routes agents to Qinghu AI ecommerce workflows through qhkit for video generation, product-image editing, super-resolution, watermark removal, and short-video or creator data tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and ecommerce operators use this skill to select and run Qinghu AI workflows for product videos, ad creatives, image cleanup, image enhancement, watermark removal, and social video or creator data tracking. Agents use it to inspect available workflows, estimate credits, submit jobs, poll status, and return generated media links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can direct an agent to install or update Node/qhkit on the host environment.

Mitigation: Review installation commands before execution and run the skill only in environments where qhkit installation is approved.

Risk: The skill uses a Qinghu API token and can submit paid workflow jobs.

Mitigation: Configure tokens only for intended Qinghu workspaces, run credit estimates before generation, and require user confirmation before paid submissions.

Risk: The skill may upload local image, video, or audio files to Qinghu workflows.

Mitigation: Use only user-owned or authorized media and confirm upload intent before submitting materials to the external service.

Risk: Broad image and video requests could trigger external workflow routing when a user expected local-only assistance.

Mitigation: Confirm that Qinghu workflows are intended before invoking qhkit for ambiguous creative or editing requests.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/qinghu-workflow-apps)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API Keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline bash commands and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit workflow estimates, log IDs, status JSON, and generated media URLs returned by the external service.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
