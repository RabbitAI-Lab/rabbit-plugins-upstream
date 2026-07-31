## Description: <br>
Drafts, revises, compresses, and reviews Chinese official and formal workplace documents, including genre checks, formatting checks, formal tone revision, and AI-style reduction. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and agents use this skill to draft or review Chinese official documents and formal work materials such as requests, reports, notices, plans, minutes, institutional rules, procurement materials, and AI-compute service documents. It is also used to check document genre, administrative relationship, required handling elements, formal style, placeholders, and review risks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Official documents may contain sensitive, regulated, legal, financial, procurement, audit, or final-signature material. <br>
Mitigation: Use the skill only on materials the user is permitted to process, and manually review legal, financial, procurement, audit, and final-signature content before relying on the result. <br>
Risk: Drafts can become misleading if unsupported facts, real entities, amounts, dates, approval conclusions, signatures, seals, or policy details are invented. <br>
Mitigation: Keep generated content within user-provided facts, preserve stated fact boundaries, and require manual confirmation for missing or uncertain official-document elements. <br>
Risk: Web search or DOCX editing can increase exposure or change source documents in ways the user did not intend. <br>
Mitigation: Allow web search or DOCX editing only when explicitly needed, and preserve original document versions unless the user clearly asks to overwrite them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gongyu0918-debug/skills/chinese-official-writing) <br>
- [README](README.md) <br>
- [Writing workflow](references/workflow.md) <br>
- [Genre routing](references/genre-routing.md) <br>
- [Handling elements](references/handling-elements.md) <br>
- [Final review layers](references/final-review-layers.md) <br>
- [GB/T 9704-2012 format reference](references/format-gbt9704.md) <br>
- [AI compute and technical service materials](references/ai-compute-docs.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, shell commands] <br>
**Output Format:** [Plain text or Markdown, with optional shell commands for local prose linting when relevant] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce full document drafts, revised text, concise review findings, formatting guidance, or DOCX-editing guidance when the user explicitly requests document-file work.] <br>

## Skill Version(s): <br>
1.5.31 (source: SKILL.md metadata, README, ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
