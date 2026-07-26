## Description: <br>
Provides local GDPR compliance checks, DPIA support, data subject rights review, cross-border transfer review, and draft compliance report generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cqdev-ai](https://clawhub.ai/user/cqdev-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Privacy, compliance, and engineering teams use this skill to run local GDPR-oriented checks and generate draft reports or templates for DPIAs, data subject rights, and cross-border transfer review. Outputs should be treated as internal compliance aids that require legal or DPO review before operational reliance. <br>

### Deployment Geography for Use: <br>
EU/EEA and UK <br>

## Known Risks and Mitigations: <br>
Risk: Generated GDPR reports or templates may be mistaken for legal advice or regulatory-ready evidence. <br>
Mitigation: Use outputs as internal drafts only and review important compliance decisions with qualified counsel or a data protection officer. <br>
Risk: Generated reports may contain business-sensitive or privacy-sensitive information. <br>
Mitigation: Run the skill locally in an approved working directory and protect report files under the organization's data-handling policy. <br>
Risk: User-selected output paths may overwrite local report files. <br>
Mitigation: Use dedicated output directories and review --output paths before running report generation commands. <br>
Risk: Dependency drift can affect reproducibility across installations. <br>
Mitigation: Pin dependency versions in controlled environments when repeatable execution is required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cqdev-ai/skills/gdpr-compliance) <br>
- [GDPR regulation reference](references/gdpr-regulation.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, guidance] <br>
**Output Format:** [Human-readable guidance plus JSON, Markdown, HTML, or CSV report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs locally and writes user-selected report outputs; generated content is not legal advice.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata, package.json, and CHANGELOG, released 2026-07-19) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
