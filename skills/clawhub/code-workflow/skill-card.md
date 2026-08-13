## Description:

A four-stage code-change workflow for research, planning, user review, and TDD implementation, with optional pull request capture guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering agents use this skill to structure non-trivial code changes through research artifacts, implementation plans, explicit review gates, TDD execution, verification, and optional PR evidence capture.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional plan-file hook claims to be warning-only while returning a blocking exit code when undecided markers are detected.

Mitigation: Review the hook before installation and use it only when a blocking undecided-marker gate is acceptable for the workspace.

Risk: The skill is an opinionated hard-stop workflow that can interrupt normal coding, planning, commit, and PR actions.

Mitigation: Adopt it deliberately for tasks that benefit from enforced review and TDD gates, and use explicit invocations to avoid accidental activation.

## Reference(s):

- [Code Workflow on ClawHub](https://clawhub.ai/drumrobot/skills/code-workflow)
- [Skill Definition](artifact/SKILL.md)
- [Implementation Workflow](artifact/implement.md)
- [Research, Plan, Review, and Branch Steps](artifact/steps.md)
- [Pull Request Workflow](artifact/pr.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with checklists, file-writing conventions, code snippets, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create workspace-local research, plan, task, and pull request evidence artifacts when followed by an agent.]

## Skill Version(s):

0.6.1 (source: server release metadata and CHANGELOG, released 2026-08-05)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
