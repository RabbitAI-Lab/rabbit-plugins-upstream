## Description:

Generates product mockup images by applying print patterns to apparel, hats, mugs, and similar merchandise with perspective, lighting, and fabric-aware visual blending.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce, print-on-demand, and product-design users invoke this skill to turn a supplied pattern and optional product image into realistic merchandise mockups. Agents use it to prepare qhkit image-generation commands, check supported options, estimate credits, and return generated image URLs to the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup and upgrade flow can install or change Node, npm packages, registries, PATH entries, and qhkit versions in the local environment.

Mitigation: Require approval before installs, upgrades, Node setup, registry mirror use, or PATH changes; prefer the least-privileged install path that is sufficient for the task.

Risk: qhkit receives the images and prompts used to create product mockups.

Mitigation: Use the skill only when the user is comfortable sending those assets to qhkit, and avoid submitting sensitive or confidential images unless explicitly approved.

Risk: The artifact describes upgrade commands that may be suggested by remote command responses.

Mitigation: Manually review upgrade commands from remote output before execution instead of running copied response text automatically.

Risk: Token setup can expose credentials if entered directly into shell history or shared logs.

Mitigation: Prefer an environment variable or secret manager for the qhkit token, and avoid echoing or storing the token in plaintext command transcripts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-pod-pattern-apply)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu AI workbench](https://www.iqinghu.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit-generated image URLs, estimated or actual credit usage, and user-facing failure messages returned by the CLI.]

## Skill Version(s):

0.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
