## Description: <br>
Audit and repair agent memory systems using DDIA reliability + DDD bounded-context analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[milesnee](https://clawhub.ai/user/milesnee) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to assess OpenClaw-style agent memory systems, identify stale or inconsistent memory content, and plan prioritized maintenance before making changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide broad edits to agent memory and behavior files, including MEMORY.md and AGENTS.md. <br>
Mitigation: Run baseline and diagnosis read-only first, then require a proposed diff and explicit approval before repairs, memory updates, cron setup, or trace-logging integration. <br>


## Reference(s): <br>
- [Audit Checklist](references/audit-checklist.md) <br>
- [DDIA + DDD Memory System Mapping](references/ddia-ddd-mapping.md) <br>
- [Audit Report Template](assets/audit-report-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown audit reports, JSON baseline data, inline shell commands, and proposed code or configuration changes.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Baseline and diagnosis phases should be run read-only before proposing repairs.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
