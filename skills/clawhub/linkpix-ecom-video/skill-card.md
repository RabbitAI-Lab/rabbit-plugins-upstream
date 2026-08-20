## Description:

LinkPix helps agents use the qhkit CLI to create ecommerce product videos, short promotional videos, brand clips, advertising assets, scripts, storyboards, and multi-image video drafts for platforms such as TikTok, Douyin, Amazon, and Shopee.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce operators, and developers use this skill to route video-generation requests to qhkit commands for product videos, ads, storyboards, and quick image-to-video workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install or upgrade global tooling, fetch a Node runtime, and change PATH for the session.

Mitigation: Require explicit user approval before setup or upgrades, and review the qhkit package source and install location before allowing agents to run it.

Risk: The skill can reuse or persist qhkit credentials and upload local media to an external service.

Mitigation: Require explicit approval before credential use or media upload, and confirm that the selected files and account are appropriate for the video job.

Risk: The skill can spend account credits on paid generation jobs.

Mitigation: Estimate costs where supported and confirm the task, model, media, and expected credit spend before submitting generation jobs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-ecom-video)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with qhkit CLI commands and JSON arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task IDs, polling instructions, video URLs, and credit usage when qhkit jobs complete.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
