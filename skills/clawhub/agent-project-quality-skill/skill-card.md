## Description:

Creates, audits, and refactors authoritative technical specifications, issue and improvement logs, risk-based verification workflows, and automated documentation checks for engineering repositories.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wuworks](https://clawhub.ai/user/wuworks)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineering agents use this skill to create or audit project quality governance: source-of-truth specifications, defect and improvement logs, verification levels, and diagnostic documentation checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to restructure authoritative project governance documents, which could introduce inaccurate rules or change history if accepted without review.

Mitigation: Review proposed documentation diffs, unresolved items, and evidence before accepting changes.

Risk: The validator must be adapted to the repository schema and could produce misleading diagnostics if configured incorrectly.

Mitigation: Configure explicit spec and log paths plus schema options, then run proportionate verification before integrating it.

Risk: Private research, secrets, or repository-specific material could leak into reusable artifacts if authorization boundaries are ignored.

Mitigation: Authorize private access only when needed and keep private paths, secrets, build outputs, and raw investigation notes out of release-ready material.

## Reference(s):

- [GitHub source repository](https://github.com/WuWorks/Agent-Project-quality-Skill)
- [ClawHub skill page](https://clawhub.ai/wuworks/skills/agent-project-quality-skill)
- [Technical Specification Architecture](references/technical-spec-architecture.md)
- [Issue and Improvement Log](references/issue-and-improvement-log.md)
- [Verification Workflow](references/verification-workflow.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with optional JavaScript validator code, YAML configuration, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Diagnostic validator reads explicit files and reports issues without rewriting documents.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
