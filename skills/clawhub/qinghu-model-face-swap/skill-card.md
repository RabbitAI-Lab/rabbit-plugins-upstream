## Description:

This skill helps agents replace or localize models and faces in ecommerce images and videos while preserving clothing, pose, composition, and lighting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers and content operators use this skill to guide authorized model or face replacement for product images and videos, including localization by market, age, or skin tone.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a third-party qhkit CLI that may be installed globally or upgraded to @latest.

Mitigation: Use a reviewed pinned package version where possible, avoid automatic latest-version upgrades, and install in a constrained environment.

Risk: The workflow handles user media files and a Qinghu API token.

Mitigation: Run the skill in a restricted workspace, provide only task-specific media, and protect or rotate the API token if exposure is suspected.

Risk: Face or model replacement can misuse a real person's likeness.

Mitigation: Confirm the user has rights to use the likeness before processing and refuse unauthorized face replacement requests.

Risk: Generated edits may alter details such as text, logos, product structure, or identity cues.

Mitigation: Review generated outputs for key commercial and identity details before publication or delivery.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-model-face-swap)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [AutoAGC publisher profile](https://clawhub.ai/user/autoagc)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with qhkit command examples and JSON parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated image or video URLs, task IDs, status updates, and credit usage reported by the qhkit service.]

## Skill Version(s):

0.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
