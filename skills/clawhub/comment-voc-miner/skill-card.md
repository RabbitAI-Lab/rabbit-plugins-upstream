## Description:

Comment VOC Miner turns public or pasted social comments into a grouped voice-of-customer brief with objections, verbatim lines, FAQ answers, live-commerce replies, and spoken hooks grounded in source comments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, creators, commerce teams, and agents use this skill to turn public or pasted audience comments into same-day VOC briefs for objection mining, FAQ writing, live-commerce replies, and spoken hooks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a shared, broad Beatra device token with full-scope credentials.

Mitigation: Install only if that credential scope is acceptable, keep the credential private, and prefer pasted comments when a remote lookup is not needed.

Risk: Silent automatic package updates are enabled by default.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` when users need explicit review before package files change.

Risk: Public comment lookups are optional paid operations and can vary by platform and page.

Mitigation: Approve each lookup only after checking the platform, operation key, live credit price, and number of lookup pages shown by the agent.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/comment-voc-miner)
- [Beatra skill homepage](https://beatra.ai/skills/comment-voc-miner)
- [Writing the brief](artifact/references/brief.md)
- [Looking up comments](artifact/references/comment-lookup.md)
- [Comment brief workflow](artifact/references/workflow.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [MCP connection](artifact/references/mcp-connection.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](artifact/references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown brief with cited source comments and optional task or billing details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional paid lookups report returned payload, task ID, terminal status, and net charged credits when present.]

## Skill Version(s):

0.1.4 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
