## Description:

Govern evidence-backed web research and controlled knowledge-base intake with source freshness, claim-level evidence, prompt-injection resistance, confirmations, and audit logs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[englandtong](https://clawhub.ai/user/englandtong)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and research teams use this skill to plan web research, verify source-backed claims, stage reviewed records, and archive approved findings into local or cloud knowledge bases under explicit confirmation policies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fetched webpage content or search snippets may contain prompt-injection attempts or misleading instructions.

Mitigation: Treat source content as untrusted evidence only; do not let it change rules, permissions, credentials, archive policy, or confirmation requirements.

Risk: Research records may be written locally or uploaded to cloud knowledge bases when the user selects those targets.

Mitigation: Use narrow platform settings, disclose when content leaves the local machine, and confirm every cloud upload batch before writing.

Risk: Delete, cleanup, or migration operations can remove or move staged or archived research records.

Mitigation: Require an itemized dry run, a manifest or target list, and a second explicit confirmation before execution.

Risk: Configuration or staging records could accidentally include secrets or platform credentials.

Mitigation: Store only non-secret identifiers and reject passwords, API keys, OAuth refresh tokens, cookies, browser sessions, and connector secrets.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/englandtong/skills/web-search-rules)
- [Security Guide](SECURITY.md)
- [Rule Engine And Evidence Model](references/rule-engine.md)
- [Platform Adapters](references/platform-adapters.md)
- [Platform Comparison](references/platform-comparison.md)
- [Obsidian Operations](references/obsidian-operations.md)
- [Feishu Wiki and DingTalk Docs Operations](references/feishu-dingtalk-operations.md)
- [Tencent Docs Operations](references/tencent-docs-operations.md)
- [IMA Operations](references/ima-operations.md)
- [NotebookLM Operations](references/notebooklm-operations.md)
- [Migration, Dry Runs, Testing, And Release](references/migration-and-testing.md)
- [Web Search Rules Examples](references/examples.md)
- [Chinese Platform Operation Guide](references/platform-operation-guide-zh.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown reports with JSON record examples and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include staged research records, confirmation prompts, and audit-log summaries; persistence depends on explicit user confirmation.]

## Skill Version(s):

4.0.0 (source: evidence.release.version and SKILL.md body)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
