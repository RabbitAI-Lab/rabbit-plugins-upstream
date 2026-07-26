## Description: <br>
Manage OmniFocus tasks via JavaScript for Automation (JXA) scripts, including adding, listing, searching, completing, updating, summarizing, and acting on tasks in OmniFocus based on user queries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shenzo1](https://clawhub.ai/user/shenzo1) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and OmniFocus users use this skill to let an agent inspect and manage local OmniFocus tasks through macOS JXA scripts. It supports task review, inbox triage, search, completion, property updates, statistics, and user-facing summaries of task status. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read OmniFocus task names, notes, dates, tags, and projects, which may expose sensitive personal or work information to the agent. <br>
Mitigation: Install only when agent access to OmniFocus data is intended, and avoid storing sensitive information in task notes unless agent visibility is acceptable. <br>
Risk: The skill can modify local OmniFocus data by adding tasks, completing matching tasks, and updating notes, due dates, or flags. <br>
Mitigation: List or search matching tasks before mutating them, and confirm the target task when names may be duplicated. <br>


## Reference(s): <br>
- [ClawHub OmniFocus Skill Page](https://clawhub.ai/shenzo1/skills/omnifocus) <br>
- [OmniFocus Automation Guide](references/automation-guide.md) <br>
- [OmniFocus JXA API Reference](references/jxa-api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, JSON, guidance] <br>
**Output Format:** [Markdown or text with inline shell commands and parsed JSON task data] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Local macOS execution via osascript; mutating operations can add, complete, or update OmniFocus tasks.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
