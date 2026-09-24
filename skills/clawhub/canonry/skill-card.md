## Description:

Navigate Canonry through connected MCP tools or the `cnry` CLI to inspect evidence, diagnose changes, plan measurement, review integrations, and report results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

External operators, developers, and marketing teams use this skill to operate Canonry through MCP or the Canonry CLI, inspect saved AI visibility evidence, diagnose measurement changes, review integrations, and prepare reports without treating the skill as an authorization mechanism.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide broad Canonry operations, including writes, schedules, syncs, ads actions, WordPress changes, and destructive disconnect or delete commands.

Mitigation: Require explicit approval for the exact target, action, and bounded work before executing any write, sync, schedule, provider read, quota-spending operation, or externally visible action.

Risk: Credentials, OAuth secrets, API keys, and provider tokens may be involved in Canonry setup and integrations.

Mitigation: Keep secrets out of chat, tool arguments, reports, and public guidance; use secure setup flows or private terminal commands and prefer read-only or project-scoped keys when possible.

Risk: Read-only labels and dry-run style previews may not fully describe cost, authorization, or provider-side effects.

Mitigation: Inspect tool descriptions and saved state first, preserve approval boundaries, and verify receipts or saved evidence before retrying ambiguous operations.

## Reference(s):

- [Canonry Operations Guide v1](artifact/SKILL.md)
- [Canonry CLI Reference](artifact/references/canonry-cli.md)
- [AEO Analysis: Interpreting Canonry Results](artifact/references/aeo-analysis.md)
- [Indexing Workflow](artifact/references/indexing.md)
- [WordPress Integration](artifact/references/wordpress-integration.md)
- [Server-side Traffic](artifact/references/server-side-traffic.md)
- [Google Business Profile Integration](artifact/references/google-business-profile.md)
- [Google Ads and GTM Evidence Boundaries](artifact/references/google-marketing.md)
- [Canonry Skill Page](https://clawhub.ai/arberx/skills/canonry)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline CLI commands and structured JSON references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses saved evidence first and requires explicit approval before live provider reads, quota-spending operations, writes, syncs, schedules, or externally visible actions.]

## Skill Version(s):

5.16.0+fbd3ec6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
