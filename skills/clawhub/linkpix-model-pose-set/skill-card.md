## Description:

Generates multiple pose and angle variations from one apparel model image for ecommerce product pages and social media marketing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, content creators, and marketing teams use this skill to turn one apparel model photo into a set of pose and viewing-angle variants while keeping the same model, clothing, and commercial photography style.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can direct agents to install or upgrade qhkit and change the local Node/npm environment.

Mitigation: Prefer platform-managed or contained qhkit installation and review install or upgrade steps before allowing them.

Risk: The skill may reuse an existing Qinghu/OpenClaw API token for paid image generation.

Mitigation: Confirm token use and require explicit user approval of model, reference images, image count, size, and estimated credits before generation.

Risk: Generated product images may slightly change key apparel details such as text, logos, or garment structure.

Mitigation: Review generated images against the source product before publishing or using them in commerce.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-model-pose-set)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and generated image URLs from qhkit JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include credit estimates, confirmation prompts before paid generation, and links to generated images after completion.]

## Skill Version(s):

0.1.1 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
