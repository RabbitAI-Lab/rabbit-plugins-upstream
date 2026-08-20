## Description:

Uses the qhkit CLI to extract print patterns from apparel or product images into high-resolution, tiled bitmap design assets for POD customization and apparel design.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and ecommerce design teams use this skill when they need an agent to turn product or clothing photos into reusable POD print-pattern assets through qhkit. The skill also guides the agent to explain bitmap and copyright limitations when users request vector assets or branded designs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source images may be uploaded to the qhkit service during pattern extraction.

Mitigation: Use the skill only with images approved for that service and confirm privacy or data-handling requirements before processing sensitive product imagery.

Risk: The skill may reuse an existing Qinghu/OpenClaw token and can spend account credits.

Mitigation: Use an explicitly approved qhkit configuration, check estimates before generation when reporting cost matters, and monitor available account credits.

Risk: Automatic setup instructions can install Node binaries or global npm packages.

Mitigation: Prefer a preinstalled or administrator-approved qhkit setup, and review installation commands before allowing broad system changes.

Risk: Generated pattern images can differ slightly from the source print and may raise copyright concerns for branded or IP-protected designs.

Mitigation: Review output against key visual elements before use and flag obvious brand or IP designs for rights clearance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-pod-pattern-extract)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu LinkPix workbench](https://www.iqinghu.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and returned image URLs or JSON status messages.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated assets are bitmap pattern images; the skill instructs agents to report actual credit usage and CLI failure messages.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
