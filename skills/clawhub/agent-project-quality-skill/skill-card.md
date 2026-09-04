## Description:

Create, audit, or refactor authoritative technical specifications, issue and improvement logs, risk-based verification workflows, and automated documentation checks for engineering repositories.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wuworks](https://clawhub.ai/user/wuworks)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to establish or maintain quality governance documents, structured defect and improvement history, proportional verification workflows, and diagnostic documentation checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Governance changes proposed by an agent can introduce incorrect rules, misleading history, or unsupported verification claims.

Mitigation: Review generated specifications, logs, and verification evidence before adopting them as authoritative project records.

Risk: Validation requires reading repository documents and can expose private paths or sensitive notes if the scope is too broad.

Mitigation: Specify the target documents and private paths that are off-limits before use, and run the validator only against explicit file inputs.

## Reference(s):

- [Technical Specification Architecture](references/technical-spec-architecture.md)
- [Issue and Improvement Log](references/issue-and-improvement-log.md)
- [Verification Workflow](references/verification-workflow.md)
- [Project Quality Governance on ClawHub](https://clawhub.ai/wuworks/skills/agent-project-quality-skill)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with optional code, shell command, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include read-only validation diagnostics when the validation script is used.]

## Skill Version(s):

0.1.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
