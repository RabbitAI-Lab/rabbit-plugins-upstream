## Description: <br>
Monitors Hang Seng Indexes press releases, notices, insights, and reports, detects newly published items, matches them against configured indexes, and produces a concise digest per run. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[joeyiptk](https://clawhub.ai/user/joeyiptk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, analysts, and operators use this skill to run an agent-led daily or ad hoc monitor for Hang Seng Indexes announcements and receive a deduplicated digest of items relevant to their configured indexes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill fetches public Hang Seng Indexes content and depends on the website remaining reachable and structurally compatible. <br>
Mitigation: Review digest health warnings and rerun or investigate when sources are blocked, malformed, or skipped. <br>
Risk: The skill stores configuration, scratch data, and deduplication state under ~/.config/hsil-monitor by default. <br>
Mitigation: Set HSIL_MONITOR_HOME to an approved writable location when the default per-user storage path is not appropriate. <br>
Risk: The skill can create a daily OpenClaw cron job during setup if scheduling is approved. <br>
Mitigation: Confirm the schedule before creation and inspect or remove the job with OpenClaw cron commands when needed. <br>
Risk: The setup helper checks commands through a shell=True invocation. <br>
Mitigation: Review the setup helper before execution and replace the command check with shutil.which in a future update. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/joeyiptk/skills/hsil-monitor) <br>
- [Hang Seng Indexes press releases](https://www.hsi.com.hk/en-hk/media-room/#press-releases) <br>
- [Hang Seng Indexes notices](https://www.hsi.com.hk/en-hk/media-room/#index-other-notices) <br>
- [Hang Seng Indexes insights](https://www.hsi.com.hk/en-hk/insights-and-reports/#insights) <br>
- [Hang Seng Indexes reports](https://www.hsi.com.hk/en-hk/insights-and-reports/#reports) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Plain text digest with markdown-style sections and shell command snippets for setup and operation.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill emits the digest as the agent final response; OpenClaw routing is separate from the skill.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter, changelog, version.txt, release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
