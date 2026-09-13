## Description:

Test skills before using or publishing. Trial, compare, evaluate in isolation without affecting your environment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivangdavila](https://clawhub.ai/user/ivangdavila)

### License/Terms of Use:


## Use Case:

Developers and skill publishers use this skill to test, compare, and evaluate agent skills in isolation before installing them or releasing them publicly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow includes unpinned npx install and info commands while describing the test environment as isolated.

Mitigation: Use a pinned or preinstalled trusted ClawHub CLI, and run install tests only in a disposable sandbox or container.

Risk: Testing skills that require credentials can expose real accounts or sensitive access if normal credentials are reused.

Mitigation: Use throwaway test credentials or skip authentication-dependent features during skill evaluation.

Risk: Skill slugs used in install paths can point to the wrong package if they are not verified first.

Mitigation: Validate skill slugs before using them in commands or filesystem paths.

## Reference(s):

- [Skill Test on ClawHub](https://clawhub.ai/ivangdavila/skills/skill-test)
- [Sandbox Testing](artifact/sandbox.md)
- [Comparing Skills](artifact/compare.md)
- [Multi-Agent Evaluation](artifact/evaluate.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands]

**Output Format:** [Markdown with inline shell command examples and evaluation checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces recommendations, comparison summaries, and review findings for human decision-making.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
