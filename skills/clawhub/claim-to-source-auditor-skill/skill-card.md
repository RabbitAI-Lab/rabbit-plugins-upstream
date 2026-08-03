## Description: <br>
Audit, fact-check, verify, or cross-check an article, report, draft, or series by extracting verifiable claims, tracing them to primary or reliable secondary sources, classifying support status, and producing a structured audit report with P0-P2 severity. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Editors, analysts, researchers, and developers use this skill to audit factual claims in long-form articles, reports, drafts, and cross-platform versions before publication or revision. It helps separate verified facts, unsupported claims, wrong claims, judgment, and source conflicts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Audit reports and CSV records may contain claims, source notes, or excerpts from sensitive internal materials. <br>
Mitigation: Point the skill only at intended article and evidence locations, and handle generated reports and CSV files according to the data sensitivity of the underlying materials. <br>
Risk: Incorrect source classification or claim verdicts could lead to misleading publication decisions. <br>
Mitigation: Review P0 and P1 findings against the cited primary or reliable secondary sources before revising, publishing, or relying on the audit decision. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/haiyangchenbj/skills/claim-to-source-auditor-skill) <br>
- [Artifact README](artifact/README.md) <br>
- [Artifact Skill Definition](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, csv, guidance] <br>
**Output Format:** [Structured Markdown report plus CSV audit records] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include an optional regression gold-set CSV for future re-runs.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
