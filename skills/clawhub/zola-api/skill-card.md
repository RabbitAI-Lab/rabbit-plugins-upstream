## Description:

Query or update Zola wedding-planning data (vendors, budget, guests, seating, events/RSVPs, registry, gift tracker, inquiries, wedding website) straight from a shell with curl against mobile-api.zola.com, instead of running the zola-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query or update Zola wedding-planning records from shell scripts with curl and jq. It covers account data such as vendors, budgets, guests, events, registries, and wedding website content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup example can expose a reusable refresh token in command output or logs.

Mitigation: Load credentials from protected storage without printing or logging them, and rotate any token already exposed in retained output.

Risk: A website settings change could unintentionally make the wedding website searchable.

Mitigation: Preserve existing search-visibility settings unless a change is requested, and review the setting before saving.

Risk: Deletes, public website edits, or whole-record writes can affect existing data beyond the intended change.

Mitigation: Review deletions and public edits, and preserve unrelated record fields when updating records.

## Reference(s):

- [Mobile API Endpoint Recipes](artifact/references/mobile-api-endpoints.md)
- [Zola Mobile API](https://mobile-api.zola.com)
- [Zola](https://www.zola.com)
- [ClawHub Skill Release](https://clawhub.ai/chrischall/skills/zola-api)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline curl and jq code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands rely on the user's Zola account credentials and account identifiers; write examples may replace whole records and require preserving existing fields.]

## Skill Version(s):

2.2.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
