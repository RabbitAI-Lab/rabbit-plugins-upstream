## Description:

Checks hospital and clinic medical consumable markup worksheets by recalculating stock balances, stock amounts, markup rates, totals, duplicate rows, blank fields, and negative values, with each finding tied to source line numbers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External hospital and clinic pricing staff, consumable accountants, and finance teams use this skill before monthly closing or pricing self-checks to recalculate local consumable worksheets and identify line-level arithmetic or table-quality discrepancies. It is not a medical, procurement-price, physical-inventory, or local pricing-policy determination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Outputs may be mistaken for pricing-policy, procurement-price, physical-inventory, or medical determinations.

Mitigation: Use the results only as arithmetic and table checks, then verify policy, procurement data, inventory, and clinical questions against authoritative local records and reviewers.

Risk: The free release intentionally omits zero-rate markup judgment, below-cost judgment, three-part amount reconciliation, and impact-ranked adjustment lists.

Mitigation: Review the checks_not_run output and use a separate review process or the complete product before relying on conclusions in those areas.

Risk: Missing or incorrectly exported worksheet columns can prevent valid conclusions.

Mitigation: Provide worksheet text with the required headers and treat insufficient-input output as no conclusion, not as a finding that no issue exists.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/medical-consumable-markup-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Artifact skill documentation](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Plain text or JSON from a local Node.js command, usually summarized in Markdown by the agent.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include source line numbers, severity levels, checks performed, checks not run, and an explicit insufficient-input status when required worksheet columns are missing.]

## Skill Version(s):

1.0.43 (source: server release evidence; artifact frontmatter reports 1.0.42)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
