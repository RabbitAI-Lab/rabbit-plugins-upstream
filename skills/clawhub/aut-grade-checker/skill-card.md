## Description:

Classifies vehicle driving automation levels for decision support using inputs about driving responsibility and operating-domain limits, with JSON results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, vehicle businesses, and individuals use this tool to estimate a vehicle's driving automation grade and related responsibility boundaries. Results are decision support, not legal advice or regulatory certification, and require human review.

### Deployment Geography for Use:

Global (classification is based on China's GB/T 40429-2021; confirm local applicability)

## Known Risks and Mitigations:

Risk: Classification may not reflect current regulatory text or constitute an authoritative compliance decision.

Mitigation: Verify the result against the current official GB/T 40429-2021 text and obtain human review before relying on it.

Risk: The package's licensing claims conflict across release metadata, code, and documentation.

Mitigation: Confirm the applicable code license and separate documentation and theory rights with the publisher before redistribution.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/aut-grade-checker)
- [LGD theory overview](https://medxpert.cn/theory)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes an L0–L5 grade, responsibility and obligations, source note, warnings, return code, and AIGC metadata.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata; bundled files still say 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
