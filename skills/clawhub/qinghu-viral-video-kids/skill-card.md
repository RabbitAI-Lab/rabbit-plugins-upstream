## Description:

This skill guides an agent through Qinghu AI's qhkit workflow to create children's clothing short videos by transferring motion from a reference video to a provided child model image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce creators, apparel marketers, and content operators use this skill to prepare paid Qinghu AI video-generation jobs for children's clothing promotion. It helps agents collect authorized video and image inputs, estimate costs, submit the workflow after user approval, poll status, and return generated media links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference videos and child model images are uploaded to Qinghu AI for processing.

Mitigation: Use only authorized materials, obtain guardian authorization for any minor depicted, and proceed only when the user accepts Qinghu AI processing.

Risk: Workflow submission is paid and may consume credits.

Mitigation: Run an estimate first, present the selected workflow, inputs, and expected credit cost, and submit only after explicit user approval.

Risk: The qhkit package and Qinghu API key are required to run the workflow.

Mitigation: Review package installation steps before use and provide a Qinghu API key only in trusted environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-viral-video-kids)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Qinghu workflow status details, generated media URLs, and final credit consumption when a job completes.]

## Skill Version(s):

0.1.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
