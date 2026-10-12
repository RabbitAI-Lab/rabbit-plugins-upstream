## Description:

Helps agents create multiple product video ads for feed placements, brand campaigns, and social media using LinkPix's qhkit tool.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Marketers and creative teams use this skill to prepare and generate batches of product video ads for different channels and placements, with a cost estimate before submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may prompt agents to install or upgrade software and change the shell environment.

Mitigation: Preinstall and pin qhkit; require confirmation before installs, upgrades, or PATH changes.

Risk: Generating videos can spend paid credits, including when producing batches.

Mitigation: Estimate costs and obtain approval before submitting each generation job.

Risk: Selected media assets are uploaded to the service and a service token is needed.

Mitigation: Review assets before upload and use a scoped token; avoid exposing it in shared outputs.

## Reference(s):

- [LinkPix video ad skill on ClawHub](https://clawhub.ai/autoagc/skills/linkpix-video-ad-assets)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Video asset links]

**Output Format:** [Markdown with command examples, task status, and video links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports estimated or charged credits and task IDs when available.]

## Skill Version(s):

0.1.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
