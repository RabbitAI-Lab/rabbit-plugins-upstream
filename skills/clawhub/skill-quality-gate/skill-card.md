## Description:

Reviews an agent skill against nine pre-publication quality checks and reports which checks pass or fail.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only); documentation and theory all rights reserved

## Use Case:

Skill authors and marketplace reviewers use it to check a skill directory for required metadata, readable scripts, documentation, bilingual descriptions, trigger guidance, and secret-like content before publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The checker reads local skill files for secret-like patterns and compiles Python files.

Mitigation: Run it only on skill directories you intend to review and check the directory's contents first.

Risk: The release's license label differs from the packaged license notice, which reserves rights in documentation and theory.

Mitigation: Confirm the code and documentation terms fit your marketplace process before installing or redistributing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhaoxinghua09-cell/skills/skill-quality-gate)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Plain-text pass/fail checklist and human-readable guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Nine quality checks with an overall release recommendation]

## Skill Version(s):

1.0.2 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
