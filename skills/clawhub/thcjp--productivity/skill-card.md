## Description: <br>
Productivity helps agents build and maintain a local Markdown productivity system for goals, projects, tasks, habits, planning, reviews, focus sessions, commitments, and context-specific adjustments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and knowledge workers use this skill to create and operate a local productivity system that connects goals to projects, tasks, habits, planning, reviews, focus work, and commitments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The local ~/productivity/ directory can contain sensitive goals, commitments, habits, preferences, and work context. <br>
Mitigation: Keep the directory private, review backups or sync settings, and avoid sharing generated files unless their contents have been reviewed. <br>
Risk: The skill may create or update local productivity Markdown files. <br>
Mitigation: Confirm file writes before execution and review proposed changes to productivity records before accepting them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/productivity) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>
- [Artifact SKILL.md](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown responses with optional shell commands and local Markdown file updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses local files under ~/productivity/ and should write preferences or productivity records only after explicit user confirmation.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
