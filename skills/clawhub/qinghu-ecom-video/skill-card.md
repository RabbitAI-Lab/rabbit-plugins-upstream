## Description:

Guides agents through creating Qinghu AI e-commerce videos, product promotions, and storyboards from prompts or images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams and creators use this skill to plan product-video scripts, select generation options, and request promotional videos for e-commerce channels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill prompts installation or upgrades of persistent Node and qhkit tooling before use.

Mitigation: Approve setup explicitly; prefer a pinned or preinstalled qhkit version and avoid shell startup changes unless desired.

Risk: Generating videos requires a Qinghu API token and may upload selected media files to the Qinghu service.

Mitigation: Configure the token securely and review which media files are shared before submitting a job.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-ecom-video)
- [qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown with command examples and generated-video links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated videos are delivered by link after asynchronous processing; credits may apply.]

## Skill Version(s):

0.1.3 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
