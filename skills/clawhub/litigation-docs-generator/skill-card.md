## Description: <br>
Generates coordinated civil and commercial litigation filing documents, including pleadings, preservation materials, attorney authorization records, an interview record, an interest-loss spreadsheet, and a retainer agreement. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leahlu0124-creator](https://clawhub.ai/user/leahlu0124-creator) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Legal professionals and legal-service agents use this skill to collect case facts and produce a consistent filing package for civil and commercial litigation matters. It is intended for Chinese-language litigation drafting workflows that may use legal database checks when available. <br>

### Deployment Geography for Use: <br>
Global, with content focused on China civil and commercial litigation workflows. <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles sensitive litigation facts, signed contract contents, lawyer and client details, and law-firm payment information. <br>
Mitigation: Use only necessary case materials, confirm consent and privacy handling before sharing documents, and avoid uploading unnecessary signed or financial records. <br>
Risk: The skill may use external legal databases or company-information lookups without clear privacy and consent boundaries. <br>
Mitigation: Confirm which legal databases are connected and that each lookup is authorized before sending party, case, or company information to external tools. <br>
Risk: If no professional legal database is connected, legal citations may rely on model knowledge and can be inaccurate or outdated. <br>
Mitigation: Use connected authoritative legal databases where possible and have a qualified lawyer verify every statute, case reference, and legal conclusion. <br>
Risk: Generated pleadings, preservation materials, retainer terms, fee details, and interest calculations may contain factual, legal, or financial errors. <br>
Mitigation: Review all generated documents, formulas, party details, amounts, dates, and payment terms before filing, signing, or sharing with clients. <br>


## Reference(s): <br>
- [Skill source](artifact/SKILL.md) <br>
- [Complaint template](artifact/references/complaint_template.md) <br>
- [Preservation application template](artifact/references/preservation_application_template.md) <br>
- [Guarantee letter template](artifact/references/guarantee_letter_template.md) <br>
- [Power of attorney template](artifact/references/power_of_attorney_template.md) <br>
- [Legal representative certificate template](artifact/references/legal_rep_certificate_template.md) <br>
- [Interview record template](artifact/references/interview_record_template.md) <br>
- [Retainer agreement template](artifact/references/retainer_agreement_template.md) <br>
- [Yuandian tools guide](artifact/references/yuandian_tools_guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files, Shell commands, Guidance] <br>
**Output Format:** [Chinese legal document drafts, generated .docx documents, and an .xlsx interest-loss workbook.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires case facts, party details, court, claim, preservation, lawyer, fee, and interest inputs; legal citations and final documents should be reviewed before filing or signing.] <br>

## Skill Version(s): <br>
2.2.1 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
