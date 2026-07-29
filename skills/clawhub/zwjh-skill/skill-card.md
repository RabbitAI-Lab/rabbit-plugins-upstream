## Description: <br>
zwjh-skill provides a local long-term memory and knowledge-graph layer for agents, including memory deposit, semantic and timeline retrieval, conflict resolution, health checks, backups, scheduled autopilot runs, and graph visualization. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fyniujin](https://clawhub.ai/user/fyniujin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users can use this skill to maintain local persistent memory, extract entities and relationships, query prior work, audit memory health, and back up or restore agent memory data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores long-term local memory about the user and their work, which may contain sensitive information. <br>
Mitigation: Review what is deposited, keep backups and snapshots protected, and avoid adding secrets or regulated data unless the local environment is approved for that data. <br>
Risk: The setup and autopilot features can register persistent scheduled execution through cron or schtasks. <br>
Mitigation: Review the scheduled entry before enabling it, and use the remove command if ongoing execution is not desired. <br>
Risk: Backup and snapshot features may create plaintext copies of memory data, and optional Baidu Netdisk backup can upload data through a locally configured bypy account. <br>
Mitigation: Use local backup by default, restrict backup directory permissions, and enable Baidu Netdisk only after confirming the configured account and upload destination. <br>
Risk: The graph web UI references an external CDN dependency for ECharts. <br>
Mitigation: Use the web UI only in environments where that dependency is acceptable, or replace the CDN dependency with an approved local asset before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/zwjh-skill) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and structured local data files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include local SQLite-backed memory records, JSON snapshots, Mermaid graph text, CLI status reports, and browser-served graph views.] <br>

## Skill Version(s): <br>
2.2.0 (source: frontmatter, version.json, server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
