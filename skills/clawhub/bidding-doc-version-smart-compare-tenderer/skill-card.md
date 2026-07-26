## Description: <br>
Compares two tender-document versions from the tenderer or purchaser perspective and produces a pre-release self-check report covering change risk, compliance thresholds, consistency issues, and release recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chesaram](https://clawhub.ai/user/chesaram) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Tenderers, purchasers, and procurement agencies use this skill before issuing corrections or addenda to compare old and new tender documents, identify changes that could trigger challenges, and prepare an internal release-readiness report. It is not a substitute for legal counsel, formal audit, or bidder-side strategy. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tender documents may contain sensitive procurement information and are parsed from user-provided files. <br>
Mitigation: Use the skill only where users are comfortable providing the documents for local parsing and any configured knowledge-base lookup. <br>
Risk: Generated findings can be incomplete or low confidence when PDFs are scanned, tables are complex, documents are large, or source text extraction has gaps. <br>
Mitigation: Review data-gap and low-confidence findings against the original documents before relying on the report. <br>
Risk: Compliance and release recommendations are decision support, not final legal advice. <br>
Mitigation: Have legal or compliance reviewers confirm high-risk, threshold-related, or data-gap findings before publication. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/chesaram/skills/bidding-doc-version-smart-compare-tenderer) <br>
- [Publisher Profile](https://clawhub.ai/user/chesaram) <br>
- [Output Schema](artifact/references/output_schema.md) <br>
- [Stage 3 Difference Rules](artifact/references/stage3_diff.md) <br>
- [Stage 4 Classification Guidance](artifact/references/stage4_classify.md) <br>
- [Stage 5 Review Guidance](artifact/references/stage5_review.md) <br>
- [Golden Regression Dataset](artifact/references/golden_longling_4vs5.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Structured findings JSON plus Markdown and DOCX report artifacts when the bundled report renderer is used] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The report includes global risk level, release recommendation, P0-P4 prioritized actions, timeliness checks, consistency scan results, per-change rationale, confidence, and data-gap notices.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
