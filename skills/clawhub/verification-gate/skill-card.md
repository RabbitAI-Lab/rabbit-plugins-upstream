## Description:

Guides agents through an eight-stage verification gate after code changes, with e2e functional checks and real-runtime validation as hard readiness criteria before claiming work is complete or opening a PR.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cat-xierluo](https://clawhub.ai/user/cat-xierluo)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering agents use this skill after feature work, bug fixes, refactors, or PR preparation to run build, type, lint, unit, e2e, real-runtime, security, and diff checks before declaring code ready.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Staging-service verification examples can affect shared systems if run with broad credentials or write operations.

Mitigation: Use dedicated staging data, least-privilege test credentials, non-destructive requests where possible, cleanup steps, and explicit approval for any write operation against shared systems.

Risk: Verification results can be misleading if an agent accepts self-reported PASS status instead of checking actual command output.

Mitigation: Run the project commands directly, inspect their outputs, and record READY only when the required e2e and real-runtime gates pass or have a documented NOT_RUN reason.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cat-xierluo/skills/verification-gate)
- [Project homepage](https://github.com/cat-xierluo/legal-skills)
- [assertion-depth.md](references/assertion-depth.md)
- [e2e-practice.md](references/e2e-practice.md)
- [eight-phases-rationale.md](references/eight-phases-rationale.md)
- [lessons-from-practice.md](references/lessons-from-practice.md)
- [test-pyramid.md](references/test-pyramid.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with command examples and a verification-report table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only workflow guidance; users run and review project-specific commands before deciding readiness.]

## Skill Version(s):

1.0.2 (source: frontmatter, changelog, and server release metadata; released 2026-08-05)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
