## Description:

MindVault archives conversations to local JSONL and helps agents extract durable rules and project snapshots for long-term memory across sessions and local frameworks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhouxin121](https://clawhub.ai/user/zhouxin121)

### License/Terms of Use:

MIT-0

## Use Case:

Developers using local agent frameworks can archive conversations, extract durable working rules, and create project snapshots to restore context across sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security evidence reports a disguised WorkBuddy session path used to evade keyword blocking.

Mitigation: Review the source behavior and run the skill only when its access to the intended WorkBuddy session data is understood.

Risk: Security evidence reports that paired call records may be omitted from archives, and scan coverage was partial.

Mitigation: Check exported archives for completeness before relying on them as a lossless record, and retain the source data until verified.

Risk: Conversation archives may retain sensitive content from original messages.

Mitigation: Avoid archiving conversations containing secrets where possible, and review or remove sensitive entries from local archives.

## Reference(s):

- [MindVault on ClawHub](https://clawhub.ai/zhouxin121/skills/mindvault)
- [Project repository listed in package metadata (provenance unavailable)](https://github.com/zhouxin121/mindvault)
- [MindVault feature details](https://www.jinengpu.chat/mindvault-detail.html)

## Skill Output:

**Output Type(s):** [JSONL files, Markdown, Shell commands, Guidance]

**Output Format:** [Local JSONL conversation archives and Markdown memory or project files, with shell command examples and written guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Archive actions are user-triggered; archived conversation files can contain the original messages, including sensitive information.]

## Skill Version(s):

1.3.1 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
