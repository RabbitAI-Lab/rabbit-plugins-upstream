## Description:

AI 自动优化商品主图的构图、光影、质感及细节，提升商品吸引力与点击率。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and commerce operators use this skill to guide an agent through optimizing product listing images with Qinghu AI's qhkit CLI. It helps choose generation modes, estimate credits, run image generation, and return generated image URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill permits installing or upgrading the external qhkit CLI.

Mitigation: Use a pinned, isolated qhkit installation and review installation commands before execution.

Risk: Selected images are uploaded to Qinghu's third-party service for generation.

Mitigation: Ask for confirmation before uploads and avoid using confidential or sensitive product images unless the user has approved that service.

Risk: Paid API-token based generation may spend credits.

Mitigation: Run qhkit image estimate before generation and confirm credit spending when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-main-image-optimize)
- [Publisher profile](https://clawhub.ai/user/autoagc)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Markdown]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce third-party image generation URLs and credit usage summaries after qhkit execution.]

## Skill Version(s):

0.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
