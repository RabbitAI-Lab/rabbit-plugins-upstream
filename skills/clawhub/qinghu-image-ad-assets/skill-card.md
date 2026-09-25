## Description:

Generates Chinese e-commerce marketing image-and-copy assets, including ad images, promotional graphics, and text posts derived from product videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create Chinese e-commerce ad copy, image-generation prompts, advertising images, promotional graphics, and product-seeding text posts from videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can direct an agent to install or upgrade qhkit and Node, which may change the execution environment.

Mitigation: Review and approve install or upgrade commands manually, and prefer a pinned qhkit version before use.

Risk: The skill can guide qhkit token configuration for an external service.

Mitigation: Configure tokens manually or through approved secret-management procedures, and avoid exposing qhkit credentials in chat or logs.

Risk: The skill instructs the agent to relay or act on qhkit command messages.

Mitigation: Do not let the agent run commands copied from qhkit response messages without human review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-image-ad-assets)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and generated asset links when qhkit succeeds]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ad copy variants, image prompts, generated image URLs, qhkit task IDs, credit estimates, and setup or troubleshooting guidance.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
