## Description:

Use when the user needs to create or refine a feature SPEC SDD before implementation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to turn ambiguous feature, bugfix, refactor, API, infrastructure, frontend, or documentation requests into an approved Spec-Driven Development document before implementation begins. It guides requirements discovery in Portuguese and produces a SPEC that acts as the implementation source of truth.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled SPEC template can direct a downstream implementation agent to open a pull request automatically after completion.

Mitigation: Before using a generated SPEC for implementation, remove or override automatic PR-opening instructions and require explicit final approval before any branch, PR, or remote repository action.

Risk: The workflow is designed around Portuguese user-facing requirements gathering, which can be a poor fit for teams expecting another language.

Mitigation: Use the skill only when a pt-BR requirements workflow is acceptable, or adapt the generated SPEC and questioning flow before relying on it.

## Reference(s):

- [SPEC SDD template](references/spec-sdd-template.md)
- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/write-specs)
- [Project URL from skill metadata](https://github.com/afonsoft/skills)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown SPEC document with Portuguese user-facing questions and approval status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a .specs/SPEC-{YYYYMMDD}-{feature}.md planning document and stops before implementation.]

## Skill Version(s):

1.0.2 (source: server release metadata; packaged SKILL.md metadata reports 1.2.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
