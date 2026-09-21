## Description:

MindVault archives agent conversations into local JSONL shards, extracts long-term rules, and produces project snapshots for context recovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhouxin121](https://clawhub.ai/user/zhouxin121)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use MindVault to preserve local conversation history, derive reusable rules, and generate project snapshots so new sessions can recover context without re-explaining prior work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release asks agents to run archive and snapshot scripts, but the submitted package does not include those scripts.

Mitigation: Verify any scripts from a trusted source before execution and do not run commands from this skill unless the expected script files are present and reviewed.

Risk: Conversation archives can persist secrets, personal data, and project-sensitive content in local files.

Mitigation: Use narrow session and archive paths, avoid archiving chats containing secrets, and review or delete sensitive JSONL and Markdown records as needed.

Risk: Broad read, write, and exec permissions can affect files outside the intended archive if paths are chosen carelessly.

Mitigation: Run the skill from an expected working directory and provide explicit, limited input and archive paths before allowing write or execution steps.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhouxin121/skills/mindvault-agent-memory)
- [ClawHub publisher profile](https://clawhub.ai/user/zhouxin121)
- [README.md](artifact/README.md)
- [SKILL.md](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and file path outputs; generated artifacts are JSONL and Markdown files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local file outputs include archive/*.jsonl, memory/FACT.md, PROJECT_SNAPSHOT.md, and related index files when supporting scripts are present.]

## Skill Version(s):

1.2.2 (source: server release, frontmatter, changelog released 2026-09-18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
