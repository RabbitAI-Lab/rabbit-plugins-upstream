## Description: <br>
Ai Assistant Free helps agents assess long commercial documents, extract core logic, and identify basic risks such as ambiguities, internal conflicts, and undefined terms. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and document reviewers use this skill to prepare contract reviews or summarize long memos by producing a structured document assessment, core logic summary, and basic risk list. It provides analysis support and does not replace licensed legal advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may be used with confidential contracts, proposals, or internal memos. <br>
Mitigation: Review the skill before installing it for sensitive workflows and avoid sending confidential content to untrusted endpoints. <br>
Risk: The optional callback_url can disclose analysis data to an external endpoint without enough privacy or scope detail. <br>
Mitigation: Do not use callback_url unless the endpoint is trusted and the data being sent is understood and approved. <br>
Risk: The skill requests exec capability for document preprocessing. <br>
Mitigation: Remove or restrict exec unless command-line preprocessing is required for the workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/ai-assistant-free) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, shell commands] <br>
**Output Format:** [Markdown with structured document assessment, core logic, and risk sections] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include cited document clauses, basic risk items, and review-preparation notes; no fixed token cap is stated.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
