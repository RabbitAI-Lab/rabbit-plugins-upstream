## Description:

Drafts, rewrites, compresses, and reviews Chinese official and formal work documents while checking genre, format, official tone, and unsupported facts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, public-sector staff, educators, and business users use this skill to draft or review Chinese official documents such as requests, reports, notices, plans, meeting minutes, procurement materials, and AI-compute service documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated legal, financial, procurement, audit, or signing conclusions may be mistaken for final authority.

Mitigation: Treat those outputs as drafts and route them to the appropriate human reviewer before use.

Risk: Drafting may introduce unsupported real-world facts, dates, amounts, contacts, approvals, or document metadata when source material is incomplete.

Mitigation: Use only user-provided or verified facts, leave unresolved elements out of the body or mark them for confirmation, and review the final text before formal submission.

Risk: Local linting can process sensitive draft content.

Mitigation: Run the lint script only on documents the user is comfortable processing locally, and treat script results as advisory rather than automatic edits.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/gongyu0918-debug/skills/chinese-official-writing)
- [README](README.md)
- [Writing Workflow](references/workflow.md)
- [Genre Routing](references/genre-routing.md)
- [Handling Elements](references/handling-elements.md)
- [Review Checklist](references/review-checklist.md)
- [GB/T 9704-2012 Format Reference](references/format-gbt9704.md)
- [AI Compute Documents](references/ai-compute-docs.md)
- [Anti-AI Expression Checks](references/anti-ai-patterns.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Chinese prose, Markdown review notes, and occasional inline shell commands for local linting]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce full document drafts, revised text, concise review findings, format checks, or local lint command suggestions depending on the user's requested mode.]

## Skill Version(s):

1.6.0 (source: release evidence, SKILL.md frontmatter, README, agents/openai.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
