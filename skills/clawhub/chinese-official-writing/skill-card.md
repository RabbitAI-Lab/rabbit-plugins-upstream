## Description:

Drafts, rewrites, condenses, and reviews Chinese official documents and formal workplace materials, including genre checks, format checks, de-formalization cleanup, and low-AI-tone review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, writers, reviewers, and agents use this skill to draft or review Chinese official documents, formal work materials, AI-compute procurement materials, and related public-sector or workplace texts while preserving genre, addressing, formatting, and fact-boundary constraints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Legal, financial, procurement, audit, or formal-signature outputs may be treated as final decisions even though the skill produces drafts and review guidance.

Mitigation: Require human review before using these outputs for official decisions, submissions, procurement actions, audits, or signatures.

Risk: The optional local prose linter reads draft documents supplied to the agent.

Mitigation: Run the linter only on documents the user is comfortable exposing to their local agent environment.

Risk: Chinese official-document drafts can sound authoritative while relying on incomplete user-provided facts.

Mitigation: Check dates, amounts, policy references, responsible parties, approvals, and required document elements before release.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/gongyu0918-debug/skills/chinese-official-writing)
- [README](README.md)
- [Skill Entry](SKILL.md)
- [Writing Workflow](references/workflow.md)
- [Genre Routing](references/genre-routing.md)
- [Handling Elements](references/handling-elements.md)
- [Review Checklist](references/review-checklist.md)
- [Anti-AI Expression Checks](references/anti-ai-patterns.md)
- [GB/T 9704 Format Reference](references/format-gbt9704.md)
- [AI Compute and Technical Service Materials](references/ai-compute-docs.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, shell commands]

**Output Format:** [Plain text or Markdown, with optional shell commands for the local prose linter]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include drafted Chinese official-document prose, review findings, revision suggestions, formatted body text, or local lint guidance.]

## Skill Version(s):

1.5.37 (source: server release metadata, SKILL.md metadata, README, and OpenClaw metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
