## Description: <br>
Helps agents draft, format, and review Chinese public-sector reports and formal documents using GB/T 9704-2012 formatting guidance, report templates, official wording conventions, and confidentiality checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mogician11111](https://clawhub.ai/user/mogician11111) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Employees and external users working in or with Chinese state-owned enterprises, government agencies, public institutions, or similar organizations use this skill to prepare formal reports, summaries, briefings, meeting minutes, notices, and implementation plans. It is intended for drafting and formatting assistance, with user review required before organizational submission. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may include classified, confidential, or sensitive internal material when requesting a draft. <br>
Mitigation: Use placeholders or sanitized excerpts, avoid classified or confidential inputs, and review any generated document under the organization's information-handling rules. <br>
Risk: The activation wording is broad enough that the skill could be invoked for ordinary writing tasks where this specialized workflow is not intended. <br>
Mitigation: Invoke it deliberately for Chinese public-sector, state-owned enterprise, or institutional formal-document drafting, and use a general writing workflow for unrelated tasks. <br>
Risk: Generated facts, names, dates, figures, and policy references may be incomplete or inaccurate. <br>
Mitigation: Treat outputs as drafts and verify all factual, policy, and formatting details before submission or distribution. <br>


## Reference(s): <br>
- [GB/T 9704-2012 formatting guide](references/gb-t9704-format.md) <br>
- [Report templates](references/report-templates.md) <br>
- [Vocabulary and wording guide](references/vocabulary-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, files, guidance] <br>
**Output Format:** [Markdown guidance or formal Chinese document drafts, with Word document output when paired with a document-generation skill] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses XX placeholders for missing or sensitive fields and asks users to review facts, dates, names, policy references, formatting, and required fonts before use.] <br>

## Skill Version(s): <br>
1.1.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
