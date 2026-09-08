## Description:

This skill helps agents use LinkPix through qhkit to redraw ecommerce product images with translated text while preserving the original layout and design style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators and localization teams use this skill to translate text in product listing images for cross-border sales while keeping the original visual layout. Agents can also use it to install and configure qhkit, estimate generation cost, run image translation jobs, and report generated image URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs agents to install or upgrade a mutable third-party CLI in the global Node environment.

Mitigation: Prefer a reviewed, pinned qhkit version installed locally, and avoid automatic @latest upgrades unless a specific compatibility issue requires them.

Risk: Local product images may be uploaded to the external LinkPix service during generation.

Mitigation: Use the service only for images approved for external processing, and provide the token only when the user intends to run LinkPix jobs.

Risk: Generated image translation can introduce incorrect text, pricing, specifications, logo details, or product structure changes.

Mitigation: Perform manual visual review of every generated image, with special attention to translated text, numbers, brand names, logos, and product details.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-image-translate)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated image URLs and credit usage from qhkit; users should review translated text, prices, specifications, brand names, logos, and product structure before delivery.]

## Skill Version(s):

0.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
