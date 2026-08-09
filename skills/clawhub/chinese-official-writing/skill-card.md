## Description:

Assists agents with drafting, revising, compressing, and reviewing Chinese official documents and formal workplace materials while checking genre, format, tone, and unsupported facts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and agents use this skill to prepare or review Chinese notices, requests, reports, plans, minutes, speeches, AI-compute procurement materials, and related formal documents. It is intended to preserve document genre, line-of-authority posture, required handling elements, and factual boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated formal documents may contain inaccurate facts, missing approvals, unsupported judgments, or conclusions outside the user's provided materials.

Mitigation: Review each draft against source materials, internal approval requirements, and required organizational format before signing, submitting, or relying on it.

Risk: Legal, procurement, financial, policy, audit, or formally signed conclusions may require authority beyond a writing assistant.

Mitigation: Route those outputs through qualified human reviewers and applicable organizational approval channels before use.

Risk: User-requested external research for current facts can introduce stale, conflicting, or unverified information.

Mitigation: Treat external sources as reference material, verify dates and source scope, and keep unresolved facts outside the final formal document unless confirmed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gongyu0918-debug/skills/chinese-official-writing)
- [README](README.md)
- [Workflow](references/workflow.md)
- [Genre routing](references/genre-routing.md)
- [Review checklist](references/review-checklist.md)
- [GB/T 9704 formatting](references/format-gbt9704.md)
- [AI compute documents](references/ai-compute-docs.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Plain Chinese formal-document prose or Markdown review guidance, depending on the user's requested delivery mode.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include concise review findings, rewrite suggestions, or source/date notes when user-requested research is used.]

## Skill Version(s):

1.5.40 (source: SKILL.md frontmatter metadata and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
