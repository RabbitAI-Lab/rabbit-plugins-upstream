## Description:

Creates 3D models, textures, animations, and converted assets, and prepares models for physical 3D printing through Meshy workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arlieeee](https://clawhub.ai/user/arlieeee)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and 3D creators use this skill to generate, texture, rig, animate, convert, and prepare digital models and physical print assets using Meshy workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, photos, and models selected for a job are sent to Meshy, and cloud work can consume account credits.

Mitigation: Use inputs suitable for sharing and agree on a credit budget before submitting cloud work.

Risk: Session credentials and signed asset URLs can expose account access or private assets if shared.

Mitigation: Keep tokens, credential files, and signed asset URLs private.

Risk: The separately installed Meshy CLI implementation is outside the security review described in the release evidence.

Mitigation: Review the CLI package and its behavior before using it with sensitive files or account access.

## Reference(s):

- [Project homepage](https://github.com/meshy-dev/meshy-3d-agent)
- [Meshy pricing documentation](https://docs.meshy.ai/en/api/pricing)
- [Setup and sign-in](artifact/references/setup.md)
- [3D asset pipelines](artifact/references/pipelines.md)
- [Rigging and animation](artifact/references/animation.md)
- [Physical printing workflows](artifact/references/printing.md)
- [Creative Lab products](artifact/references/creative-lab.md)
- [Delivery and costs](artifact/references/delivery.md)
- [Troubleshooting](artifact/references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Guidance]

**Output Format:** [3D asset and print files (including GLB, OBJ, STL, and 3MF), with workflow guidance and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated asset formats and print preparation steps depend on the requested workflow.]

## Skill Version(s):

0.9.1 (source: server-resolved ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
