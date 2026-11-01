## Description:

Memorize Bible verses with Remember Me, the Bible memory app with spaced repetition. Use when the user wants to memorize, learn by heart or keep a Bible verse, review or be quizzed on their memory verses, read today's passages from a one-year Bible reading plan, or find a ready-made collection of verses to memorize. Works through the Remember Me MCP tools (add_verse, get_review_queue, get_daily_reading, browse_collections and others).

This skill is ready for commercial/non-commercial use.

## Publisher:

[pschaffl](https://clawhub.ai/user/pschaffl)

### License/Terms of Use:

MIT-0

## Use Case:

Bible learners use this skill to add verses to Remember Me, practice due verses, read daily portions from a one-year Bible plan, and discover published collections. In OpenClaw, the integration supports browsing public collections; authenticated clients can also manage the user's verses and collections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated access can change the signed-in user's verses and collections.

Mitigation: Use the intended account, review proposed batch additions before saving, and ask before deleting verses.

Risk: Unlisted collections can still be opened by anyone with their link.

Mitigation: Treat unlisted collection links as shareable and avoid putting sensitive content in those collections.

## Reference(s):

- [Connecting Remember Me](references/connect.md)
- [Remember Me vocabulary](references/vocabulary.md)
- [Remember Me MCP documentation](https://www.remem.me/docs/mcp/)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Guidance]

**Output Format:** [Conversational text and Remember Me tool calls]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Verse wording follows the selected translation; review results are not saved by the assistant.]

## Skill Version(s):

1.0.7 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
