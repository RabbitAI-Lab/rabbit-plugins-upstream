## Description:

Guides agents in extracting garment and product prints into high-resolution, flattened pattern artwork using Qinghu AI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Designers and POD sellers use this skill to turn prints in clothing or product photos into reusable, flattened bitmap artwork. The agent provides setup and generation guidance and returns the resulting image link when available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected source images are uploaded to the Qinghu service for generation.

Mitigation: Upload only images approved for sharing with that service.

Risk: Installing or upgrading qhkit introduces a package supply-chain dependency.

Mitigation: Review the package and prefer a pinned version in sensitive environments; avoid persistent PATH changes unless needed.

Risk: Generative redraws may alter print details, and branded patterns may carry intellectual-property restrictions.

Mitigation: Check important visual details and confirm rights before reusing the output.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-pod-pattern-extract)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu AI](https://www.iqinghu.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Image URLs]

**Output Format:** [Markdown text with commands and an image link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Resulting artwork is a white-background bitmap, not a vector or transparent layer; generated details may differ from the source.]

## Skill Version(s):

0.1.1 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
