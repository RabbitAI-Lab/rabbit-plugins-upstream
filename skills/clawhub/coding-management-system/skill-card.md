## Description:

Keeps AI-assisted software projects aligned by turning unclear goals and drifting project records into compact authorization, bounded execution, and evidence-based QA decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[englandtong](https://clawhub.ai/user/englandtong)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, project owners, and agent operators use this skill to clarify uncertain goals, bootstrap legacy project records, size work, authorize bounded agent execution, check alignment, and preserve independent final QA for AI-assisted software delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may create or update project-local governance records.

Mitigation: Review dry runs and require explicit owner approval before archive, reset, rebaseline, deletion, production, credential, deployment, paid-resource, or destructive actions.

Risk: Governance records can accidentally include sensitive or private project information.

Mitigation: Do not store API keys, tokens, credentials, private documents, contact data, financial records, contracts, or confidential materials in Active Packets, work orders, QA decisions, or cloud uploads without explicit confirmation.

Risk: Governance output can grow without producing verified user-visible behavior.

Mitigation: Use the lightest governance profile, keep the active document set compact, archive superseded history, and stop expansion when evidence is insufficient or the project drifts from the target.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/englandtong/skills/coding-management-system)
- [Quickstart](QUICKSTART.md)
- [Security](SECURITY.md)
- [Execution Contract 2.1](references/en/execution-contract.md)
- [Goal Discovery 2.1](references/en/goal-discovery.md)
- [Planning And Sizing 2.1](references/en/planning-and-sizing.md)
- [Governance Profiles And Files 2.1](references/en/governance-profiles.md)
- [Controller, Stage Reviewer, And Independent QA 2.1](references/en/controller-qa.md)
- [Alignment, Rebaseline, Audit, And Finish Line 2.1](references/en/alignment-and-rebaseline.md)
- [Anti-Involution 2.2](references/en/anti-involution.md)
- [Legacy Bootstrap 2.1](references/en/legacy-bootstrap.md)
- [Cross-Plugin File Contracts (CDH)](references/en/cross-plugin-file-contracts.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with structured status fields, templates, and optional shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Bilingual English/Chinese guidance; creates or updates project-local governance records only when authorized.]

## Skill Version(s):

2.2.1 (source: server release metadata, SECURITY.md, and SKILL.md body)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
