## Description:

Generates professional infographics with varied layouts and visual styles by analyzing content, expanding prompts when needed, generating images, and optionally reviewing quality across rounds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sensenova-skills](https://clawhub.ai/user/sensenova-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn English or Chinese infographic, diagram, visual-summary, or data-visualization requests into generated infographic images with optional prompt expansion and quality review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad infographic and visualization triggers may send user prompts, URLs, or structured data to configured SenseNova model services.

Mitigation: Review before use with sensitive prompts, private URLs, or regulated data, and narrow invocation triggers where the deployment requires tighter control.

Risk: Intermediate files are stored under a predictable temporary workspace path.

Mitigation: Use the skill only on trusted local machines or update the deployment to use a private temporary directory with restrictive permissions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sensenova-skills/skills/sn-infographic)
- [Analysis framework](references/analysis-framework.md)
- [Runtime parameters](references/runtime-parameters.md)
- [Layout and style selection rules](references/layout-style-selection.md)
- [Evaluation standard](references/evaluation-standard.md)
- [Prompt expansion system prompt](references/prompts-expand-system.md)
- [Prompt critic system prompt](references/prompts-critic-system.md)
- [Structured content template](references/structured-content-template.md)
- [Base prompt](references/base-prompt.md)

## Skill Output:

**Output Type(s):** [Text, Files, JSON]

**Output Format:** [Plain text or Markdown-style status text plus generated PNG image files; verbose mode includes quality ranking and timing details.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports friendly and verbose output modes, max_rounds from 1 to 8, and explicit or inferred aspect ratio and image size.]

## Skill Version(s):

2026.9.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
