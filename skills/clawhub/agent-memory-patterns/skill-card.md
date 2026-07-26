## Description: <br>
Provides patterns and example snippets for persistent agent memory using daily logs, curated long-term memory, grep-based search, staged external-content review, scheduled maintenance, and heartbeat checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byron-mckeeby](https://clawhub.ai/user/byron-mckeeby) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent builders use this skill to design local persistent memory for long-running agents, including daily note files, curated long-term memory, search routines, staged review of external content, and maintenance schedules. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent local memory can retain secrets, sensitive personal data, or stale context. <br>
Mitigation: Do not store secrets or sensitive personal data in memory files, and periodically prune or archive old notes so future agent context remains appropriate. <br>
Risk: Example scripts and cron entries write to local paths and may not match a user's workspace layout. <br>
Mitigation: Review and adjust all paths before running any example script or scheduled job. <br>
Risk: External content queued into memory may be untrusted or unverified. <br>
Mitigation: Use the staged pending-memory review flow to check reliability, consistency, value, and classification before promoting external content into long-term memory. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/byron-mckeeby/skills/agent-memory-patterns) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with shell and JSON code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Provides local file-based memory workflow examples; no automatic installation or networked execution is described.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
