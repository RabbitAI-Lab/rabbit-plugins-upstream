## Description: <br>
Learning Review provides five review cycles that help an agent turn learning notes into post-learning reviews, weekly internalization, application checks, archive compression, and knowledge integration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mayf3](https://clawhub.ai/user/mayf3) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents and developers use this skill to review recent learning, convert useful lessons into working behavior, and produce structured learning review reports. It is suited for ongoing learning workflows that already use daily-learning notes and review directories. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Scheduled review workflows can change persistent agent instruction, memory, and skill files without a clear approval or rollback step. <br>
Mitigation: Configure cron use as opt-in, require review of diffs before changes to AGENTS.md, TOOLS.md, SOUL.md, MEMORY.md, memory files, or skills, and keep backups or version control for learning and instruction files. <br>


## Reference(s): <br>
- [Cron configuration templates](references/cron-templates.md) <br>
- [Review report templates](references/templates.md) <br>
- [ClawHub skill page](https://clawhub.ai/mayf3/skills/learning-review) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown reports, checklist tables, and occasional bash setup commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May update persistent agent instruction, memory, and skill files when review or cron workflows are configured.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
