## Description: <br>
Drafts, revises, compresses, and reviews Chinese official documents and formal work materials, including genre checks, format checks, formal-tone editing, and AI-style reduction. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Chinese-speaking employees, external users, and agent developers use this skill to prepare or review formal work documents such as requests, reports, notices, plans, summaries, speeches, feasibility materials, and AI-compute procurement materials. It helps preserve official-document structure, writing posture, handling elements, and fact boundaries while reducing informal or AI-like phrasing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The optional lint script reads draft files passed to it, which may expose sensitive formal documents inside the user's agent environment. <br>
Mitigation: Avoid running the lint script on sensitive drafts unless the user is comfortable processing those files in the active environment. <br>
Risk: Formal legal, financial, procurement, audit, and signed-document conclusions may require domain judgment beyond drafting support. <br>
Mitigation: Require human review before relying on outputs for formal approval, signature, procurement, audit, legal, or financial decisions. <br>
Risk: Drafted official documents can become misleading if unsupported facts, policy claims, figures, dates, or approval conclusions are added. <br>
Mitigation: Constrain drafts to user-provided evidence and separately confirm time-sensitive or authoritative facts when the user requests source checking. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gongyu0918-debug/skills/chinese-official-writing) <br>
- [README](README.md) <br>
- [Skill entry](SKILL.md) <br>
- [Writing workflow](references/workflow.md) <br>
- [Genre routing](references/genre-routing.md) <br>
- [Handling elements](references/handling-elements.md) <br>
- [Information selection](references/information-selection.md) <br>
- [Argument chains](references/argument-chains.md) <br>
- [Review checklist](references/review-checklist.md) <br>
- [Final review layers](references/final-review-layers.md) <br>
- [Anti-AI expression checks](references/anti-ai-patterns.md) <br>
- [GB/T 9704-2012 format reference](references/format-gbt9704.md) <br>
- [AI compute and technical service materials](references/ai-compute-docs.md) <br>
- [External research guidance](references/external-research.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Plain text or Markdown drafts, revised document text, review findings, and concise editing guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include issue lists, rewrite suggestions, formal-document structure checks, and fact-boundary reminders.] <br>

## Skill Version(s): <br>
1.5.34 (source: evidence release, metadata, and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
