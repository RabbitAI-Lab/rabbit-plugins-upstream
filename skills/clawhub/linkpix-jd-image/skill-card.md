## Description:

This skill helps JD.com ecommerce operators generate product listing images, main-image sets, detail images, white-background images, scene images, refined edits, premium posters, marketing KV images, multi-angle displays, and appliance or 3C parameter graphics through Qinghu AI and qhkit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, advertising optimizers, and brand teams use this skill to prepare JD.com-oriented product visuals for listings, detail pages, and campaign graphics. The skill guides agents through qhkit option lookup, image generation, estimation, credential setup, and result delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may download and run mutable npm, Node, or Python packages during setup.

Mitigation: Use an isolated environment and prefer pinned, reviewed dependency versions before installation.

Risk: The skill requires qhkit credentials or API keys for Qinghu AI access.

Mitigation: Configure credentials through secure local secret storage or environment variables rather than pasting secrets into chat.

Risk: The skill uploads selected product images to Qinghu AI for generation workflows.

Mitigation: Upload only images approved for third-party processing and avoid sensitive, confidential, or rights-restricted product assets.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-jd-image)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated image URLs, credit estimates, actual credit usage, and qhkit JSON responses when the underlying tool is run.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
