## Description:

Fingerprint a project or repository portfolio for listable assets, rank relevant directories, and identify the next asset to build.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orensegal](https://clawhub.ai/user/orensegal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to identify where a project can be listed, understand each listing's requirements, and plan the next useful asset to build.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The catalog includes unpinned npm commands that could run changed or compromised code if followed.

Mitigation: Review commands before use, pin and verify package versions, and use an isolated environment without unrelated credentials for install or publishing steps.

Risk: Scan coverage is partial and does not establish that the artifact is safe.

Mitigation: Treat the scan as incomplete and do not use it as proof of safety.

## Reference(s):

- [Project repository](https://github.com/OrenSegal/visibility)
- [ClawHub skill release](https://clawhub.ai/orensegal/skills/visibility-plan)

## Skill Output:

**Output Type(s):** [Markdown, CSV, Guidance, Shell commands]

**Output Format:** [Markdown planning files and a CSV ledger]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates project facts, an asset scan, a ranked visibility plan, and a submission ledger under .visibility/.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
