## Description:

AI Delivery Spec helps agents create, review, reverse-engineer, change, and accept requirements, PRDs, prototypes, and existing-system evidence while keeping outputs traceable from framing through acceptance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[franklinxkk](https://clawhub.ai/user/franklinxkk)

### License/Terms of Use:

Apache 2.0

## Use Case:

Product, design, engineering, QA, compliance, and agent teams use this skill to turn ideas, source materials, existing systems, changes, and acceptance needs into the smallest complete requirement artifact for the current stage. It is suited for requirement framing, PRD and prototype specification, review baselines, change impact analysis, traceability, and acceptance records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read project requirement materials and create local artifacts for scaffolding, gates, baselines, traceability, or acceptance records.

Mitigation: Use it in trusted project workspaces and review generated files before sharing them outside the team.

Risk: Static gate results can be mistaken for proof of domain correctness, legal suitability, browser behavior, implemented behavior, or customer acceptance.

Mitigation: Treat PASS as a contract check only and require separate domain, browser, implementation, and customer evidence where those claims matter.

Risk: Running local Python gates from an untrusted or modified package could execute code outside the expected release behavior.

Mitigation: Run Python gates only from the trusted installed package and keep scanner or package provenance evidence with the release review.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/franklinxkk/skills/ai-delivery-spec)
- [README](README.md)
- [Lifecycle Stages](references/stages.md)
- [Requirement Specification](references/specify.md)
- [Prototype Guidance](references/prototype.md)
- [Review Workspace](references/review-workspace.md)
- [Change and Acceptance](references/change-acceptance.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, YAML, JSON, diagrams, prototype files, and command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local artifacts and static gate records when requested; static PASS does not prove legal, domain, browser, implementation, or customer acceptance correctness.]

## Skill Version(s):

5.4.7 (source: ClawHub release metadata, created 2026-08-26; CHANGELOG entry dated 2026-08-22)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
