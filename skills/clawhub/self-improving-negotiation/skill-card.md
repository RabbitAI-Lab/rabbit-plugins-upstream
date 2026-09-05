## Description:

Logs redacted negotiation learnings and provides optional project-scoped reminder hooks plus dry-run skill extraction without accepting terms, setting pricing, approving deals, or finalizing agreements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jose-compu](https://clawhub.ai/user/jose-compu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agent operators use this skill to capture redacted negotiation issues, learnings, and feature requests so recurring patterns can be reviewed and promoted into playbooks, objection libraries, concession guardrails, BATNA checklists, or deal review templates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Negotiation logs can expose BATNA values, pricing floors, confidential terms, legal advice, approval tokens, or raw transcripts.

Mitigation: Record only redacted process-level summaries and keep .learnings private or reviewed before committing.

Risk: Reminder hooks could become too broad or persistent if installed globally.

Mitigation: Enable hooks only at the project level and keep them reminder-only.

Risk: Generated SKILL.md scaffolds may encode incomplete or unsafe negotiation practices.

Mitigation: Use extraction in dry-run mode by default and review any generated diff before using or publishing it.

Risk: Agents may overstep by treating negotiation guidance as authorization.

Mitigation: Require explicit human approval for high-impact concessions, final terms, pricing commitments, legal approvals, and agreement finalization.

## Reference(s):

- [Negotiation Entry Examples](references/examples.md)
- [Hook Setup Guide](references/hooks-setup.md)
- [OpenClaw Integration](references/openclaw-integration.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local learning entries, reminder text, setup guidance, and dry-run skill scaffolds that require review before use.]

## Skill Version(s):

1.0.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
