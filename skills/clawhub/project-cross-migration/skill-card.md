## Description:

A third-party ClawHub skill for migrating local project materials across agent frameworks, including raw conversation JSONL, project memory, persona/tool materials, validation, and readable restoration in the free edition.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhouxin121](https://clawhub.ai/user/zhouxin121)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to validate, restore, and migrate local project archives between agent frameworks while preserving raw conversation context and project memory. It is intended for private, local migrations unless the user has a working desensitization path and manually checks the package before sharing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles raw project archives and credentials by default.

Mitigation: Use it only for private, local migrations under the user's control; encrypt or restrict access to backup archives and avoid including live credentials unless deliberately moving them.

Risk: Sharing a generated package can expose credentials or private conversation content if desensitization is unavailable or incomplete.

Mitigation: Do not share generated packages unless a working desensitization path is available and the user manually verifies that credentials and private conversation content were removed.

Risk: Some safety-related features are locked in the free edition, including confirmation gates, environment snapshots, and the sharing desensitizer.

Mitigation: Treat the free edition as a local migration aid and require manual review of package scope, destination, credentials, and restored content before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhouxin121/skills/project-cross-migration)
- [Publisher profile](https://clawhub.ai/user/zhouxin121)
- [README](README.md)
- [CHANGELOG](CHANGELOG.md)
- [Full edition link](https://wzyp.cn/item/p0r2lb)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Markdown, JSON, Configuration]

**Output Format:** [Markdown guidance with bash commands and generated JSON, JSONL, and Markdown files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Free edition locks the confirmation gate, environment snapshot, and sharing desensitizer entries; local migration packages may include private credentials unless the user intentionally creates and verifies a share package.]

## Skill Version(s):

2.4.2 (source: frontmatter, CHANGELOG, evidence release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
