## Description: <br>
Reviews Chinese-language contracts for clause risks, key information, legal and compliance concerns, and suggested report-ready revisions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fyniujin](https://clawhub.ai/user/fyniujin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Legal, business, procurement, HR, and operations users reviewing Chinese-language contracts use this skill to extract contract facts, identify common clause and compliance risks, and produce review reports or revised draft files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Confidential or privileged contract text may be sent to configured remote LLM APIs. <br>
Mitigation: Use --no-llm or a controlled local model for confidential, privileged, regulated, or client contracts. <br>
Risk: Review metadata and history can be persisted under the user's home directory. <br>
Mitigation: Review and manage ~/.contract-review retention, or run the skill in an isolated environment when handling sensitive contracts. <br>
Risk: Update checks, hardware profiling, and the curl-piped Ollama installer introduce operational and network exposure. <br>
Mitigation: Avoid the curl-piped installer, use controlled installation sources, and disable or restrict update checks in sensitive environments. <br>
Risk: AI-generated contract analysis may be incomplete or may not substitute for jurisdiction-specific legal advice. <br>
Mitigation: Have qualified legal counsel review high-value, regulated, or mission-critical contracts before relying on the output. <br>


## Reference(s): <br>
- [Legal Basis](references/legal_basis.md) <br>
- [Risk Rules](references/risk_rules.yaml) <br>
- [Contract Types](references/contract_types.yaml) <br>
- [Clause Library Index](references/clause_library/clause_index.yaml) <br>
- [Compliance Checklist](references/compliance_checklist.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, JSON, Files, Guidance] <br>
**Output Format:** [Markdown, JSON, or DOCX contract review reports and revision drafts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include risk levels, clause references, legal basis notes, suggested replacement language, scores, and locally written report or history files.] <br>

## Skill Version(s): <br>
4.0.0 (source: SKILL.md frontmatter and server release metadata; pyproject.toml reports 3.2.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
