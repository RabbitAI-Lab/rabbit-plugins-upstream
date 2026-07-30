## Description: <br>
Bid Dup Check helps agents screen Chinese bid or tender documents for duplicate text, key-field collisions, document metadata anomalies, table similarity, and two-document diffs, then produce structured reports with risk levels and locations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chesaram](https://clawhub.ai/user/chesaram) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External procurement users, bidders, and reviewers use this skill for preliminary self-checks or screening of Chinese bid and tender packages. It is designed for initial risk triage and does not replace formal evaluation committee decisions, professional duplicate-checking systems, or legal judgment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Uploaded bid documents can contain confidential business data, personal information, document metadata, and extracted images. <br>
Mitigation: Use the skill only in an environment authorized for those documents, and review or delete extracted.json, findings.json, extracted_images/, and generated reports after use. <br>
Risk: The skill performs preliminary risk screening and can produce false positives or miss issues, especially when OCR is unavailable or no tender baseline is provided. <br>
Mitigation: Treat results as triage, document coverage limits in the report, and require human review before any formal procurement, legal, or enforcement decision. <br>
Risk: Runtime dependency installation may introduce package-management risk in uncontrolled environments. <br>
Mitigation: Run in a controlled Python environment and preinstall or pin required packages such as python-docx and pypdf where package drift is a concern. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chesaram/skills/bid-dup-check) <br>
- [Publisher profile](https://clawhub.ai/user/chesaram) <br>
- [Detection rules reference](artifact/references/detection_rules.md) <br>
- [Artifact README](artifact/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown summaries, structured JSON findings, and generated DOCX or Markdown reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local intermediate JSON, extracted image folders, and generated report files in the workspace.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and target metadata; artifact frontmatter and manifest report 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
