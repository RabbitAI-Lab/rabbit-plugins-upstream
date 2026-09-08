## Description:

Generates ecommerce marketing assets with Qinghu AI/qhkit, including product images, scene images, detail-page graphics, promotional posters, advertising images, and advertising videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and ecommerce marketing teams use this skill to plan and generate bundled campaign assets for products, promotions, and paid advertising. It routes image and video requests through qhkit, estimates credits before generation, and returns completed asset URLs with usage details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product assets and QHKIT token data may be sent to Qinghu/qhkit services.

Mitigation: Use the skill only after confirming the data-sharing posture is acceptable, and avoid submitting sensitive product assets or credentials outside approved environments.

Risk: The skill installs or upgrades an unpinned global qhkit CLI, which can change behavior across runs.

Mitigation: Prefer a sandboxed or project-local pinned install and review package/version changes before running generation workflows.

Risk: Agent execution of upgrade commands copied from CLI output can introduce unreviewed command changes.

Mitigation: Require separate human verification before executing upgrade commands surfaced by tool output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-marketing-assets)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with qhkit CLI commands, JSON parameters, status summaries, and generated asset URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include credit estimates, task IDs, image URLs, video URLs, and failure messages returned by the CLI.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
