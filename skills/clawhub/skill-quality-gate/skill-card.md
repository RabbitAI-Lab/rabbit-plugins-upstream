## Description:

Checks a skill directory against nine publication-readiness criteria and reports which checks pass or fail.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT for Python code; documentation and theory all rights reserved

## Use Case:

Skill authors and developers use this gate before publishing to check required metadata, documentation, scripts, and potential sensitive content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The checker reads the selected skill directory and may compile its Python scripts.

Mitigation: Point it only at a directory you are comfortable inspecting and compiling.

Risk: A failed check may not produce a failing process exit status.

Mitigation: Inspect the reported pass/fail results and block publication when any check fails rather than relying on the exit status.

Risk: The code and accompanying documentation have different reuse terms.

Mitigation: Review the included license scope before redistributing documentation or theory text.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/skill-quality-gate)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Plain-text pass/fail checklist and publication recommendation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Nine checks; results require human review before publication.]

## Skill Version(s):

1.0.3 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
