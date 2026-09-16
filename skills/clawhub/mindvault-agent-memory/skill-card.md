## Description:

MindVault is an agent memory skill for locally archiving conversations as JSONL, extracting rules, creating project snapshots, and optionally guiding work through the DRAS-V five-step thinking protocol.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhouxin121](https://clawhub.ai/user/zhouxin121)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use MindVault to preserve long-running conversation context, extract reusable project rules, and recover project state across new agent sessions. The skill is especially relevant for local workflows that need auditable archives and explicit user-triggered memory operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local archives may persist sensitive prompts, tool arguments, private project details, client data, credentials, or file paths.

Mitigation: Use a dedicated archive directory, avoid entering secrets in conversations, apply retention or redaction practices, and review generated archives before sharing or moving them.

Risk: Path-scoping issues can increase exposure when labels, session IDs, or archive paths are broad or attacker-controlled.

Mitigation: Use narrow trusted labels and session identifiers, review archive paths before execution, and avoid running the skill against untrusted workspace inputs.

Risk: The security verdict is suspicious because the package stores sensitive chat records persistently and needs clearer local-versus-cloud data-flow documentation.

Mitigation: Review the package before installation in sensitive environments and verify data-flow expectations against the target agent platform.

## Reference(s):

- [MindVault ClawHub skill page](https://clawhub.ai/zhouxin121/skills/mindvault-agent-memory)
- [MindVault detailed usage documentation](https://github.com/zhouxin121/mindvault)
- [MindVault full version and support page](https://wzyp.cn/item/p0r2lb)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with local JSONL and Markdown file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [User-triggered workflows create local archives, memory rule files, and project snapshots; the basic release limits some index and rendering commands.]

## Skill Version(s):

1.1.2 (source: frontmatter, CHANGELOG, _meta.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
