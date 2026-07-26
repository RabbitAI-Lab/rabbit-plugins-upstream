## Description: <br>
Helps users create practical workflows, checklists, analysis, code changes, and decision support for Gog-style Google Workspace and productivity tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External agent users, skill authors, maintainers, and teams use this skill to turn demand for Gog-style Google Workspace workflows into concrete plans, templates, checklists, implementation help, and reliability guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad triggers and implicit invocation may activate the skill during unrelated Gmail, Drive, Calendar, or CLI tasks. <br>
Mitigation: Review trigger settings before installation and prefer explicit invocation when the workspace task is sensitive or ambiguous. <br>
Risk: Google Workspace actions can affect mail, calendars, files, sheets, or contacts. <br>
Mitigation: Keep OAuth scopes limited and require confirmation before sending mail, creating calendar items, changing Drive or Sheets content, or accessing contacts. <br>


## Reference(s): <br>
- [Requirement Plan](artifact/references/requirement-plan.md) <br>
- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/work-productivity-gog-google-workflow-helper-002325) <br>
- [Popular ClawHub skill demand: Gog](https://clawhub.ai/skills/gog) <br>
- [Hacker News: Fired by Google for creating the Google workspace CLI](https://news.ycombinator.com/item?id=48650067) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with optional code blocks and command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include assumptions, validation notes, remaining risks, and follow-up work.] <br>

## Skill Version(s): <br>
0.1.1 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
