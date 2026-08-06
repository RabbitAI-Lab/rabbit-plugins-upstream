## Description:

Agent self-awareness of cognitive states such as context fatigue, attention drift, memory debt, confidence erosion, and skill staleness, with protocols to detect, report, and mitigate degrading conditions before they cause failures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to help agents monitor long-running sessions for cognitive degradation, report meaningful status, and choose recovery actions such as session splitting, memory consolidation, or retry-loop interruption.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can lead agents to persist conversation facts, write logs, deploy background monitoring, delegate to subagents, or patch skills without sufficient user control.

Mitigation: Require explicit user approval before memory writes, file logging, cron deployment, subagent delegation, or skill patching, especially in sensitive chats, shared machines, or autonomous-agent settings.

Risk: Passive logging and guardian cron workflows can expose session details or secrets if logs are retained broadly or written with permissive file access.

Mitigation: Redact secrets before logging, set short retention periods, restrict file permissions, and review log destinations before enabling background monitoring.

Risk: Skill-patching guidance can alter future agent behavior if applied without review.

Mitigation: Treat proposed skill patches as changes requiring human review, security scanning, and rollback planning before use.

## Reference(s):

- [Detection Heuristics](artifact/references/detection-heuristics.md)
- [Self-Check Script](artifact/scripts/self_check.py)
- [Guardian Cronjob Template](artifact/templates/guardian-cronjob.yaml)
- [Server-Resolved GitHub Repository](https://github.com/voronindenis5/agent-cognitive-states)
- [ClawHub Skill Page](https://clawhub.ai/voronindenis5/skills/agent-cognitive-states)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional Python script output, JSON reports, shell commands, and YAML configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose memory writes, file logging, background monitoring, subagent delegation, and skill patching; require explicit user approval in sensitive or autonomous settings.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
