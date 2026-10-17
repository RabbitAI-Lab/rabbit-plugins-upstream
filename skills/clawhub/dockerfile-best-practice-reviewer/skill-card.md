## Description:

Reviews Dockerfiles for layer hygiene, least-privilege users, image pinning, and clearer build structure.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hmahmadcs](https://clawhub.ai/user/hmahmadcs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to review a pasted Dockerfile and receive prioritized improvements, patch suggestions, and verification steps without running a build by default.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pasted Dockerfiles may expose embedded secrets.

Mitigation: Remove real secrets before sharing a Dockerfile; do not provide registry passwords.

Risk: Suggested changes may not fit a project's build or deployment constraints.

Mitigation: Review proposed changes against local requirements and validate them with the provided verification steps before adoption.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/hmahmadcs/skills/dockerfile-best-practice-reviewer)

## Skill Output:

**Output Type(s):** [Analysis, Code, Shell commands, Guidance]

**Output Format:** [Markdown with Dockerfile snippets and verification commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prioritized findings with severity, explanations, minimal patch suggestions, and a final checklist; no build execution by default.]

## Skill Version(s):

1.0.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
