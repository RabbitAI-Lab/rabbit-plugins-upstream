## Description:

根据商品自动生成真实、高质感的商品场景图，适用于家居、美妆、服饰、数码等行业。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and commerce teams use this skill to guide an agent in producing product scene-image prompts and qhkit image-generation commands for product detail pages, ads, and lifestyle marketing materials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade a third-party CLI globally.

Mitigation: Review before installing, prefer a pinned local qhkit install in an isolated environment, and confirm before install or upgrade.

Risk: The skill handles Qinghu tokens and uploads product images to an external service.

Mitigation: Use protected secret handling for the Qinghu token and upload only product images approved for the Qinghu service.

Risk: The skill text suggests following upgrade commands emitted by the CLI.

Mitigation: Do not execute upgrade commands copied directly from CLI output; verify the package and version through trusted package-management channels first.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-scene-image)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides qhkit image generation and returns product-image delivery guidance; actual image URLs are produced by the external qhkit service.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
