## Description: <br>
Captures learnings, errors, and corrections to enable continuous improvement. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gasgangrene](https://clawhub.ai/user/gasgangrene) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to capture command failures, user corrections, missing capability requests, and recurring workflow learnings in durable markdown logs. The logs can then be reviewed, resolved, deduplicated, or promoted into workspace guidance for future agent sessions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Learning logs and optional session-end error summaries may contain sensitive workspace context. <br>
Mitigation: Keep .learnings out of version control unless intentionally sharing it, redact secrets, and prefer concise summaries over raw transcripts or full command output. <br>
Risk: Promoting unreviewed entries into workspace guidance can preserve incorrect or misleading agent behavior. <br>
Mitigation: Review entries before promotion into AGENTS.md, TOOLS.md, or SOUL.md, and mark stale or incorrect entries as resolved or wont_fix. <br>
Risk: The optional OpenClaw hook can derive error summaries from ended session transcripts. <br>
Mitigation: Enable the hook only in trusted workspaces where transcript-derived summaries are acceptable, and disable the sweep by removing the .learnings directory. <br>


## Reference(s): <br>
- [Self-Improving Agent on ClawHub](https://clawhub.ai/gasgangrene/skills/self-improving-agent) <br>
- [OpenClaw Integration](references/openclaw-integration.md) <br>
- [Entry Examples](references/examples.md) <br>
- [Uninstall Guide](references/uninstall.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Files, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and file templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates or appends local .learnings markdown files and may emit setup commands for optional OpenClaw hook installation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter reports 4.0.0 and artifact _meta reports 4.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
