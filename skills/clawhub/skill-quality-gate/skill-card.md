## Description:

Checks nine quality dimensions of a local skill directory before release and reports pass/fail results with fix guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and release reviewers use this local checklist to check skill packaging, bilingual documentation, basic secret patterns, and release readiness before publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Checking a directory reads local skill files and Python compilation may create cache files.

Mitigation: Run against only the intended skill directory and review any generated cache files.

Risk: The bilingual English/Chinese requirement can reject skills that intentionally use one language.

Mitigation: Use this gate when bilingual documentation is required and review failed checks in context.

## Reference(s):

- [Skill Quality Gate on ClawHub](https://clawhub.ai/zhaoxinghua09-cell/skills/skill-quality-gate)
- [LGD theory background](https://github.com/zhaoxinghua09-cell/lgd-theory)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Plain-text pass/fail report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Nine check results, an overall verdict, and fix hints for failed checks; the script does not itself publish or prevent publication.]

## Skill Version(s):

1.0.5 (source: ClawHub release; bundled SKILL.md states 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
