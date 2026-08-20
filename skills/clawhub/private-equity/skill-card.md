## Description:

Private Equity is a Chinese-language PE/VC workflow skill suite for term sheet review, due diligence checklists, investment committee memos, return modeling, deal screening, and exit analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ebandao777-oss](https://clawhub.ai/user/ebandao777-oss)

### License/Terms of Use:

MIT-0

## Use Case:

Investment teams use this skill to route PE/VC requests to structured templates for deal screening, due diligence, legal and commercial review, investment memo drafting, return analysis, and exit planning. It is intended to support analyst workflows and review-ready Markdown deliverables, not to replace professional investment, legal, tax, or compliance judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Confidential deal materials could be written to Notion when the optional connector is enabled.

Mitigation: Require explicit user confirmation before any Notion write, verify the destination workspace and permissions, and prefer local Markdown output for confidential transactions.

Risk: Investment, legal, tax, or valuation outputs may be incomplete or misleading if treated as final advice.

Mitigation: Use the skill output as analyst work product for review and require appropriate investment, legal, tax, and compliance review before acting on it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ebandao777-oss/skills/private-equity)
- [Server-resolved GitHub provenance](https://github.com/ebandao777-oss/private-equity)
- [README](README.md)
- [Deal screening template](references/deal-screening.md)
- [Due diligence checklist template](references/due-diligence-checklist.md)
- [Exit analysis template](references/exit-analysis.md)
- [Investment memo template](references/investment-memo.md)
- [Return modeling template](references/return-modeling.md)
- [Term sheet review template](references/term-sheet-review.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance, Configuration]

**Output Format:** [Markdown reports, checklists, memos, matrices, and structured review tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local Markdown deliverables and, when explicitly allowed, Notion-ready content.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact frontmatter reports 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
