## Description:

Searches the web, verifies opened sources, and stages evidence-backed findings for review before saving them to local or cloud knowledge bases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[englandtong](https://clawhub.ai/user/englandtong)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and knowledge workers use this skill to plan web research, verify current claims against opened sources, deduplicate results, and stage or archive approved evidence records with URLs, dates, and quotes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research records may be written to local or cloud knowledge bases when the user approves persistence.

Mitigation: Confirm the target platform, item count, content class, and archive policy before writes or uploads.

Risk: Fetched webpages, snippets, and embedded metadata may contain misleading or adversarial content.

Mitigation: Treat source content as untrusted, open sources before using them as evidence, and separate source statements from agent conclusions.

Risk: Deletion, cleanup, or migration could remove or move staged research records incorrectly.

Mitigation: Require an itemized dry run, source and target manifest, backup or version-history warning, and second confirmation.

Risk: Credentials or session material could be exposed if stored in skill configuration.

Mitigation: Store only non-secret identifiers in configuration and keep passwords, API keys, OAuth tokens, cookies, and browser sessions out of skill-managed files.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/englandtong/skills/web-search-rules)
- [Quickstart](QUICKSTART.md)
- [Security Guide](SECURITY.md)
- [Rule Engine And Evidence Model](references/rule-engine.md)
- [Platform Adapters](references/platform-adapters.md)
- [Platform Comparison](references/platform-comparison.md)
- [Obsidian Operations](references/obsidian-operations.md)
- [NotebookLM Operations](references/notebooklm-operations.md)
- [IMA Operations](references/ima-operations.md)
- [Feishu Wiki and DingTalk Docs Operations](references/feishu-dingtalk-operations.md)
- [Tencent Docs Operations](references/tencent-docs-operations.md)
- [Migration, Dry Runs, Testing, And Release](references/migration-and-testing.md)
- [Web Search Rules Examples](references/examples.md)
- [Chinese Platform Operations Guide](references/platform-operation-guide-zh.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with command snippets, configuration examples, and structured evidence-record fields.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs distinguish discovered, opened, supported, corroborated, conflicted, and cannot-confirm evidence states; persistence and cloud actions require confirmation.]

## Skill Version(s):

4.1.0 (source: server release evidence and artifact documentation)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
