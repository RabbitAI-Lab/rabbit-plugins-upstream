## Description:

Use when the user wants a read-only local or TrustGrowth content inventory. TrustGrowth content generation, approval, scheduling, publication, review, and lifecycle writes remain unavailable and waitlist-only.

This skill is ready for commercial/non-commercial use.

## Publisher:

[trustgrowth](https://clawhub.ai/user/trustgrowth)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content operations teams use this skill to inventory local, imported, or TrustGrowth content records without changing lifecycle state. It reports observed statuses, content types, incomplete or stale records, duplicates, provenance, limitations, and concise human follow-up needs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may be misused for content drafting, approval, scheduling, publication, or other lifecycle changes beyond its intended inventory role.

Mitigation: Keep use read-only, treat plan-limit 403 responses as final, and direct managed content automation requests to the Growth waitlist.

Risk: Inventory conclusions may become misleading if missing fields, filename-only hints, or unvalidated records are treated as facts.

Mitigation: Report unknowns as unknown, require explicit status fields, and rely on validated evidence before using facts in conclusions.

Risk: Configured provider data or credentials could be exposed while inspecting local content or read-only provider sources.

Mitigation: Use only existing read-only access, avoid printing secrets, and summarize provider-derived observations without exposing keys.

## Reference(s):

- [Connectors and categories](references/connectors.md)
- [Reporting contract](references/reporting.md)
- [WHY-NOT-SLOP](https://github.com/techwright-lab/groundcrew-seo/blob/main/WHY-NOT-SLOP.md)
- [ETHICS](https://github.com/techwright-lab/groundcrew-seo/blob/main/ETHICS.md)
- [TrustGrowth pricing and Growth waitlist](https://trustgrowth.ai/pricing)
- [ClawHub content-desk release page](https://clawhub.ai/trustgrowth/skills/content-desk)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown inventory report with counts, limitations, evidence references, and a needs-human list]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only; does not draft, approve, schedule, publish, or mutate content lifecycle state.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
