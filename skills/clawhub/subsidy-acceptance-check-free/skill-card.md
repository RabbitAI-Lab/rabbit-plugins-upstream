## Description:

A deterministic local checker for Chinese government subsidy ledgers and acceptance-document checklists that recomputes line-level amounts, flags missing acceptance materials, identifies duplicate declarations, and cites source lines without deciding eligibility or policy applicability.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, tax, and project-application staff use this skill during subsidy acceptance, subsidy closeout, and annual fiscal self-checks to cross-check ledger arithmetic and acceptance-document completeness. It is a bookkeeping aid and does not replace legal, audit, policy eligibility, or official acceptance review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may over-rely on the checker as legal, audit, policy eligibility, or official acceptance approval advice.

Mitigation: Use the output only as a bookkeeping cross-check and route eligibility, compliance, audit, and acceptance decisions to qualified reviewers or responsible authorities.

Risk: The documentation has inconsistent text about anonymous usage statistics, even though the inspected code has no artifact-backed network call.

Mitigation: Review the release artifact and security evidence before deployment where telemetry expectations are material.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/subsidy-acceptance-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Sample input template](artifact/templates/sample.json)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands and optional JSON checker output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include severity, category, source line, message, advice, summary counts, executed checks, skipped checks, and out-of-scope checks.]

## Skill Version(s):

1.0.1 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
