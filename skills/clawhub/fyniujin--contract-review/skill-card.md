## Description: <br>
Reviews Chinese-language contracts for clause risks, key terms, compliance issues, and suggested revisions across common agreement types. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fyniujin](https://clawhub.ai/user/fyniujin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and legal or business reviewers use this skill to review Chinese-language contracts, identify risk patterns, extract key terms, and generate structured reports with suggested edits. It is intended as review support and does not replace qualified legal advice. <br>

### Deployment Geography for Use: <br>
Mainland China <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive contract text may be transmitted to an external LLM service when remote LLM review is enabled. <br>
Mitigation: Use --no-llm for sensitive contracts or configure a trusted local model such as Ollama before reviewing confidential documents. <br>
Risk: Review history may be stored locally in plaintext. <br>
Mitigation: Review and clear ~/.contract-review history data according to the user's retention requirements. <br>
Risk: The scanner notes that a file-processing safety claim may fail at runtime because extract_text.py references an undefined Blocked_SYSTEM_EXT name. <br>
Mitigation: Fix and test the file blocking path before relying on dangerous file interception, and manually screen inputs until that issue is resolved. <br>
Risk: AI-generated contract findings can be incomplete or mistaken. <br>
Mitigation: Use the report as review support and consult a qualified lawyer for high-value, complex, or legally sensitive contracts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/contract-review) <br>
- [README](README.md) <br>
- [Legal basis](references/legal_basis.md) <br>
- [Contract type definitions](references/contract_types.yaml) <br>
- [Risk rules](references/risk_rules.yaml) <br>
- [Compliance checklist](references/compliance_checklist.md) <br>
- [Report template](assets/report_template.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, JSON, Files, Guidance] <br>
**Output Format:** [Markdown, JSON, or DOCX contract review reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports include risk severity, clause references, legal basis, suggested revisions, scoring, and disclaimers.] <br>

## Skill Version(s): <br>
3.2.0 (source: frontmatter, pyproject.toml, server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
