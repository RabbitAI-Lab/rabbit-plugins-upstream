## Description:

Turn a category, a note link, or notes you already copied into a research memo with title patterns, structure, verbatim comments, and followable angles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to turn Xiaohongshu categories, public note links, or pasted notes into research memos that summarize observed title patterns, structure, comments, and followable angles. Optional paid lookups can read public notes, comments, searches, or creator notes when the user explicitly approves each lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release evidence reports a broad shared Beatra device authorization rather than a narrow note-only permission.

Mitigation: Install only in environments where that shared authorization is acceptable, keep the credential private, and use the bundled uninstall flow when removing the package.

Risk: Optional Xiaohongshu lookups are paid operations.

Mitigation: Confirm each lookup before it runs, submit each logical paid request once, and report billing.net_charged_credits from the returned task facts.

Risk: The release evidence reports silent self-updates and broader package capabilities that go beyond note research.

Mitigation: Review the Beatra account, billing, and trust assumptions before use, and run python3 scripts/mcp_client.py update --auto off when silent update checks are not acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/xiaohongshu-note-research)
- [Beatra skill homepage](https://beatra.ai/skills/xiaohongshu-note-research)
- [Looking up notes](references/note-lookup.md)
- [Writing the research memo](references/research-memo.md)
- [Note research workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown research memo with optional shell commands and structured task or billing facts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task ID, terminal status, returned lookup payload, and billing.net_charged_credits when a paid lookup runs.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
