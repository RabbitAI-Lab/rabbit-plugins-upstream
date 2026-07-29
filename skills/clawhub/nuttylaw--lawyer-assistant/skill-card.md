## Description: <br>
Full-scene legal assistant for civil and criminal practice in China, covering legal research, case retrieval, evidence analysis with OCR, legal reasoning, document drafting, non-litigation work, enforcement, and labor-dispute workflows with mandatory source verification for legal and case citations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nuttylaw](https://clawhub.ai/user/nuttylaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External legal professionals and agents use this skill to structure PRC civil and criminal legal work, including verified legal research, case lookup, evidence review, legal strategy analysis, document drafting, enforcement support, contract review, due diligence, and labor-dispute analysis. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles sensitive legal, identity, contact, and financial data in evidence and generated documents. <br>
Mitigation: Redact unnecessary identifiers, contact details, bank details, and confidential case materials before use; manage OCR outputs and drafts as sensitive legal records. <br>
Risk: Legal research, citation, or strategy outputs may be incorrect, incomplete, outdated, or jurisdictionally mismatched. <br>
Mitigation: Confirm the PRC jurisdiction and matter type, verify legal citations and case references against authoritative sources, and have a qualified lawyer review legal strategy and final documents. <br>
Risk: OCR extraction may misread important dates, amounts, signatures, seals, or names. <br>
Mitigation: Compare OCR output with the original evidence materials and manually verify key facts before relying on the extracted text. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nuttylaw/skills/lawyer-assistant) <br>
- [Anti-Fabrication Protocol](references/anti_fabrication_protocol.md) <br>
- [Legal Research Methodology](references/legal_research_methodology.md) <br>
- [Evidence Analysis Framework](references/evidence_analysis_framework.md) <br>
- [Legal Reasoning Framework](references/legal_reasoning_framework.md) <br>
- [Civil Law Practice Guide](references/civil_law_practice.md) <br>
- [Criminal Law Practice Guide](references/criminal_law_practice.md) <br>
- [Non-Litigation Practice Guide](references/non_litigation_practice.md) <br>
- [Enforcement Practice Guide](references/enforcement_practice.md) <br>
- [Labor Dispute Practice Guide](references/labor_dispute_practice.md) <br>
- [Case Analysis Report Template](assets/case_analysis_template.md) <br>
- [Evidence Analysis Report Template](assets/evidence_analysis_template.md) <br>
- [Legal Memo Template](assets/legal_memo_template.md) <br>
- [OCR Evidence Script](scripts/ocr_evidence.py) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands] <br>
**Output Format:** [Markdown reports, legal-document drafts, structured legal analysis, citation/source records, and occasional shell commands for OCR processing] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Legal citations and case references require source verification; OCR results require comparison with original evidence materials.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact manifest) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
