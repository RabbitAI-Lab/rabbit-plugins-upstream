## Description:

AI Company Governance provides a modular governance framework for coordinating C-suite AI agents across strategy, finance, legal, security, risk, operations, quality, and engineering workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[johnsmithfan](https://clawhub.ai/user/johnsmithfan)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, operators, and developers use this skill to structure AI-company governance work: selecting the right C-suite agent module, coordinating cross-agent decisions, applying audit and conflict-resolution routines, and producing governance-oriented plans or reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad tool authority and operational workflows could let the skill influence files, commands, web activity, or agent coordination beyond the user's intent.

Mitigation: Install and run it in a sandboxed workspace, limit tool grants to the specific task, and require explicit user approval before writes, command execution, external calls, or agent registration changes.

Risk: Governance modules describe financial, legal, security, and operational decision paths that could affect sensitive company data or high-impact actions.

Mitigation: Do not connect the skill directly to real financial accounts, production authority, or fund movement; route high-impact recommendations through human review and documented approval.

Risk: The skill defines long-lived audit, legal, financial, HR, and shared-state records that may contain sensitive business or personal data.

Mitigation: Define retention periods, access controls, and data minimization rules before storing records, and keep sensitive data out of prompts unless the workspace is approved for that use.

## Reference(s):

- [ClawHub AI Company Governance Release Page](https://clawhub.ai/johnsmithfan/skills/ai-company-governance)
- [Core Architecture](references/architecture.md)
- [CEO Governance Module](references/ceo.md)
- [CFO Finance Module](references/cfo.md)
- [CMO Brand Module](references/cmo.md)
- [CHO People and Agent Registry Module](references/cho.md)
- [CPO Partnerships Module](references/cpo.md)
- [CLO Legal and Compliance Module](references/clo.md)
- [CTO Technical Governance Module](references/cto.md)
- [CQO Quality Module](references/cqo.md)
- [CISO Security Module](references/ciso.md)
- [CRO Risk Module](references/cro.md)
- [COO Operations Module](references/coo.md)
- [Governance Tools](references/governance-tools.md)
- [Engineering Process](references/engineering.md)
- [External Interface Specification](references/api-spec.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with tables, role playbooks, command examples, YAML or JSON-style schemas, and action plans]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Pure markdown with no external dependencies; documented compatibility with OpenClaw >= 0.1.0 on Linux, macOS, and Windows]

## Skill Version(s):

3.1.0 (source: server release metadata and skill version history, released 2026-04-14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
