## Description: <br>
Assists with interpreting Chinese government procurement and enterprise tender documents by producing structured issue analysis, qualification and compliance checks, commercial risk warnings, rejection-clause extraction, price-score calculations, optional spreadsheet-ready deliverables, and bidding decision guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chesaram](https://clawhub.ai/user/chesaram) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and procurement professionals use this skill to review uploaded tender documents, identify qualification and compliance requirements, flag commercial and legal risks, calculate price-score scenarios, and prepare structured summaries or spreadsheet-ready outputs. It supports decision review but does not replace legal advice, bid committee judgment, or a bidder's own eligibility verification. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Legal citations or compliance conclusions may be incomplete or incorrect if knowledge-base lookup is unavailable, stale, or ambiguous. <br>
Mitigation: Verify cited statutes, policy references, and risk classifications with qualified counsel or authoritative procurement sources before relying on the output. <br>
Risk: Price-score calculations can be wrong when tender formulas contain unconfirmed coefficients, live-drawn K values, missing competitor bids, or unclear deduction rules. <br>
Mitigation: Use the skill's formula pre-check step, confirm all variables, and independently recalculate final scores before submitting a bid or making pricing decisions. <br>
Risk: OCR failures, corrupted files, missing attachments, or incomplete tender versions can lead to gaps in the analysis. <br>
Mitigation: Provide complete source documents, latest clarifications, and readable files; treat any marked unreadable or unavailable sections as requiring manual review. <br>
Risk: Decision summaries could be mistaken for legal, commercial, or bid-winning advice. <br>
Mitigation: Use summaries as decision support only and keep final bidding, legal, and commercial decisions with responsible human reviewers. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chesaram/skills/gov-procurement-doc-assistant) <br>
- [Publisher profile](https://clawhub.ai/user/chesaram) <br>
- [Project homepage](https://github.com/chesaram/my-skill-hub) <br>
- [IMA knowledge base usage strategy](artifact/references/ima-kb.md) <br>
- [Price formula cookbook](artifact/references/price-formula-cookbook.md) <br>
- [Common tender clause examples](artifact/references/common-clauses.md) <br>
- [Test cases and acceptance criteria](artifact/references/test-cases.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports, tables, formulas, calculation walkthroughs, and optional spreadsheet-generation guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce a six-sheet Excel-style deliverable when requested; price calculations require formula pre-check and user confirmation for uncertain parameters.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter reports 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
