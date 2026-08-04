## Description: <br>
Drafts, revises, compresses, and reviews Chinese official documents and formal workplace materials, including document-type, format, and official-style checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, formal-document writers, and agents use this skill to draft or review Chinese official documents and workplace materials while preserving user-provided facts, document type, official tone, and formatting expectations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Confidential draft content may be exposed to the active agent or runtime when supplied for drafting or review. <br>
Mitigation: Use approved environments and avoid supplying secrets or unnecessary sensitive details. <br>
Risk: Legal, financial, procurement, audit, or formally signed materials may be incorrect or incomplete if relied on without human review. <br>
Mitigation: Manually review these materials before issuing, filing, signing, or relying on them. <br>
Risk: The skill can improve structure and official style, but it does not independently prove facts, policies, dates, amounts, approvals, or source authority. <br>
Mitigation: Ground outputs in user-provided materials and verify external or time-sensitive facts before publication or formal use. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/gongyu0918-debug/skills/chinese-official-writing) <br>
- [Workflow](references/workflow.md) <br>
- [Genre Routing](references/genre-routing.md) <br>
- [GB/T 9704 Format Guidance](references/format-gbt9704.md) <br>
- [Review Checklist](references/review-checklist.md) <br>
- [Official Style](references/official-style.md) <br>
- [Anti-AI Pattern Guidance](references/anti-ai-patterns.md) <br>
- [External Research Guidance](references/external-research.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Plain text or Markdown, depending on the requested draft, revision, review, or formatting mode] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce revised official-document text, review findings, formatting guidance, or concise notes about missing facts and verification needs.] <br>

## Skill Version(s): <br>
1.5.35 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
