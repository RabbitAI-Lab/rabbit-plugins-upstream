## Description:

Helps 1688 wholesalers, source factories, and B2B operators use Qinghu AI through qhkit to generate product main images, carousel sets, detail-page images, and promotional campaign images for 1688 commerce workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External B2B commerce operators and agents use this skill to prepare 1688-ready product imagery, including factory-style main images, white-background images, parameter and detail breakdowns, multi-SKU layouts, watermark-protected images, and promotional posters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install, upgrade, or execute unpinned third-party qhkit tooling on the user's machine.

Mitigation: Review the Qinghu/qhkit supply chain first and prefer a preinstalled, pinned qhkit version instead of automatic installation or upgrades.

Risk: Product images may be uploaded to the Qinghu/qhkit service during generation.

Mitigation: Use the skill only with images approved for that service and avoid confidential, regulated, or customer-sensitive product assets unless the upload is authorized.

Risk: The skill text asks for API key handling in chat-oriented flows.

Mitigation: Do not paste API keys into chat; configure credentials through a private secret store, local terminal flow, or environment variable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-1688-image)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with qhkit shell commands and JSON parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The qhkit workflow can return generated image URLs and credit usage after task completion.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
