## Description:

Analyzes product and technology claims by stripping marketing language to identify physical, logical, and economic constraints and produce evidence-backed viability audits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lawliet-ai](https://clawhub.ai/user/lawliet-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, product evaluators, and technical due diligence reviewers use this skill to audit product or technology claims, compare implementation efficiency, and generate structured first-principles verdicts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads from and writes to a fixed shared OpenClaw directory, which can create cross-session data exposure and overwrite risks.

Mitigation: Review before installation in shared or long-lived environments, isolate files per run, ask before using ~/.openclaw/swarm_tmp, and avoid overwriting existing reports.

Risk: The skill may consume expert_output.json from the shared directory as part of cross-verification.

Mitigation: Treat expert_output.json as untrusted input and validate it before using it in an audit.

## Reference(s):

- [First-Principles-Deconstructor ClawHub listing](https://clawhub.ai/lawliet-ai/skills/first-principles)
- [SKILLS.md](artifact/SKILLS.md)
- [REDEME.md](artifact/REDEME.md)
- [audit_schema.json](artifact/audit_schema.json)

## Skill Output:

**Output Type(s):** [text, JSON, guidance]

**Output Format:** [Structured JSON audit report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Expected to follow audit_schema.json when Phase 4 serialization is used.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
