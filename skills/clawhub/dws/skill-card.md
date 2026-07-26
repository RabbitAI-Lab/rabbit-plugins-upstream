## Description: <br>
dws helps agents operate DingTalk work products through the dws CLI, including tables, search, calendars, contacts, chat, tasks, approvals, attendance, reports, documents, drive files, meeting minutes, mail, spreadsheets, and wikis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[flyredm](https://clawhub.ai/user/flyredm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to route DingTalk requests to documented dws CLI commands and helper scripts for business workflows such as messaging, scheduling, document work, approvals, attendance, reporting, and data operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access sensitive DingTalk communications, identity data, documents, attendance records, and meeting minutes. <br>
Mitigation: Install only for users who need broad DingTalk operations, scope account access carefully, and avoid using private chat history for speaker identification unless affected users have clearly approved it. <br>
Risk: The skill can trigger visible or state-changing business actions such as messages, email, tasks, directory changes, approvals, permission changes, PAT grants, attendance changes, and speaker-label replacement. <br>
Mitigation: Require explicit user confirmation before those actions and use dry-run or preview flows where the skill provides them. <br>
Risk: Some helper behavior can mutate the local Python environment by installing dependencies during execution. <br>
Mitigation: Preinstall required dependencies in the runtime environment and do not allow helper scripts to run pip during normal skill execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/flyredm/skills/dws) <br>
- [SKILL.md](SKILL.md) <br>
- [Intent guide](references/intent-guide.md) <br>
- [Global reference](references/global-reference.md) <br>
- [Capability limits](references/capability-limits.md) <br>
- [Recovery guide](references/recovery-guide.md) <br>
- [URL patterns](references/url-patterns.md) <br>
- [Best practices](references/best_practices/lite-recipes.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration] <br>
**Output Format:** [Markdown with dws CLI commands and JSON-oriented workflow guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Prefers --format json command output, documented helper scripts, dry-run previews, and explicit confirmation for sensitive actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
