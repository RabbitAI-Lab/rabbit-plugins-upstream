## Description:

Guides agents in replacing models or faces in e-commerce images and people in videos using Qinghu AI while aiming to preserve the original product presentation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams and content creators use this skill to localize product images by changing a model's appearance and to replace a person in a video. It provides instructions for using Qinghu AI's qhkit service, including account setup, estimates, and delivery of generated results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using a real person's likeness without permission can misuse their identity.

Mitigation: Confirm authorization to use the likeness before generating a replacement; decline unauthorized requests.

Risk: Source images and videos are uploaded to Qinghu's service, and an account token is needed.

Mitigation: Confirm the user accepts media upload and account use; keep the token private.

Risk: Installing or updating qhkit through npm or npx may fetch unreviewed versions.

Mitigation: For tighter supply-chain control, install a reviewed, pinned qhkit version.

Risk: Generative replacement may alter clothing details, text, logos, or product structure.

Mitigation: Inspect generated results against the source before using them in product listings.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-model-face-swap)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu AI API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Image and video links]

**Output Format:** [Markdown with CLI examples and links to generated media]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images and videos may require review for fidelity to the original product.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
