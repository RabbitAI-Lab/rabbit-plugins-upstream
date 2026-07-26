## Description: <br>
Compares two text-layer Chinese tender documents from a bidder's perspective and produces a structured change-impact report covering pricing, technical, eligibility, deadline, and compliance risks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chesaram](https://clawhub.ai/user/chesaram) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External bidders and bid teams use this skill to compare an original tender document with a revised, clarification, or addendum version and understand how changes affect bid preparation. It helps identify red-line risks, hidden eligibility barriers, pricing impact, deadline rights, and recommended next actions for human review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Uploaded tender document text is parsed locally and may be summarized with knowledge-base-assisted lookups. <br>
Mitigation: Install only for tender-document comparison workflows where the user is comfortable with this analysis path and has appropriate permission to process the document text. <br>
Risk: The report is an initial screening aid and may miss issues or provide incomplete legal context. <br>
Mitigation: Treat findings as triage output; have qualified reviewers check red-line, high-value, eligibility, pricing, and deadline conclusions before acting. <br>
Risk: The package contains a stale tenderer-report option and a lenient text-file fallback outside the documented DOCX/PDF-only bidder workflow. <br>
Mitigation: Use the documented bidder workflow with exactly two supported Chinese DOCX or text-layer PDF files, and confirm inputs before executing scripts. <br>


## Reference(s): <br>
- [Stage 3 Difference Detection Rules](artifact/references/stage3_diff.md) <br>
- [Output Schema](artifact/references/output_schema.md) <br>
- [Bidder Impact Classifier](artifact/references/bidder/stage4_classify.md) <br>
- [Bidder Review, Timeliness, and Pricing Evaluation](artifact/references/bidder/stage5_review.md) <br>
- [Golden Regression Dataset](artifact/references/golden_longling_4vs5.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown report with optional DOCX file and structured JSON intermediate files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Analyzes exactly two Chinese DOCX or text-layer PDF tender documents; scanned PDFs, image-only files, and English documents are outside the documented scope.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence release, SKILL.md frontmatter, manifest.yaml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
