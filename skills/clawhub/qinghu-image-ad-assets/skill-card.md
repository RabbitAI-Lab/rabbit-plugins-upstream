## Description:

Generates ecommerce image-and-text marketing assets, including ad images, promotional posters, and product-seeding copy derived from videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, ecommerce operators, and agent users use this skill to create advertising images, promotion graphics, and product-seeding text for ecommerce campaigns. The skill guides an agent through qhkit setup, generation commands, polling, credit reporting, and delivery of generated media URLs and copy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send selected product images, videos, prompts, and marketing content to Qinghu's qhkit service.

Mitigation: Confirm media uploads with the user, avoid sensitive assets, and disclose that generated outputs depend on the external service.

Risk: The skill directs installation or upgrade of a Node/npm CLI on the host.

Mitigation: Prefer a sandbox or project-local pinned install and review install or upgrade commands before execution.

Risk: The skill requires API-token configuration for qhkit.

Mitigation: Use protected secret handling such as QHKIT_TOKEN and avoid exposing tokens in commands, logs, or shared transcripts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-image-ad-assets)
- [ClawHub publisher profile](https://clawhub.ai/user/autoagc)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with qhkit commands, JSON parameters, generated media URLs, credit usage, and generated marketing copy.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires qhkit, a Qinghu API token or QHKIT_TOKEN, and review of generated image text before delivery.]

## Skill Version(s):

0.1.0 (source: evidence.json release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
