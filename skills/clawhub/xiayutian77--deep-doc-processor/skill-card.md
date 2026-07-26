## Description: <br>
Deep Doc Processor helps agents summarize, extract key points from, compare, report on, and answer questions about user-provided documents across PDF, Word, Markdown, web, and plain-text sources. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xiayutian77](https://clawhub.ai/user/xiayutian77) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and developers use this skill to turn one or more documents or URLs into layered summaries, evidence-backed key points, comparison matrices, structured reports, and follow-up answers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger phrases could activate the skill for requests that are not document-processing tasks. <br>
Mitigation: Confirm the user is asking about provided documents, links, or document-derived follow-up questions before applying the workflow. <br>
Risk: User-provided documents may contain personal or sensitive business information. <br>
Mitigation: Mask personal identifiers in generated reports and remind users to handle sensitive commercial documents carefully. <br>
Risk: Summaries, comparisons, or answers may omit context or overstate conclusions from the source material. <br>
Mitigation: Ground outputs in the supplied content and include source excerpts, locations, or evidence notes when answering detailed questions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xiayutian77/skills/deep-doc-processor) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, files, guidance] <br>
**Output Format:** [Markdown reports, tables, summaries, and question-answer responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write structured reports or comparison matrices to an output directory; privacy-sensitive values should be masked.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
