## Description: <br>
Make your AI agent learn and improve automatically by reviewing sessions, extracting learnings, updating memory files, and compounding knowledge over time. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[amangarg1999](https://clawhub.ai/user/amangarg1999) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to review prior work sessions, extract durable learnings, and maintain MEMORY.md, daily memory snapshots, and agent instruction updates. It can also help configure manual, hourly, or nightly review loops for agent memory workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Automated session review and persistent memory edits can capture sensitive, outdated, or incorrect information. <br>
Mitigation: Start with manual review, exclude secrets and sensitive sessions, and inspect diffs before writing MEMORY.md, daily memory files, or AGENTS.md. <br>
Risk: Agent-instruction changes may weaken future behavior if unreviewed session-derived guidance is accepted. <br>
Mitigation: Review proposed instruction changes before use and prune outdated memory regularly. <br>
Risk: Automated commits or pushes can publish session-derived memory before it has been checked. <br>
Mitigation: Keep generated memory out of git until reviewed and do not push session-derived content to remotes automatically. <br>
Risk: Cron or launchd automation can run unattended after setup. <br>
Mitigation: Enable scheduled review only after confirming the job scope, logs, and a clear disable path. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/amangarg1999/skills/ai-compound-1-0-1) <br>
- [Publisher Profile](https://clawhub.ai/user/amangarg1999) <br>
- [AI Compound project link cited by skill documentation](https://github.com/lxgicstudios/ai-compound) <br>
- [LXGIC Studios social link cited by skill documentation](https://x.com/lxgicstudios) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell, JSON, XML, and cron snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces agent-facing review prompts, memory-file structure guidance, and optional scheduling examples.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
