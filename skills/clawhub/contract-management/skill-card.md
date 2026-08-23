## Description:

A Chinese-language contract management skill suite for NDA screening, contract tracking, contract comparison, contract review, legal lookup, and contract drafting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ebandao777-oss](https://clawhub.ai/user/ebandao777-oss)

### License/Terms of Use:

MIT-0

## Use Case:

Legal, operations, and business teams use this skill to route contract-related requests into templates for NDA triage, contract review, comparison, deadline tracking, legal lookup, and contract drafting. It is framed for workflows involving Chinese contract law and should be reviewed by qualified counsel before legal decisions are made.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill can handle confidential contracts and may save or publish contract reports or drafts through connected services such as Notion.

Mitigation: Use only documents the user is authorized to process, keep Notion disconnected or require explicit local-only handling unless publication is approved, and review outputs before sharing.

Risk: The skill produces contract analysis, legal lookup summaries, and contract language that could be mistaken for final legal advice.

Mitigation: Require qualified legal review before relying on analysis, generated clauses, or legal citations for business decisions.

Risk: The skill is framed around Chinese contract law, so applying its outputs to other governing laws may be misleading.

Mitigation: Confirm governing law and jurisdiction before use, and route non-China matters to appropriate legal expertise.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ebandao777-oss/skills/contract-management)
- [Server-resolved GitHub provenance](https://github.com/ebandao777-oss/contract-management)
- [README](README.md)
- [NDA screening template](references/nda-screening.md)
- [Contract tracker template](references/contract-tracker.md)
- [Contract comparison template](references/contract-comparison.md)
- [Contract review template](references/contract-review.md)
- [Legal lookup template](references/legal-lookup.md)
- [Contract drafting template](references/contract-drafting.md)
- [Word formatting specification](references/word-format-spec.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown reports, checklists, contract drafts, comparison tables, legal lookup summaries, and optional document formatting guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or publish contract-related reports and drafts when the environment provides file or Notion capabilities.]

## Skill Version(s):

0.1.0 (source: server release metadata; artifact frontmatter says 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
