## Description:

A local checker for construction and project settlement materials that runs 14 built-in checks per project and reports per-project conclusions with source file and line references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Project accountants, cost-control staff, owner representatives, and project management teams use this skill to check settlement worksheets at recurring reporting, subcontract settlement, billing, collection, capitalization, and closeout milestones. It supports arithmetic and consistency review, not audit, legal, tax, payment approval, or engineering-cost certification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes sensitive project settlement materials locally.

Mitigation: Install and run it only in environments approved for those materials, and rely on the ClawHub security evidence showing no network use, persistence, or destructive behavior for this release.

Risk: Users may overread arithmetic and consistency findings as audit, legal, tax, payment approval, or engineering-cost certification.

Mitigation: Treat the output as a review aid and route payment, audit, tax, and engineering-cost decisions through the appropriate qualified reviewers.

Risk: The free package explicitly omits some checks and may mark input areas as not run.

Mitigation: Review checks_not_run and sub_checks_not_run before acting on results, and do not treat omitted or insufficient-input areas as passed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chenqg618/skills/project-settlement-pack-free)
- [artifact/SKILL.md](artifact/SKILL.md)
- [artifact/templates/sample.json](artifact/templates/sample.json)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Terminal text or JSON containing per-project conclusions, check status, findings, and source file/line references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally over user-provided project files; reports checks_not_run and sub_checks_not_run when checks are outside the free package or input coverage is incomplete.]

## Skill Version(s):

1.0.22 (source: evidence.release.version and artifact/SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
