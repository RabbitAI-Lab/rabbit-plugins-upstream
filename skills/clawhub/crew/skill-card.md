## Description:

Crew helps a Claude Code session manage cooperating agents in iTerm2 panes, including starting agents, exchanging messages, and saving or restoring a group.

This skill is ready for commercial/non-commercial use.

## Publisher:

[garmanwu](https://clawhub.ai/user/garmanwu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers using Claude Code can start Codex, Antigravity, or Claude Code agents in visible iTerm2 panes, coordinate them through messages, and save or restore the group with its session details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan rates the release suspicious because agents may be launched without sandboxing or approval checks, and workspace trust may be accepted automatically.

Mitigation: Review the project contents and trust state before launching agents. Use Codex with its sandbox enabled where practical, and review the permissions and approval behavior for each selected agent.

Risk: ClawScan reports that a generated launcher may use unsafe paths or injected shell commands.

Mitigation: Inspect the generated .command launcher and its paths before running it, and use it only from a project directory you have reviewed.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/garmanwu/skills/crew)
- [Crew project repository](https://github.com/garmanwu/crew)
- [Claude Code](https://claude.com/claude-code)

## Skill Output:

**Output Type(s):** [JSON, Configuration files, Shell commands, Guidance]

**Output Format:** [JSON status responses, a .crew.json group state file, and a .command restore launcher]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands and saved state depend on the chosen agents, models, effort settings, and project directory.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
