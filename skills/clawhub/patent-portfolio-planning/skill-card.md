## Description:

Helps teams compare technology routes and plan patent filing priorities, timing, and budgets using PatentMax patent data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

R&D and IP teams use this skill to compare technology routes, prioritize patent filings, allocate budgets, and plan applications around disclosure dates. Its recommendations are technical and commercial guidance, not legal advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive patent strategy, technical materials, budgets, and confidentiality constraints may be sent to PatentMax.

Mitigation: Get approval before sharing proprietary information; omit or redact unnecessary secrets and specify confidentiality limits.

Risk: A configurable service endpoint can receive submitted content and API credentials.

Mitigation: Use only a trusted PatentMax endpoint and ensure PATENTMAX_BASE_URL cannot be changed by an untrusted party.

Risk: A free-trial credential may remain on the local machine.

Mitigation: Inspect or remove ~/.patentmax/ when local credential retention is not wanted.

Risk: Patent database gaps and unpublished applications can make clearance or novelty conclusions incomplete.

Mitigation: Avoid guarantees of freedom to operate and have a qualified patent professional review filing and infringement decisions.

Risk: Creating an analysis is a paid task and retries can incur additional charges.

Mitigation: Quote the cost and obtain explicit approval before submission; check existing task status rather than resubmitting after a timeout.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ip930/skills/patent-portfolio-planning)
- [PatentMax API platform](https://api.ip930.com/features/api-platform)
- [Business context guide](references/context-guide.md)
- [Planning workflow](references/workflow.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Word documents]

**Output Format:** [Markdown recommendations and a downloadable DOCX report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Route comparisons, filing priorities, budget and timing recommendations, and patent risk summaries; report quality indicators when available.]

## Skill Version(s):

1.0.0 (source: release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
